import bpy
import random
import bmesh

# Get the active object and its mesh
obj = bpy.context.active_object
bm = bmesh.from_edit_mesh(obj.data)

# Store the selected vertices in a variable
selected_vertices = [v for v in bm.verts if v.select]

# Define the amount of movement
movement_amount = 0.005

# Move each selected vertex slightly in a random direction
for vertex in selected_vertices:
    vertex.co.x += random.uniform(-movement_amount, movement_amount)
    vertex.co.y += random.uniform(-movement_amount, movement_amount)
    vertex.co.z += random.uniform(-movement_amount, movement_amount)

# Update the object to reflect the changes
bmesh.update_edit_mesh(obj.data)
