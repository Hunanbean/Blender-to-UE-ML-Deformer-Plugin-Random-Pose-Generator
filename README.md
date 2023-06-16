# Blender-to-UE-ML-Deformer-Plugin-Random-Pose-Generator
This script will generate random poses for Bone/Joints you specify for use as a base for Unreal Engine Machine Learning Training to fix your Characters Mesh Deformations when Animated.

IMPORTANT: Due to Unreal Engine weirdness, the .FBX and the .ABC CANNOT have the same exact name. model.fbx and model.abc will Not work. model.fbx and modelx.abc will.

Update the Joint dictionary and the Armature Name (currently root), to match your needs. Also, update the joint limits as you see fit.
Epic documentation suggests 20,000 to 50,000 random poses. That will create HUGE files in the end. in the multiple Gigabyte range.
I suggest testing with fewer poses, perhaps 100, before investing those resources.

once Poses are keyframed, export your FBX to go to UE. Also, Export an Alembic of the same(as what you put in the FBX)
Then, follow the Epic/Unreal Documentation found here. https://docs.unrealengine.com/5.1/en-US/how-to-use-the-machine-learning-deformer-in-unreal-engine/

During your testing phase, determine if you should import the Alembic starting at frame 1 or 0. I suggest 1.
Also, when importing your FBX, use the Exported Time as the animation length setting.

Don't forget to tune the joint limits to your skeleton

NOTE!:  There seems to some confusion as to how the ML Deformation Corrective system in UE actually functions.. This script generates the poses required by the MLDeform system to learn from, but you have to actually supply it with a difference in the mesh to learn. For example, Epic built an extremely realistic muscle simulation system that became the Alembic Geometry Cache to train the simpler Skinned SKeletal Mesh that is your charcater. So, short of building a complex muscle simulation system, the fastest way to get results would be to use Blenders built in Corrective Smooth modifier on the your mesh.  So, you would have your Character already in Unreal. you would then use the same Skeletal Mesh in Blender to make a series of poses on. You could enable the Smooth Corrective Modifier on, and be done. you then Export the Animation as both the regular mesh, and as an Alembic Cache. So, when you go back in to UE, you would have the Poses Animation work on your Character Skeletal MEsh. You would also Import the Alembic Geometry Cache that has the Corrective Smooth Modifer corrections already in effect. THe ML Deformer Training would then take your Character Mesh and the Alembic Cache and apply those changes between your Base Character Mesh and the Alembic Cache.
