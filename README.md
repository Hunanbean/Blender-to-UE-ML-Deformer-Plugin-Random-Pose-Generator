# Blender-to-UE-ML-Deformer-Plugin-Random-Pose-Generator
This script will generate random poses for Bone/Joints you specify for use as a base for Unreal Engine Machine Learning Training to fix your Characters Mesh Deformations when Animated.


Update the Joint dictionary and the Armature Name (currently root), to match your needs. Also, update the joint limits as you see fit.
Epic documentation suggests 20,000 to 50,000 random poses. That will create HUGE files in the end. in the multiple Gigabyte range.
I suggest testing with fewer poses, perhaps 100, before investing those resources.

once Poses are keyframed, export your FBX to go to UE. Also, Export an Alembic of the same(as what you put in the FBX)
Then, follow the Epic/Unreal Documentation found here. https://docs.unrealengine.com/5.1/en-US/how-to-use-the-machine-learning-deformer-in-unreal-engine/

During your testing phase, determine if you should import the Alembic starting at frame 1 or 0. I suggest 1.
Also, when importing your FBX, use the Animation Time as the animation length setting.
