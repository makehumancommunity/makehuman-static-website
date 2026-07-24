---
title: "Unreal Engine ALS V4"
draft: false
---

# UE4 Advanced Locomotion System 

I finally got the animation retargeting working, still there are problems, but this should bring you a step further. 

### What was the problem#  
Clearly there is a bug in UE4! During the retargeting we have at least tree elements, the animation, the source skeleton and the target skeleton. (Add to this the retargeting manager stuff for each skeleton.)  What happens - at least in theory  - is that some bones are used/referred to in the animation, and for each of these bones UE4 must transfer the parameters 1:1, and the result is complied in the new animation. 

For some reason this went wrong; in some cases UE4 crash due to an array index runs over... and since I know a bit about programming, my guess it that this is a simple case of using the wrong index for the wrong skeleton! In this case it is rather easy to guess that the source skeleton (or perhaps the source animation) have more bones than the target skeleton... likewise, you can guess that things could go OK, if only the target skeleton has more bones than the source! 

### Solution - or rater a crude fix!!# 
Since I was keen on getting on; i simply added some fake virtual bones to the target skeleton! Enough bones so the "source index" would not be higher than the max of the target skeleton area! This is indeed a crude fix, as we can assume that the retargeting process will fail to find any use in those fake virtual bones. 

Fact is that you can now retarget the **Advanced Locomotion System V4**!!

## The next problems= 
There are still some problems! But these are of a more general character.... I tried to retarget one of the PARAGON characters. And as for the Makehuman/Mixamo characters only a subset of the system is working. IK can be made working, somewhat, following some of the steps shown in the tutorials below - but ALS V4 holds a lot of changes and we need a lot more virtual IK bones, a subject I don't enough about yet.... 

Since ALS V4 is a very strong product I hope that there will be a better UE4, and perhaps one of us could make one to share? I will share what I got, as soon as I have made it a bit better. Take a look at the older ALS tutorials for "odd" skeletons: 

