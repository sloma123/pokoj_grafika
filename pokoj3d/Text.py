import bpy

# 🔄 Wyczyść scenę
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# 📐 Parametry pokoju
width = 10
depth = 10
height = 6
thickness = 0.2

def create_wall(name, scale, location):
    bpy.ops.mesh.primitive_cube_add(location=location)
    wall = bpy.context.active_object
    wall.name = name
    wall.scale = scale
    bpy.ops.rigidbody.object_add()
    wall.rigid_body.type = 'PASSIVE'
    wall.rigid_body.collision_shape = 'BOX'
    
    wall.game.use_actor = True
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')
    wall.game.use_collision_bounds = True
    return wall

# 🧱 Ściany i podłoga
create_wall("Floor", (width/2, depth/2, thickness/2), (0, 0, 0))
create_wall("Ceiling", (width/2, depth/2, thickness/2), (0, 0, height))
create_wall("Wall_Back",  (width/2, thickness/2, height/2), (0, -depth/2, height/2))
create_wall("Wall_Front", (width/2, thickness/2, height/2), (0,  depth/2, height/2))
create_wall("Wall_Left",  (thickness/2, depth/2, height/2), (-width/2, 0, height/2))
create_wall("Wall_Right", (thickness/2, depth/2, height/2), ( width/2, 0, height/2))

# Światło w środku sufitu
bpy.ops.object.light_add(type='POINT', location=(0, 0, height - 0.2))
bpy.context.object.data.energy = 700


# 🎥 Tylko kamera (jako gracz FPS)
bpy.ops.object.camera_add(location=(1, 1, 1.6))
camera = bpy.context.object
camera.name = "PlayerCamera"
camera.rotation_euler = (0, 0, 0)

bpy.ops.object.select_all(action='DESELECT')
camera.select_set(True)
bpy.context.view_layer.objects.active = camera

## Dodaj fizykę do kamery
camera.game.physics_type = 'DYNAMIC'
camera.game.use_actor = True
camera.game.use_collision_bounds = True
camera.game.collision_bounds_type = 'CAPSULE'

## 🧠 Dodaj Game Component: FirstPersonCamera
#component = camera.components.new('fps_camera')
#component.template = 'FirstPersonCamera'

# 🔧 Ustaw aktywną kamerę i przełącz widok
bpy.context.scene.camera = camera
for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        for space in area.spaces:
            if space.type == 'VIEW_3D':
                space.region_3d.view_perspective = 'CAMERA'
#pliki w pythonie
#tu coś pisze