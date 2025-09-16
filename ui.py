from ursina import *
import init
def uiStart(block, lit_with_shadows_shader):
    global init
    blockIndecater1 = Entity(
        parent=camera.ui,
        model='cube',
        color=color.white,
        position=(-0.2, -0.4),
        scale=(0.2, 0.2, 0.2),
        texture=f'minecraft/model{block-1}.png',
    )

    blockIndecater2 = Entity(
        parent=camera.ui,
        model='cube',
        color=color.white,
        position=(0, -0.4),
        scale=(0.2, 0.2, 0.2),
        texture=f'minecraft/model{block}.png',
    )

    blockIndecater3 = Entity(
        parent=camera.ui,
        model='cube',
        color=color.white,
        position=(0.2, -0.4),
        scale=(0.2, 0.2, 0.2),
        texture=f'minecraft/model{block+1}.png',
    )

    overlay = Entity(
        parent=camera.ui,
        model='cube',
        color=color.white,
        position=(0, -0.4),
        scale=(0.6, 0.2, 0.2),
        texture=f'minecraft/overlay.png',
    )
    arm = Entity(
        parent=camera.ui,
        model='cube',
        color=lerp(color.black, color.light_gray, 0.5),
        position=(0.65, -0.6),
        rotation=(150, -10, 6),
        scale=(0.2, 0.2, 1.5),
        shader=lit_with_shadows_shader
    )
    saveText = Text(
        text=init.saveEnabled,
        parent = camera.ui,
        color=lerp(color.black, color.light_gray, 0.5),
        position=(1, 1)
    )
    return blockIndecater1, blockIndecater2, blockIndecater3, arm, overlay, saveText