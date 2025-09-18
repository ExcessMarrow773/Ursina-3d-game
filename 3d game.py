from init import *
app = Ursina(title='Python Game!', vsync=True, editor_ui_enabled=True,  development_mode=True)
window.fullscreen = True

Sky()

block = 3
BLOCK_TEXTURES = [3, 3, 3, 3, 3, 4]
BLOCK_TEXTURES_2 = [4, 4, 4, 4, 4, 5]

light = DirectionalLight()
light.look_at(Vec3(1, -1, 1))
light.color = color.light_gray
light.shadows=True
block_list = []

class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(parent=scene,
                         position=position,
                         model='cube',
                         origin_y=.5,
                         texture=f'minecraft/model{block}.png',
                         color=color.white,
                         highlight_color=color.white,
                         shader=lit_with_shadows_shader
                         )
        data = {"parent": scene,
                "position": position,
                "model": 'cube',
                "origin_y": .5,
                "texture": f'minecraft/model{block}.png',
                "color": color.white,
                "highlight_color": color.white,
                "shader": lit_with_shadows_shader}
        block_list.append(data)


for z in range(15):
    for x in range(15):
        # if random.randrange(50) == 4:
        #     block = 1
        #     for y in range(6, 9):
        #         Voxel(position=(x, y, z))
        block = random.choice(BLOCK_TEXTURES)
        Voxel(position=(x, 5, z))
        block = random.choice(BLOCK_TEXTURES_2)
        Voxel(position=(x, 4, z))
        block = 5
        Voxel(position=(x, 3, z))

uiParts = uiStart(block, lit_with_shadows_shader)
arm = uiParts[3]
blockIndecater1 = uiParts[0]
blockIndecater2 = uiParts[1]
blockIndecater3 = uiParts[2]

def update():
    arm.position = (0.6, -0.5) if held_keys['left mouse'] or held_keys['right mouse'] else (0.75, -0.6)
    blockIndecater1.texture = f'minecraft/model{block-1}.png'
    blockIndecater2.texture = f'minecraft/model{block}.png'
    blockIndecater3.texture = f'minecraft/model{block+1}.png'

player = playerStart()

def input(key):
    global block, block_list
    if held_keys['c'] or key == 'right mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal)

    if key == 'left mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)

    if held_keys['x'] and mouse.hovered_entity:
        destroy(mouse.hovered_entity)
    if key == 'escape':
        quit()

    if held_keys['q'] or key == 'scroll up':
        block = 13 if block == 0 else block - 1
    if held_keys['e'] or key == 'scroll down':
        block = 1 if block == 15 else block + 1


    player.speed = 6 if held_keys['left shift'] else 4.45

    if key == 'middle mouse down' and str(mouse.hovered_entity) == 'voxel':
        block = int(str(mouse.hovered_entity.texture)[5:-4])

    if key == 'r':
        player.x_setter(15 // 2)
        player.y_setter(10)
        player.z_setter(15 // 2)
    if key == 'g':
        f = open("saveFile.txt", "w")
        f.write(str(block_list))
        f.close()


app.run()