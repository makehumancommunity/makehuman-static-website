---
title: "Application design and Code overview"
draft: false
---

### Application design and Code overview

=### Structural Organization of MakeHuman

MakeHuman is organized hierarchically.  There is a root application (type gui3d.Application) that handles rendering of objects (guicommon.Object). These objects can be added/removed to/from the root application.  Objects added to root application are always visible in the canvas.[I'm wondering if this is really true? - There are object on hidden tabs and the skeleton or mesh can be visible or not.  Am I confusing the distinction between 'canvass' and 'view'? - RWB]  Every added object has an openGL counterpart.
mhmain.MHApplication inherits from root application to constructmain application. A view is a visual context. A tab is a view, for example, the main application is a view.[The main application IS a view or the main application HAS a view? "the "main application frame/window is a view?"- RWB]
The Root application[you do meanrootand notmain? - RWB]contains Categories. A Category (gui3d.Category) is a specialised view object which contains multple taskiew objects (gui3d.TaskView).   Taskview objects are specialised view objects with a panes and tab.  In context of MakeHuman interface, Category objects constitute the  upper row of tabs while taskview objects constitute the lower row of tabs. 
Objects (guicommon.Object) can be added/removed to/from a taskview.  Objects added to a taskview are only visible if the taskview is visible.  For example, a skeleton added to the skeleton chooser is only visible  when the skeleton chooser taskview is visible.  Objects added to root application[root not main? - RWB]are always visible.  Thus objects like human and all proxies such as clothes are added to theapplication,because they should always be visible. Visiblilty can be disabled by setting the visibility flag on objects but an object that is not added to a currently visible taskview, or the application, is not visible, even if its visibility flag is set positive. [Wording needs improving -- 'should always be visible' and a 'visibility flag' are mixed message - RWB]
An object can only be added to one context. So an object is either added to one taskview, or the application, not two different taskviews.
Apart from root application, there is another application (type qtui.Application) which implements MH gui structures using Qtlibraries. mhmain.MHApplication inherits from this application too for handling of gui content.e 
General structure in MH can be represented as: !IMAGE!Pictures/mh-inheritance.png!/IMAGE! 

###  
Basics of event handling in Makehuman: ### 

Makehuman is a GUI based, interactive, Qt application in which objects interact by sending messages to each other. The Qt class QEvent encapsulates notion of low level events like mouse events, key press events, action events, etc. A Qt application is event loop-based, which is basically a program structure which allows events to be prioritized, queued and dispatched to application objects.   
In a Qt based application, there are different sources of events. Some events like key events and mouse events come from window system, while some others originate from within application. When an event occurs, Qt creates an event object to represent it by constructing an instance of the appropriate QEvent subclass, and delivers it to a particular instance of QObject (or one of its subclasses) by calling its event() function. This function does not handle the event itself, but rather, it calls an event handlerbased on the type of event delivered, and sends an acknowlegement based on whether the event was accepted or ignored.
QCoreApplication::exec()method enters the main event loop and waits until exit() is called. It is necessary to call this function to start event handling. In MH, it is done in lib.qtui.Applicationwhich inherits fromQApplicationwhich in turn inherits fromQCoreApplication:
def start(self):
  
        self.OnInit()
  
        self.callAsync(self.started)
  
        self.messages.start()
  
        self.exec_()
  
    
  
In MH, event handling falls in two broad categories.
* Event handling forcontainers(application, categories, taskviews)
* Event handling forwidgets(contained in containers)

=### Event handling for containers:

MH is organized hierarchically in the context of containers.  At top is the main application (core.mhmain.MHMainApplication).  It contains categories (core.gui.Category), which in turn contains taskviews (core.gui.TaskView).
In a Qt-based application, there are five different ways of events processing, as listed below:
* * Reimplementing an event handler function like paintEvent(), mousePressEvent() and so on. This is the most common, easiest, but least powerful approach.
* ReimplementingQCoreApplication::notify( QObject * receiver, QEvent * event ).  This is very powerful, providing complete control; but only one subclass can be active at a time.  Qt's event loop and sendEvent() calls use this approach to dispatch events.
* Installing an event filter onQCoreApplication::instance().  Such an event filter is able to process all events for all widgets.  It's just as powerful as reimplementing notify(); furthermore, it's possible to have more than one application-global event filter. Global event filters even see mouse events for disabled widgets. Note that application event filters are only called for objects that live in the main thread.[I believe that MH is single threaded - implications?  RWB]
* ReimplementingQObject::event()(as QWidget does). If you do this you get Tab key presses[<--Explain what is special about TAB and shift-TAB presses ?- RWB], and you get to see the events before any widget-specific event filters.
* Installing an event filter on the object itself.  Such an event filter gets all the events, including Tab and Shift+Tab key press events[<--Explain what is special about TAB and shift-TAB presses ?- RWB], as long as they do not change the focus widget.
In MakeHuman, approaches 2 and 4  are used for extensively for event handling.  As part of strategy 2,inlib.qtui.Application (which extendsQApplication), notify has been reimplemented:[I don''t understand the implication of this? Expond? -RWB]
def notify(self, object, event):
  
        self.logger_event.debug('notify(%s, %s(%s))', object, event, event.type())
  
        return super(Application, self).notify(object, event)
  
        
  
object is the receiver object. Class implementing notify has to be singleton.  [Clarify? - RWB]
In MakeHuman,MHApplicationsubclasseslib.qtui.Application.MHApplicationobject is the main application object. It's notify function receives notification from the event loop in the underlying Qt layer about each[container only or widgets too?]event, which is then relayed to receiver object's event method. Thereceiver object's event method is either inherited from QObject or reimplemented. The Receiver object then either sends TRUE or FALSE, as the case may be, to[WHERE??] - RWB
lib.qtui.Applicationalso implements an event function, which is called if the receiver object isMHApplication objectitself.  Then,lib.qtui.Application.event()checks if its a user-defined event or not,and it is so true is returned, else we call super class's event().   In case of true being returned,Qt dispatches event to receiver object's callEvent function which determines which function to be called on object to handle the event. Called function then handles the event or propagate it to its parent(or to current task if its application object), as may seem fit.

=### Event handling for widgets

Most of MH widgets are wrappers around Qt widgets. These widgets (defined in module lib.qtgui) inherit from the respective Qt widgets and the Widget class (lib.qtgui.Widget).  MH makes use ofsignal and slot mechanismby making the connection between the signal originating from the Qt layer and the corresponding handler function. For example, class TabBase connects the signal 'currentChanged' to its function 'tabChanged' as follows:
class TabsBase(Widget):
  
    def __init__(self):
  
        super(TabsBase, self).__init__()
  
        self.tabBar().setExpanding(False)
  
        self.connect(self, QtCore.SIGNAL('currentChanged(int)'), self.tabChanged)
  
        ......................
  
        
  
Any class inheriting from TabsBase(e.g., lib.qtgui.Tabs or lib.qtgui.TabBar) also gets this facility.  So now whenever signal 'currentChanged' is emitted from Qt layer function 'tabChanged' is called. The result is that when a user clicks the mouse on a tab, the 'tabChanged' code  will be called,
Similarly, MH Slider widget connects various slider operations to its event handling functions as:
  
...........................
  
    self.connect(self.slider, QtCore.SIGNAL('sliderMoved(int)'), self._changing)
  
    self.connect(self.slider, QtCore.SIGNAL('valueChanged(int)'), self._changed)
  
    self.connect(self.slider, QtCore.SIGNAL('sliderReleased()'), self._released)
  
    self.connect(self.slider, QtCore.SIGNAL('sliderPressed()'), self._pressed)
  
...........................      
[-- EDITING/PROOFING ENDS HERE - RWB --]
 
 

=### Overriding vs event decorators:

The View, Category and Application classes inherit from events3d.EventHandler, hence they have callEvent() function.  The events that apply to this category are usually application-wide. If user make a change that impacts the whole application, and whole application must know about this change, then best way to do so is to call callEvent() for all the taskviews of the application,as follows:
for category in self.categories.itervalues():
  
    for task in category.tasks:
  
        task.callEvent('onMyEvent', params)
A good example is the event of makehuman's scene changing(core.qtui.MHApplication._sceneChanged).  So when callEvent is called on a taskview object and it has onMyEvent implemented,it is being called.  In core.gui3d.View too one can see that most of the events (onShow, onMouseDown,...) on the taskview are propagated by default to their parents - the categories. The categories also are views, so the events are propagated again to their parent, the application. If, again, the application or any category has an onMyEvent method, it is executed.
There are some events that affect the application, but only a single task at a time,for example onMouseDown event. It only happens to the active taskview
  
(the others are hidden, so they receive no mouse events). Once the mouse is pressed, an Application.currentTask.callEvent("onMouseDown", event)is issued. This causes the onMouseDown event to be received by the active Taskview, its parent Category, and finally the Application. This call executes any onMouseDown method in these objects.
Apart from the Category events described above, there are events used for local purposes.  Such events are handled withevent decorators.  Suppose we have a new Taskview, FooTaskView. This Taskview has a 'mybar' member variable, which is of type Bar(events3d.eventHandler).  The requirement is that when self.mybar executes code, we may want to communicate with its parent to inform it about an event that just happened. So, inside the code for Bar, is located a 'self.callEvent('onBaz', 42)' command.  Thus, in the Bar class, we emit a timely event signal and use the event decorator to let the parent Taskview know about the event.  In the  FooTaskView class, but below the place where self.mybar is created, we add:
@self.mybar.mhEvent
  
def onBaz(event):
  
    # code on event.
  
    # guess what, event #  42.
When now the self.mybar Bar reaches that callEvent, the above method, located in FooTaskView, will be executed.
core.mhmain.MHApplication's human is perfect example of this approach.Human has onMouseDown event handler and we need to relay it to application.
  
In loadMainGui function of MHApplication, we add decorator to human attribute as:
def loadMainGui(self):
  
        ..............
  
        
  
        @self.selectedHuman.mhEvent
  
        def onMouseDown(event):
  
          if self.tool:
  
            self.selectedGroup = self.getSelectedFaceGroup()
  
            self.tool.callEvent("onMouseDown", event)
  
          else:
  
            self.currentTask.callEvent("onMouseDown", event)
  
        .............    

Application.human.onMouseDown event is caught and it starts its trip from the Human; it is captured by the decorated method located in Application.loadMainGui (this is the place where the method is bound with the event), it is sent to the currentTask, propagated through the parent category, and finally reaches its destination, the Application.
A more intense process happens on Human.onChanged. This is emitted when a save/load happpens, so the whole application has to know. So it starts from the human, captured by the decorated method in app, sent to ALL the taskviews in MH, and finally through the categories again to the app.
 

=### The MakeHuman Graphical User Interface (GUI):

The MakeHuman GUI is based on the pyQt library which, in turn, is built on the Qt library.   Qt is a development framework for the creation of applications and user interfaces for desktop.
Important GUI classes in MakeHuman are:
lib.qtui.Canvas:This is the class in MakeHuman which takes care of rendering openGL graphics.It inherits from Qt's QGLWidget class which is a widget for rendering OpenGL graphics.  QGLWidget provides functionality for displaying OpenGL graphics integrated into a Qt application. It is very simple to use. You inherit from it and use the subclass like any other QWidget, except that you have the choice between using QPainter and standard OpenGL rendering commands.  
The Canvas class reimplements three functions from parent class to perform openGL tasks:
* paintGL() - Renders the OpenGL scene. It gets called whenever the widget needs to be updated.
* resizeGL() - Sets up the OpenGL viewport, projection, etc. Gets called whenever the widget has been resized (and also when it is shown for the first time because all newly created widgets get a resize event automatically).
* initializeGL() - Sets up the OpenGL rendering context, defines display lists, etc. Gets called once before the first timeresizeGL() orpaintGL() is called.
lib.qtui.Application:  This is the foundation class which manages GUI's control flow and main settings. It inherits fromQtGui.QApplicationandevents3d.EventHandler.  QApplicationcontains the main event loop, where all events from the window system and other sources are processed and dispatched. It also handles the application's initialization and finalization.Application class holds gui main window(instance of lib.qtui.Frame). Application class receives event notifications from underlying Qt user intrface framework and dispatches them to appropriateuser intrface elements in MakeHuman.
GUI architecture inMakeHumanMH can be depicted as follows:


![mh-uiarchitecture.png](mh-uiarchitecture.png)



### Application Design Notes from IRC Chat with Thanassis
Thanasis comments on gaining the big picture of MH coding
* [16:12:57] <Thanasis> I would avoid describing the different parts of code as different entities
* [16:13:43] <Thanasis> ie. follow the object-oriented paradigm, and avoid thinking who is inherited by who etc.
* [16:13:48] <Thanasis> more specifically
* [16:15:03] <Thanasis> I mean, treat an object as a single object
* [16:15:08] <Thanasis> I'll show an example
* [16:15:45] <Thanasis> you have the application. Inheritance says it consists of three classes, QApplication, MHApplication, and mhmain.Application (names may differ a bit).
* [16:15:58] <Thanasis> but it is only one object
* [16:16:42] <Thanasis> We don't care if the QApplication activates a function in MH application, because it happens inside the same object
* [16:16:50] <Thanasis> the application
* [16:17:18] <Thanasis> we only pay attention to the interactions the application object has with other objects
* [16:17:43] <Doctor_Hell_> but if you need to find a function, you need to follow the inheritage chain...no?
* [16:18:24] <Thanasis> of course, in the code, yes. but in a diagram it will make it complex
* [16:21:02] <Thanasis> well, let's go top-down
* [16:21:29] <Thanasis> we have: QT, App, Tab, Task
* [16:21:56] <Thanasis> The event starts from QT, and activates a handler in App
* [16:22:22] <Thanasis> The App sends a new event to the current Task
* [16:22:46] <Thanasis> The task handles it, and sends a copy to the parent Tab
* [16:23:13] <Thanasis> And finally the Tab handles it and sends a copy to the App
* [16:23:35] <Thanasis> which handles it, and stops
* [Referring to how distrating it is to describe the big picture of MH, Thanasis comments ...]
* "Distract? no, this does not consume any brain energy"
* We love your help- the more the bettter -- Thanks [RWB]

Comments Regarding MacroTarget slider processing/handling based on naming conventions:
* [16:36:24] <Doctor_Hell_> [23:26] <Doctor_Hell_> another complex part to know is the engine coded by Jonas to automatically handel the targets using their name
* [16:37:58] <Thanasis> uh. yes, that's a tough one too. I think it does, but I don't remember why and how, because it was a long time ago and Jonas changed the human modifier class since then
* [16:38:18] <Thanasis> he simplified it, actually, but I haven't seen the new version yet
* [16:38:34] <Doctor_Hell_> where is the code?
* [16:38:49] <Thanasis> apps/humanmodifier.py, I think
* [16:39:01] <Doctor_Hell_> Jonas should be very busy recently, since I asked him but he didn't reply me yet.
* [16:42:37] <Thanasis> um by the way, reading humanmodifier alone won't help a lot. I would suggest starting from the macro plugin, to trace what happens when a slider is created, and when the user moves a slider. It might be easier this way
Difficulties in understanding relationships between folder names / module names and the object structure
* [16:39:36] <Doctor_Hell_> ANother thing to understand is why we have some code inapps, other incore, other in libs..the logic is not clear for me..
* [16:39:52] <Thanasis> ah, ignore logic in that part. :)
* [16:40:20] <Thanasis> as far as I know it is all because of mh history so far
* [16:40:29] <Thanasis> the way it developed.
* [16:40:56] <Doctor_Hell_> I know some of it
* [16:41:24] <Doctor_Hell_> in the early times,it was planned to have a core folder, with all important main files
* [16:42:03] <Doctor_Hell_> then anapps folder, to contain many application based on the core files: makeHuman, makeANime, MakeToon, etc..
* [16:42:29] <Doctor_Hell_> butsharedandlibswere added later...I don't know why
* [16:43:10] <Thanasis>libs, they are classes imported from c++ directly
* [16:43:48] <Doctor_Hell_> ah ..so only the "shared" folder is the mystery
* [16:44:04] <Thanasis> shared, they are later classes used by many different parts of the code at the same time
* [16:44:15] <Thanasis> classes created later*
* [16:44:28] <Thanasis> ie. material. It's used literally everywhere
* [16:44:32] <Thanasis> progress too
* [16:44:58] <Doctor_Hell_> ok..at least now it make sense, thank you
 
* Comments on New API project
* [16:45:39] <Doctor_Hell_> now that you have more time, will you look at the API?
* [16:46:55] <Thanasis> 'time' != 'creativity'. I expect it will be easier to me after the start of the semester
* [16:46:27] <Doctor_Hell_> if you are logged to MH site, you can see this:!LINK!http://www.makehuman.org/blog/the_makehuman_api_project_mhapi.html -- http://www.makehuman.org/blog/the_makehuman_api_project_mhapi.html!/LINK!
* [16:47:02] <Doctor_Hell_> Also Joel has already created this:!LINK!https://bitbucket.org/joepal1976/makehuman-api-project/overview -- https://bitbucket.org/joepal1976/makehuman-api-project/overview!/LINK!
* [16:48:52] <Doctor_Hell_> at the moment, you can just post a list of wished api in the issue 534
* [16:49:16] <Doctor_Hell_> we want to start the API in few weeks..they are fundamental, in order to have more contributors...
* [16:51:05] <Thanasis> oh, boy. I want to clean up this code!LINK!https://bitbucket.org/joepal1976/makehuman-api-project/commits/aa5c12953fb2c8a1723b21bb0b7d90667653d615 -- https://bitbucket.org/joepal1976/makehuman-api-project/commits/aa5c12953...!/LINK!* ​Go for it? [RWB]  :)

The Doc_Hell Diagram (green and red arrows that even Glynn couln't understand)
                    [Summary - concentrate on green arrows not red arrows to get the big picture]
* <Doctor_Hell_> this is an example of bad diagram:!LINK!https://www.dropbox.com/s/v3waacufp9pyx1u/mouse_event.png?dl# 0 -- https://www.dropbox.com/s/v3waacufp9pyx1u/mouse_event.png?dl0!/LINK!
* [16:52:48] <Thanasis> well, in your shape, the actual thing is about the green arrows
* [16:53:19] <Thanasis> the red arrows could have been implemented in hundreds of different ways
* [16:53:44] <Thanasis> but the important is their result, the green arrows
* [16:53:53] <Doctor_Hell_> talking about how to draw the objects?
* [16:54:26] <Thanasis> well, my idea was, do two shapes
* [16:54:36] <Thanasis> the first without code
* [16:55:10] <Thanasis> only showing the 5 steps like I explained above, ie, the green arrows
* [16:55:28] <Thanasis> the second can explain each step in detail using the red arrows
* [16:55:50] <Thanasis> but in any case the definition is the following
* [16:56:04] <Thanasis> an event is, you send the name of a method to someone
* [16:56:14] <Doctor_Hell_> ok...but also we have the description written by Manish. I'll show you it tomorrow
* [16:56:21] <Thanasis> and that someone executes that method of theirs
* [16:56:47] <Thanasis> sure, there are many ways to describe it
* [16:57:00] <Doctor_Hell_> I hope we can find the best one
* [16:57:07] <Thanasis> I think that they all match though in some certain key points
* [16:57:52] <Thanasis> if these are filtered out, the explanation may be more simple
And touching on API ideas ...
* [16:59:09] <Doctor_Hell_> since the core is too complex for average python programmers
* [16:59:36] <Thanasis> yes... perhaps the code could be organized in tiers.
* [17:00:00] <Thanasis> core, classes, plugins, scripts
* [17:00:27] <Doctor_Hell_> ah you are talking of the current code, not the simplified api
* [17:00:54] <Doctor_Hell_> yes, it's a good idea..but what group under "core" ?
* [17:01:25] <Thanasis> theapplication and its interfaces(ie.communication with the system and devices. QT, GL etc.)
* [17:01:59] <Thanasis> classes are abstract, they use the application by calling its methods
* [17:02:35] <Thanasis> the application uses the interfaces (QT, GL.these are actually harder than the application andcould be a sepparate tier)
* [17:02:54] <Thanasis> thepluginsuse the classes to create objects
* [17:03:26] <Doctor_Hell_> I see some possible confusion because:
* [17:04:24] <Doctor_Hell_> - not all core modules are into core folder (for example qtui and qtgui are in libs)
* [17:04:49] <Doctor_Hell_> - Classes are everywhere
* [17:05:07] <Thanasis> yes, libs folder consists of both core and classes... indeed
* [17:05:23] <Thanasis> andinterfacestoo
* [17:06:51] <Thanasis> but in general, this separation exists somehow. I'm not sure how, but the past programmers instinctively created it, perhaps for better manageability
* [17:08:14] <Thanasis> ie. Human is a class, Material too, Armature (probably making name wrong again), and to function I observe that they use callbacks of Application
* [17:08:38] <Thanasis> They never use interfaces directly
* [17:09:46] <Thanasis> Even for drawing the human, it is the Application that will give the Human's object3d to OpenGL, not the Human directly
* [17:10:31] <Thanasis> and plugins use classes ie. they use the callbacks that Human, Material etc. have
* [17:11:08] <Doctor_Hell_> Do you mean abstraction classes?
* [17:13:27] <Doctor_Hell_> Thanasis: about  new API:!LINK!http://bugtracker.makehuman.org/issues/534 -- http://bugtracker.makehuman.org/issues/534!/LINK!
* [17:13:42] <Doctor_Hell_> and!LINK!http://bugtracker.makehuman.org/projects/makehuman/wiki/Abstraction_API_for_plugins -- http://bugtracker.makehuman.org/projects/makehuman/wiki/Abstraction_API_...!/LINK!
* [17:13:57] <Doctor_Hell_> Feel free to add wished api calls
 


### Q & A with Glynn Clements
Question: For an event when user clicks on a tab, Tabs class  method tabChanged is called.
  
QTabWidget documentation.There is no such method. 
  Response: 
  
The tabChanged method is defined for qtgui.TabsBase (and overridden for qtgui.Tabs).
  
Both qtgui.Tabs and qtgui.TabBar inherit from qtgui.TabsBase. 
  
Tabs inherits from both TabsBase and QTabWidget  while TabBar inherits from both TabsBase and QTabBar.
  
Both QTabWidget and QTabBar define the currentChanged signal, which is emitted  whenever the current tab changes. 
  
The TabsBase initialiser connects this signal to the tabChanged method (lib/qtgui.py:109):
  
class TabsBase(Widget):
  
def __init__(self):
  
...
  
self.connect(self, QtCore.SIGNAL('currentChanged  int)'), self.tabChanged)
  
### ## # =================================================
Question:   is it true that qtui module: low level module, that handles signals directly from QtCore,  QtGui and QtOpenGL?
  Response:
  
qtui defines the classes for the application (QApplication subclass), main window  QMainWindow subclass), drawing canvas (QGLWidget subclass), and some associated  support classes. In other words, it implements the high-level UI, or at least the aspects which are tied to Qt.
Question:   is it true that  qtgui module: low level module, that define the basic widgets of the GUI as  buttons, radiobuttons, etc..
  Response:
  
Yes; qtgui is essentially a compatibility layer between the Qt widget classes and the legacy MH GUI toolkit. The classes provide methods which more closely mimic the behaviour of original gui3d widgets. Qt events are translated to MH events3d events.
Question:   Is it true that  gui3d module: high level module, that define the principal public classes  of MakeHuman: Application, Category, TaskView and View.
  Response:
  
This is what's left of the legacy MH GUI toolkit. Before the move to Qt, everything was  a "View". Now it's just the high-level containers (Application, Category, Task) which exist as somewhere to put event handlers.
Question: What is the purpose of the module guicommon.py?  Looking at the module name, it appears to be a sort of library for the GUI functions, but it's a completely different thing.  What is it really?
  Response:
  
Object used to be part of gui3d. Its primary function is to be the base class for Human. It's the other main subclass of events3d.EventHandler (the first being gui3d.View).
  
It's not really accurate to call it a "wrapper" around Object3D (although it can have instances of both module3d.Object3D and object3d.Object3D as members).
  
One of the main differences between guicommon.Object and module3d.Object3D is that the latter is a single mesh, while the former has up to four meshes (all of type module3d.Object3D): the base (or "seed") mesh, a proxy mesh, a subdivided mesh, and a subdivided proxy mesh.
  
It [guicommon.py or guicommon.Object ??RWB] also contains an object transformation (location, rotattion, scale) [method?], and optionally a display mesh (object3d.Object3D). As a subclass of EventHandler, it [guicommon.Object ??RWB] provides mouse handlers which propagate the event to the object's view (these are overridden for the Human within MHApplication.loadMainGui).
Question:   G.app is the singular mhmain.MHApplication instance; the callEvent  method (inherited from event3d.EventHandler) will end up calling  G.app.onMouseDownCallback.  How the function callEvent end up calling G.app.onMouseDownCallback?
  Response:
  
"direction" will be either onMouseDownCallback or onMouseUpCallback.  Note the "Callback" suffix.
  
So typical event flow for clicking on the human model is:
  
G.app.mainwin.canvas.mouseUpDownEvent   ("onMouseDownCallback")
  
    [Canvas.mouseUpDownEvent]
  
G.app.callEvent("onMouseDownCallback")                [EventHandler.callEvent]
  
G.app.onMouseDownCallback()                    [gui3d.Application.onMouseDownCallback]
  
G.app.selectedHuman.callEvent('onMouseDown', event)        [EventHandler.callEvent]
  
G.app.selectedHuman.onMouseDown()
  
    [local function in MHApplication.loadMainGui]
  
G.app.currentTask.callEvent("onMouseDown", event)        [EventHandler.callEvent]
  
G.app.currentTask.onMouseDown()                    [View.onMouseDown]
  
G.app.currentCategory.callEvent("onMouseDown", event)        [EventHandler.callEvent]
  
G.app.currentCategory.onMouseDown()    
  
    [View.onMouseDown]
  
G.app.callEvent("onMouseDown", event)                [EventHandler.callEvent]
  
G.app.onMouseDown()                        [MHApplication.onMouseDown]
  
Notes: 
  
    G.app.currentTask.parent #  G.app.currentCategory
  
    G.app.currentCategory.parent #  G.app
Question: is the eventType string (also called 'direction') originated by QT?
  Response:
  
No. "direction" is just so that code which is common to both mouse press and mouse release events can go into a single method (mouseUpDownEvent) rather than duplicating it in mousePressEvent() and mouseReleaseEvent(). Those functions are identical except for the name of the event passed to callEvent.
  
Bear in mind that self.callEvent("onMouseDown", event) is almost the same as self.onMouseDown(event), except that callEvent forces a redraw after the event has been dealt with, and has some support for logging and profiling. Once you strip that away, the guts of callEvent() is just:
  
    method = getattr(self, eventType)
  
    method(event)
  
### ## # =============================================================
  Question: Can the modularization of the code can be improved? 
  Response:
  
Modularisation is already quite good. Too much of it can make the code harder to understand.
  
Currently, we try to avoid importing OpenGL or Qt modules (directly or indirectly) into modules which don't inherently depend upon them (e.g. guicommon.Object imports object3d locally in the attachMesh and detachMesh methods, so it only gets imported if you actually need to render the object).
  
TODO ACTION.  One minor point which I noticed: lib/camera.py imports glmodule solely for the queryDepth() call in convertToWorld2D (the Z coordinate is obtained by retrieving a value from the depth buffer using the X,Y coordinates). This should probably be a local import in that method, so that camera.py could be used in e.g. import/export utilities.
  
### ## # =================================================================
  Question: [Referring to DocHell's red and green diagram (!LINK!https://www.dropbox.com/s/v3waacufp9pyx1u/mouse_event.png?dl# 0] -- https://www.dropbox.com/s/v3waacufp9pyx1u/mouse_event.png?dl0]!/LINK!]
  Response:
  
I have no idea; I can't follow that [diagram]. It would probably help if you simply ignore CallEvent(), and treat object.callEvent('method',event) as just object.method(event).
  
The two factors which make following the flow slightly complicated are:
  
 Methods aren't always defined within the class used to create an object, but may be inherited from one of its base classes.
  
 Event handlers may be dynamically added to an object with the mhEvent method (which is usually invoked using Python's decorator syntax).  This is done for the Human object in MHApplication.loadMainGui():
  
@self.selectedHuman.mhEvent
  
def onMouseDown(event):
  
....
  
If you aren't familiar with the decorator syntax, the above is equivalent to:
  
def onMouseDown(event):
  
        ...
  
self.selectedHuman.mhEvent(onMouseDown)
  
which in turn boils down to:
  
def onMouseDown(event):
  
        ...
  
self.selectedHuman.onMouseDown = onMouseDown
  
### ## # ========================================================================
  Question: Could you provide an explanation of what a weak reference is?  How might this impact MakeHuman?
  Response:
  
[Jonas Hauquier ]  A weak reference, one that is not accounted for by the garbage collection.  Garbage collection removes objects from memory that have no pointers to  them anymore. Weakrefs are not counted among those, so if the object has only weakrefs pointing to it, and not real pointers, it will be removed anyway.   This is to make sure that object A and B that always point to each other, are not kept in memory just because they keep referencing each other (I  believe the garbage collection does not do expensive graph traversals to check what is still referenced by the active context).
  
[Glynn Clements]  Sort of. Python uses both reference-counting (which can't handle circular references) and reachability-based garbage collection (which can). If an object's reference count reaches zero, it will be finalised immediately. But an object with a non-zero reference count can still be finalised if it can be determined that it isn't reachable during a garbage-collection sweep.
  
However: the garbage collector won't attempt to finalise reference cycles if any of the objects in the cycle have a __del__ method, as it can't determine a safe order in which to execute them. Instead, it adds them to a list, accessible as gc.garbage.  Application code can inspect this list, manually finalise the objects (which should break the cycles), then remove them from the list (otherwise their presence in gc.garbage will itself constitute a reference).
  
It's possible to have the garbage collector report such cases using gc.set_debug(gc.DEBUG_UNCOLLECTABLE).
  
Only a few MH classes contain __del__ methods. These will only present a problem if the object itself is part of a cycle (i.e. contains references to "complex" objects which themselves contain references which could lead back to the original object).
  
"Leaf-node" classes such as Texture and Shader shouldn't present a problem unless their creators attach additonal references to them.  This may be an issue for e.g. qtgui.Slider and qtgui.RadioButton, as these have __del__ methods and will naturally create circular references. Use of weakref may be advised here. Similarly for queue.Thread. SceneItem in plugins/7_scene_editor.py may also be a problem.
  
### ## # ====================================================================
  Question: Could you clarify wherther the following acurately describe the use of decorators?
  
A basic decorator is a function that:
  
1) Gets a function "A" as argument
  
 2) Modifies the behavior of "A"
  
 3) Returns a "decorated" version of "A"
Response:  Correct.
Question:  Topic: Decorators and side-effects.  When is a decorator not about generating a function?   So, if the above accurately descibes a decorator, consider the code:
  
@self.selectedHuman.mhEvent
  
def onMouseDown(event):
  
This should translate:
  
onMouseDown = self.selectedHuman.mhEvent(onMouseDown)
  
One would expect that  using mhEvent as decorator, it returns a function, but instead, it returns None:
  
 def mhEvent(self, eventMethod):
  
self.attachEvent(eventMethod.__name__, eventMethod)
  
How can it be used as decorator?
  Response:
  
Because the returned "function" isn't actually used anywhere. The definition is local to loadMainGui(), which doesn't reference the functions, so the fact that e.g. onMouseDown is None within loadMainGui() doesn't matter.  The mhEvent() method is used for its side-effects, not its return value. It attaches an event to the selectedHuman.  It is equivalent to:
  
self.selectedHuman.attachEvent(onMouseDown.__name__, onMouseDown)
  
### ## # =====================================================================