{{#ev:youtube|kTrjEeoNi4w}}

{{#ev:youtube|fK1LIqLu1GU}}




## Standard ALS setup, and some very useful tips on changing many meshes!!=

I you are running UE4.23 you may be in "luck" - that is UE4.23 will download ALS V3 and then these tutorials will probably totally work for you!
(However that will then not be useful for you, when you upgrade to >UE4.23, unless you can and want to migrate ALS V3..) 



{{#ev:youtube|SA4xgZiqsLI}}


{{#ev:youtube|4pnN5OnXaSc}}


And this is the link to the secret playlist: [ALSV3 - Working With Other Characters](https://www.youtube.com/playlist?list=PLAR8Kc1ZLLKZjnKI_idX7Ik7mN0VORSm_)

# Simple move to 


## This is the code=
 <nowiki>
Begin Object Class# /Script/BlueprintGraph.K2Node_Event Name"K2Node_Event_0"
   EventReference# (MemberParent=Class'"/Script/AIModule.BTTask_BlueprintBase"',MemberName"ReceiveExecuteAI")
   bOverrideFunction=True
   NodePosX=80
   NodePosY=176
   NodeGuid=5AECDA0D45B70CD6668F66A7DC975CD2
   CustomProperties Pin (PinId# 3C0830D94F34DA7FFC919ABD8D07D819,PinName="OutputDelegate",Direction="EGPD_Output",PinType.PinCategory="delegate",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(MemberParent=Class'"/Script/AIModule.BTTask_BlueprintBase"',MemberName="ReceiveExecuteAI"),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPinFalse,)
   CustomProperties Pin (PinId# 69B84B6B4DD42B047415718632E6DFD3,PinName="then",Direction="EGPD_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,LinkedTo=(K2Node_CallFunction_6 B3E31D744074C0D14FED0C8F8C681276,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPinFalse,)
   CustomProperties Pin (PinId# 124B67D740510AF48431A599D3D958CD,PinName="OwnerController",PinToolTip="Owner Controller\nAIController Object Reference",Direction="EGPD_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject=Class'"/Script/AIModule.AIController"',PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,LinkedTo=(K2Node_CallFunction_6 10A7070A413C34545368BE801B05788B,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPinFalse,)
   CustomProperties Pin (PinId# A3E2D46643D499E91DBF73A5DA0CF087,PinName="ControlledPawn",PinToolTip="Controlled Pawn\nPawn Object Reference",Direction="EGPD_Output",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject=Class'"/Script/Engine.Pawn"',PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,LinkedTo=(K2Node_Knot_0 177328B947C1CEE15ABE90B78D46A073,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPinFalse,)
End Object
Begin Object Class# /Script/BlueprintGraph.K2Node_CallFunction Name"K2Node_CallFunction_0"
   FunctionReference# (MemberName="FinishExecute",bSelfContextTrue)
   NodePosX=1552
   NodePosY=158
   NodeGuid=7F4B9E9A457006867FE18AB2259E3249
   CustomProperties Pin (PinId# 6801586248E6C067280774B134C03A2B,PinName="execute",PinToolTip="\nExec",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,LinkedTo=(K2Node_AIMoveTo_0 5F9FCD2948C55C39017AC4812985F463,K2Node_CallFunction_5 D82E41C74E7EC356EBA0CD90B6C377C7,K2Node_CallFunction_6 502B59E9467A9ACC50D13D97BCA52317,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPinFalse,)
   CustomProperties Pin (PinId# 4BF230B84A974CA60637F78EDA63F129,PinName="then",PinToolTip="\nExec",Direction="EGPD_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPinFalse,)
   CustomProperties Pin (PinId# 4E080BB04C5439D6AF2B17837FAD8BB9,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinToolTip="Target\nBTTask Blueprint Base Object Reference",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject=Class'"/Script/AIModule.BTTask_BlueprintBase"',PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPinFalse,)
   CustomProperties Pin (PinId# 30D99D514AEA9B63F0EEBDB7CC915CBB,PinName="bSuccess",PinToolTip="Success\nBoolean",PinType.PinCategory="bool",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,DefaultValue="true",AutogeneratedDefaultValue="false",PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPinFalse,)
End Object
Begin Object Class# /Script/BlueprintGraph.K2Node_VariableGet Name"K2Node_VariableGet_0"
   VariableReference# (MemberName="vector",MemberGuid=2383D6DF4191BE6B60BDE8BE165E5A19,bSelfContextTrue)
   NodePosX=480
   NodePosY=320
   NodeGuid=7A6ACF594AC784584D7A94BF323664B1
   CustomProperties Pin (PinId# 3CA4A56A4E23C67452B040827EF53D71,PinName="vector",Direction="EGPD_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject=ScriptStruct'"/Script/AIModule.BlackboardKeySelector"',PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,LinkedTo=(K2Node_CallFunction_7 16B663A843E1697ECAEA0480591C4805,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPinFalse,)
   CustomProperties Pin (PinId# D7F06E7E4D16A9C8990450A573FC8565,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject=BlueprintGeneratedClass'"/Game/BSP_StoopidShooter/Blueprints/AI_Controller/StoopidShooter/T_Move2Location.T_Move2Location_C"',PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPinFalse,)
End Object
Begin Object Class# /Script/BlueprintGraph.K2Node_CallFunction Name"K2Node_CallFunction_6"
   FunctionReference# (MemberParent=Class'"/Script/AIModule.AIBlueprintHelperLibrary"',MemberName"SimpleMoveToLocation")
   NodePosX=1104
   NodePosY=176
   NodeGuid=9F83ABE44F9168D607AA39A535A01AF9
   CustomProperties Pin (PinId# B3E31D744074C0D14FED0C8F8C681276,PinName="execute",PinToolTip="\nExec",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,LinkedTo=(K2Node_Event_0 69B84B6B4DD42B047415718632E6DFD3,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPinFalse,)
   CustomProperties Pin (PinId# 502B59E9467A9ACC50D13D97BCA52317,PinName="then",PinToolTip="\nExec",Direction="EGPD_Output",PinType.PinCategory="exec",PinType.PinSubCategory="",PinType.PinSubCategoryObject=None,PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,LinkedTo=(K2Node_CallFunction_0 6801586248E6C067280774B134C03A2B,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPinFalse,)
   CustomProperties Pin (PinId# D797DE824659A113617873B49ED86BC0,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinToolTip="Target\nAIBlueprint Helper Library Object Reference",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject=Class'"/Script/AIModule.AIBlueprintHelperLibrary"',PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,DefaultObject="/Script/AIModule.Default__AIBlueprintHelperLibrary",PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPinFalse,)
   CustomProperties Pin (PinId# 10A7070A413C34545368BE801B05788B,PinName="Controller",PinToolTip="Controller\nController Object Reference",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject=Class'"/Script/Engine.Controller"',PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,LinkedTo=(K2Node_Event_0 124B67D740510AF48431A599D3D958CD,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPinFalse,)
   CustomProperties Pin (PinId# 11255715444928DF42D86C8C5F26D97B,PinName="Goal",PinToolTip="Goal\nVector (by ref)",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject=ScriptStruct'"/Script/CoreUObject.Vector"',PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=True,PinType.bIsConst=True,PinType.bIsWeakPointer=False,DefaultValue="0, 0, 0",AutogeneratedDefaultValue="0, 0, 0",LinkedTo=(K2Node_CallFunction_7 5823F3C04DFCD160BC9B3592A7C44404,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPinFalse,)
End Object
Begin Object Class# /Script/BlueprintGraph.K2Node_CallFunction Name"K2Node_CallFunction_7"
   bIsPureFunc=True
   FunctionReference# (MemberParent=Class'"/Script/AIModule.BTFunctionLibrary"',MemberName"GetBlackboardValueAsVector")
   NodePosX=688
   NodePosY=272
   NodeGuid=389A44084DDEB110E84DE99609723334
   CustomProperties Pin (PinId# B1BB35434625D06F5534108D6262D381,PinName="self",PinFriendlyName=NSLOCTEXT("K2Node", "Target", "Target"),PinToolTip="Target\nBTFunction Library Object Reference",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject=Class'"/Script/AIModule.BTFunctionLibrary"',PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,DefaultObject="/Script/AIModule.Default__BTFunctionLibrary",PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPinFalse,)
   CustomProperties Pin (PinId# 7084B9A5496507597348EF8BFB4F5C1C,PinName="NodeOwner",PinToolTip="Node Owner\nBTNode Object Reference",PinType.PinCategory="object",PinType.PinSubCategory="",PinType.PinSubCategoryObject=Class'"/Script/AIModule.BTNode"',PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,PersistentGuid=00000000000000000000000000000000,bHidden=True,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPinFalse,)
   CustomProperties Pin (PinId# 16B663A843E1697ECAEA0480591C4805,PinName="Key",PinToolTip="Key\nBlackboard Key Selector Structure (by ref)",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject=ScriptStruct'"/Script/AIModule.BlackboardKeySelector"',PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=True,PinType.bIsConst=True,PinType.bIsWeakPointer=False,LinkedTo=(K2Node_VariableGet_0 3CA4A56A4E23C67452B040827EF53D71,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=True,bAdvancedView=False,bOrphanedPinFalse,)
   CustomProperties Pin (PinId# 5823F3C04DFCD160BC9B3592A7C44404,PinName="ReturnValue",PinToolTip="Return Value\nVector\n\nGet Blackboard Value as Vector",Direction="EGPD_Output",PinType.PinCategory="struct",PinType.PinSubCategory="",PinType.PinSubCategoryObject=ScriptStruct'"/Script/CoreUObject.Vector"',PinType.PinSubCategoryMemberReference=(),PinType.PinValueType=(),PinType.ContainerType=None,PinType.bIsReference=False,PinType.bIsConst=False,PinType.bIsWeakPointer=False,DefaultValue="0, 0, 0",AutogeneratedDefaultValue="0, 0, 0",LinkedTo=(K2Node_CallFunction_3 6F171EB04C15797B82BB299A704B1C9E,K2Node_CallFunction_6 11255715444928DF42D86C8C5F26D97B,),PersistentGuid=00000000000000000000000000000000,bHidden=False,bNotConnectable=False,bDefaultValueIsReadOnly=False,bDefaultValueIsIgnored=False,bAdvancedView=False,bOrphanedPinFalse,)
End Object
</nowiki>