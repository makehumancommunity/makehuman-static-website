---
title: "Saving models for Unreal Engine and how to import them there/ALS"
draft: false
---

# UE4 Advanced Locomotion System 

I finally got the animation retargeting working, still there are problems, but this should bring you a step further. 

### What was the problem= 
Clearly there is a bug in UE4! During the retargeting we have at least tree elements, the animation, the source skeleton and the target skeleton. (Add to this the retargeting manager stuff for each skeleton.)  What happens - at least in theory  - is that some bones are used/referred to in the animation, and for each of these bones UE4 must transfer the parameters 1:1, and the result is complied in the new animation. 

For some reason this went wrong; in some cases UE4 crash due to an array index runs over... and since I know a bit about programming, my guess it that this is a simple case of using the wrong index for the wrong skeleton! In this case it is rather easy to guess that the source skeleton (or perhaps the source animation) have more bones than the target skeleton... likewise, you can guess that things could go OK, if only the target skeleton has more bones than the source! 

### Solution - or rater a crude fix!!=
Since I was keen on getting on; i simply added some fake virtual bones to the target skeleton! Enough bones so the "source index" would not be higher than the max of the target skeleton area! This is indeed a crude fix, as we can assume that the retargeting process will fail to find any use in those fake virtual bones. 

Fact is that you can now retarget the **Advanced Locomotion System V4**!!

## The next problems= 
There are still some problems! But these are of a more general character.... I tried to retarget one of the PARAGON characters. And as for the Makehuman/Mixamo characters only a subset of the system is working. IK can be made working, somewhat, following some of the steps shown in the tutorials below - but ALS V4 holds a lot of changes and we need a lot more virtual IK bones, a subject I don't enough about yet.... 

Since ALS V4 is a very strong product I hope that there will be a better UE4, and perhaps one of us could make one to share? I will share what I got, as soon as I have made it a bit better. Take a look at the older ALS tutorials for "odd" skeletons: 

{{#ev:youtube|kTrjEeoNi4w}}