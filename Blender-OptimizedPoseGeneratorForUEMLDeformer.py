import bpy
import random
from math import radians

def set_random_pose(pose_bone, limits):
    pose_bone.rotation_mode = 'XYZ'

    random_rotations = {
        axis: random.uniform(radians(limit[0]), radians(limit[1])) for axis, limit in limits.items()
    }

    pose_bone.rotation_euler = (
        random_rotations['x'],
        random_rotations['y'],
        random_rotations['z'],
    )

def keyframe_pose(joint_name, limits, frame):
    ob = bpy.data.objects['root']
    pose_bone = ob.pose.bones[joint_name]

    for axis in 'xyz':
        pose_bone.keyframe_insert(
            data_path='rotation_euler',
            frame=frame,
            index='xyz'.index(axis),
        )

# Set the number of frames you want to keyframe
num_frames = 100

    # Specify the joints you want to manipulate and their rotation limits (in degrees)
joint_list = {
    'thigh_l': {'x': (-35, 90), 'y': (-40, 45), 'z': (-90, 35)},
    'thigh_r': {'x': (35, -90), 'y': (40, -45), 'z': (-90, 35)},
    'spine_01': {'x': (-25, 25), 'y': (-20, 20), 'z': (-25, 95)},
    'spine_01.5': {'x': (-25, 25), 'y': (-20, 20), 'z': (-25, 25)},
    'spine_02': {'x': (-25, 25), 'y': (-20, 20), 'z': (-25, 25)},
    'spine_03': {'x': (-25, 25), 'y': (20, -20), 'z': (-25, 25)},
    'clavicle_l': {'x': (0, 0), 'y': (15, -45), 'z': (-25, 45)},
    'clavicle_r': {'x': (0, 0), 'y': (45, -15), 'z': (-45, 25)},
    'upperarm_l': {'x': (-60, 165), 'y': (10, -5), 'z': (60, -145)},
    'upperarm_r': {'x': (-165, 60), 'y': (-10, 5), 'z': (-145, 60)},
    'hand_l': {'x': (-40, 60), 'y': (-45, 45), 'z': (-90, 90)},
    'hand_r': {'x': (-60, 40), 'y': (45, -45), 'z': (90,-90)},
    'lowerarm_l': {'x': (-90, 30), 'y': (-30, 15), 'z': (-90, 50)},
    'lowerarm_r': {'x': (-30, 90), 'y': (-15, 30), 'z': (-90, 50)},
    'neck_01': {'x': (-45, 45), 'y': (-65, 65), 'z': (-40, 55)},
    'head': {'x': (-35, 20), 'y': (-55, 55), 'z': (-30, 30)},
    'calf_l': {'x': (30, 0), 'y': (-12, 12), 'z': (-45, 0)},
    'calf_r': {'x': (-30, 0), 'y': (-12, 12), 'z': (-45, 0)},
    'foot_l': {'x': (-45, 45), 'y': (-15, 45), 'z': (-60, 20)},
    'foot_r': {'x': (-45, 45), 'y': (-15, 45), 'z': (-20, 60)},
    'ball_l': {'x': (-60, 20), 'y': (-10, 10), 'z': (-10, 10)},
    'ball_r': {'x': (-60, 20), 'y': (-10, 10), 'z': (-10, 10)},
    }

# Select the armature object and set it as active
ob = bpy.data.objects['root']
bpy.context.view_layer.objects.active = ob

# Keyframe the rest pose at frame 1
bpy.ops.object.mode_set(mode='POSE')
for joint_name in joint_list:
    keyframe_pose(joint_name, joint_list[joint_name], 1)
bpy.ops.object.mode_set(mode='OBJECT')

# Start randomization at frame 2
for frame in range(2, num_frames + 1):
    bpy.ops.object.mode_set(mode='POSE')
    for joint_name, limits in joint_list.items():
        set_random_pose(ob.pose.bones[joint_name], limits)
        keyframe_pose(joint_name, limits, frame)
    bpy.ops.object.mode_set(mode='OBJECT')

print("Keyframed rest pose at frame 1 and random poses for selected joints.")
