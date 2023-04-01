import bpy
import mathutils
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

def draw_filled_polygon(image, uv_coordinates, color):
    draw = ImageDraw.Draw(image)
    uv_coordinates = [(uv[0] * (image.size[0] - 1), uv[1] * (image.size[1] - 1)) for uv in uv_coordinates]
    draw.polygon(uv_coordinates, fill=color)

mesh_to_mask = bpy.data.objects['Swimsuit']
mesh_to_mask_from = bpy.data.objects['Scrubs']

bvh = mathutils.bvhtree.BVHTree.FromObject(mesh_to_mask_from, bpy.context.evaluated_depsgraph_get())

ray_distance_limit = 3.0
buffer_distance = 1.0
blur_amount = 4
image_size = 1024

image = Image.new('RGBA', (image_size, image_size), (255, 255, 255, 255))

for poly in mesh_to_mask.data.polygons:
    uv_coordinates = []
    for loop_index in poly.loop_indices:
        uv_loop = mesh_to_mask.data.uv_layers.active.data[loop_index]
        uv_coordinates.append(uv_loop.uv)
        face_loop = mesh_to_mask.data.loops[loop_index]
        vertex_index = face_loop.vertex_index
        vertex_position = mesh_to_mask.matrix_world @ mesh_to_mask.data.vertices[vertex_index].co
        face_normal = poly.normal

        hit_positive = bvh.ray_cast(vertex_position, face_normal, ray_distance_limit)
        hit_negative = bvh.ray_cast(vertex_position, -face_normal, ray_distance_limit)

        if hit_positive[0] or hit_negative[0]:
            hit_position = hit_positive[0] if hit_positive[0] else hit_negative[0]
            hit_distance = (hit_position - vertex_position).length
            if hit_distance < buffer_distance:
                color = (0, 0, 0, 255)
            else:
                color = (255, 255, 255, 255)
        else:
            color = (255, 255, 255, 255)

    draw_filled_polygon(image, uv_coordinates, color)

opacity_map = np.array(image).astype(np.float32) / 255.0
opacity_map = Image.fromarray((opacity_map * 255.0).astype(np.uint8))
opacity_map = opacity_map.filter(ImageFilter.GaussianBlur(blur_amount))

opacity_map = np.array(opacity_map).astype(np.float32) / 255.0
lower_threshold = 10 / 255
upper_threshold = 11 / 255

opacity_map[opacity_map <= lower_threshold] = 0.0
opacity_map[opacity_map > upper_threshold] = 1.0
opacity_map = Image.fromarray((opacity_map * 255.0).astype(np.uint8))

opacity_map = opacity_map.transpose(Image.FLIP_TOP_BOTTOM)
opacity_map.save("k://WorkRoom//opacity_map.png")

