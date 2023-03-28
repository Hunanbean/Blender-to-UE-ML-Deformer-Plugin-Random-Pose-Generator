import bpy
import random
from math import radians

#Code by Hunanbean and ChatGPT4
#GPL3 applies to the Script itself, NOT to the output

def keyframe_random_pose(joint_name, limits, frame):
    ob = bpy.data.objects['root']
    bpy.context.view_layer.objects.active = ob
    bpy.ops.object.mode_set(mode='POSE')
    pose_bone = ob.pose.bones[joint_name]
    pose_bone.rotation_mode = 'XYZ'

    random_rotations = {
        axis: random.uniform(radians(limit[0]), radians(limit[1])) for axis, limit in limits.items()
    }
    
    pose_bone.rotation_euler = (
        random_rotations['x'],
        random_rotations['y'],
        random_rotations['z'],
    )

    for axis in 'xyz':
        pose_bone.keyframe_insert(
            data_path='rotation_euler',
            frame=frame,
            index='xyz'.index(axis),
        )

    bpy.ops.object.mode_set(mode='OBJECT')

def keyframe_rest_pose(joint_name, frame):
    ob = bpy.data.objects['root']
    bpy.context.view_layer.objects.active = ob
    bpy.ops.object.mode_set(mode='POSE')
    pose_bone = ob.pose.bones[joint_name]
    pose_bone.rotation_mode = 'XYZ'

    for axis in 'xyz':
        pose_bone.keyframe_insert(
            data_path='rotation_euler',
            frame=frame,
            index='xyz'.index(axis),
        )

    bpy.ops.object.mode_set(mode='OBJECT')

# Set the number of frames you want to keyframe
num_frames = 100

# Specify the joints you want to manipulate and their rotation limits (in degrees)
joint_list = {
    'spine_01': {'x': (-25, 25), 'y': (-20, 20), 'z': (-20, 20)},
    'spine_02': {'x': (-25, 25), 'y': (-20, 20), 'z': (-20, 20)},
    'spine_03': {'x': (-25, 25), 'y': (-20, 20), 'z': (-20, 20)},
    'clavicle_l': {'x': (-30, 30), 'y': (-15, 15), 'z': (-45, 45)},
    'upperarm_l': {'x': (-60, 160), 'y': (-80, 80), 'z': (-130, 30)},
    'lowerarm_l': {'x': (-150, 10), 'y': (-20, 20), 'z': (-20, 20)},
    'hand_l': {'x': (-40, 40), 'y': (-40, 40), 'z': (-40, 40)},
    'clavicle_r': {'x': (-30, 30), 'y': (-15, 15), 'z': (-45, 45)},
    'upperarm_r': {'x': (-60, 160), 'y': (-80, 80), 'z': (-30, 130)},
    'lowerarm_r': {'x': (-150, 10), 'y': (-20, 20), 'z': (-20, 20)},
    'hand_r': {'x': (-40, 40), 'y': (-40, 40), 'z': (-40, 40)},
    'neck_01': {'x': (-60, 60), 'y': (-30, 30), 'z': (-30, 30)},
    'head': {'x': (-60, 60), 'y': (-60, 60), 'z': (-60, 60)},
    'thigh_l': {'x': (-45, 45), 'y': (-30, 30), 'z': (-30, 80)},
    'calf_l': {'x': (-150, 0), 'y': (-5, 5), 'z': (-5, 5)},
    'foot_l': {'x': (-45, 45), 'y': (-15, 45), 'z': (-60, 20)},
    'ball_l': {'x': (-60, 20), 'y': (-10, 10), 'z': (-10, 10)},
    'thigh_r': {'x': (-45, 45), 'y': (-30, 30), 'z': (-80, 30)},
    'calf_r': {'x': (-150, 0), 'y': (-5, 5), 'z': (-5, 5)},
    'foot_r': {'x': (-45, 45), 'y': (-15, 45), 'z': (-20, 60)},
    'ball_r': {'x': (-60, 20), 'y': (-10, 10), 'z': (-10, 10)},
}


# Keyframe the rest pose at frame 1
for joint_name in joint_list:
    keyframe_rest_pose(joint_name, 1)

# Start randomization at frame 2
for frame in range(2, num_frames + 1):
    for joint_name, limits in joint_list.items():
        keyframe_random_pose(joint_name, limits, frame)

print("Keyframed rest pose at frame 1 and random poses for selected joints.")