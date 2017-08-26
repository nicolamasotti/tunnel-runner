from bge import logic, render
from mathutils import Vector

W = render.getWindowWidth()
H = render.getWindowHeight()
screen_center = Vector((W//2,H//2))

render.showMouse(True)
render.setMousePosition(int(screen_center.x),int(screen_center.y))


def _restrict_movement():

    for i in (0,2):
        if player.worldPosition[i] > limits[i]:
            player.worldPosition[i] = limits[i]
        elif player.worldPosition[i] < -limits[i]:
            player.worldPosition[i] = -limits[i]

def move():
    
    mouse_position = Vector(mouse_sensor.position)
    mouse_offset = mouse_position - screen_center
    mouse_offset.magnitude *= 0.001
    movement = Vector((mouse_offset.x, 0, - mouse_offset.y))
    player.worldPosition += movement

    _restrict_movement()


# Module execution entry point #

def start(cont):
    
    global scene
    global own
    global xLimit
    global yLimit
    global limits
    global mouse_sensor
    global player
    
    own = cont.owner

    if 'init' not in own:
        
        scene = logic.getCurrentScene()
        cont = logic.getCurrentController()
        mouse_sensor = cont.sensors['Mouse']
        player = scene.objects['Player']
        xLimit = scene.objects['xLimit'].worldPosition.x
        yLimit = scene.objects['yLimit'].worldPosition.z
        limits = (xLimit, None, yLimit)
        own['init'] = True
    else: move()
