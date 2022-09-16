---
title: "Vol4 - animation"
draft: false
weight: 20
---

## Adding animation

It is assumed that there are already:

1. _Blender file with animation;_
2. _a scene in Godot derived from this file._

 

### Blender

Opens a previously saved file with the original model and animations.
1. A new animation is imported.
2. The file is saved in the Godot project folder.

_**Note.** In this example, the jump animation is applied in place. In general, it is desirable to move the model in the game engine, as a node, then it will be possible to change the height of the jump. But in this case, I will show a fixed jump. To do this, leave the constraint of the bone fixed on the X-axis only. This change will affect the existing animations, but they are already in the scene file in Godot._

![vol4_01](https://i6.imageban.ru/out/2022/08/14/184bf07a17db8bd4594fbed7343f87b5.jpg)


### Godot

1. From the new file imported into Godot, only a new animation is needed:
 \
 \
 ![vol4_02](https://i4.imageban.ru/out/2022/08/14/6af31c51c6546fdc10c0e80052c9e9d8.jpg)

2. It can be copied or saved for future use:
 \
 \
 ![vol4_03](https://i2.imageban.ru/out/2022/08/14/f14c9c02f586caac32fccd5aa68cfbc5.jpg)

3. Open AnimationPlayer in an existing scene and load the new animation file there by copying or exporting:
 \
 \
 ![vol4_04](https://i5.imageban.ru/out/2022/08/14/7197e8b53e42e31efeeafda51eed5051.jpg)

That's it, the animation is added to the scene file.

\
**A huge grateful thanks to those who have helped and supported me:**
* **punkduck** (MH team)
* [**Raphael**](https://files.mastodon.social/media_attachments/files/106/976/022/172/293/623/original/0ceb03882540b2a7.jpeg)

\
Translated with http://www.DeepL.com/Translator (free version)
