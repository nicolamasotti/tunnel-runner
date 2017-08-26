from bge import logic
import random

frames = ((0, 40), (40, 80))

def _adjustSpawningPosition(random_reference_block, spawend_in_block):

    if spawend_in_block['direction'] == 'VERTICAL':
        AXIS = 0
    elif spawend_in_block['direction'] == 'HORIZONTAL':
        AXIS = 2

    rand_range = random_reference_block.worldPosition[AXIS]
    rand = random.uniform(-rand_range, rand_range)
    spawend_in_block.worldPosition[AXIS] = rand

def _fireObjects(objects, velocity):
    for object in objects:
        object.setLinearVelocity([0, -velocity, 0])

def _setFrameRange(block):
    frame_range = random.choice(frames)
    action_actuator = block.actuators['Action']
    action_actuator.frameStart = frame_range[0]
    action_actuator.frameEnd = frame_range[1]

def searchScene():
    global spawner
    reference_blocks = []
    spawner = scene.objects ['Spawner']
    for object in scene.objectsInactive:
        if "block" in object:
            reference_blocks.append(object)
        elif "brace" in object:
            reference_brace = object
    return reference_blocks, reference_brace
            
def spawn():
    random_reference_block = random.choice(reference_blocks)
    spawend_in_block = scene.addObject(random_reference_block, spawner)
    _adjustSpawningPosition(random_reference_block, spawend_in_block) #convenience method that randomly udjusts the spawend in block woldposition within the tunnel
    if "type" in spawend_in_block and spawend_in_block['type'] == 'SLIDER':
        _setFrameRange(spawend_in_block)
    spawend_in_brace = scene.addObject(reference_brace, spawner)
    objects_to_fire = (spawend_in_block, spawend_in_brace)
    _fireObjects(objects_to_fire, 60)    

def start(cont):
    global reference_blocks
    global reference_brace
    global scene
    global own

    own = cont.owner

    if "init" not in own:
        scene = logic.getCurrentScene()
        reference_blocks, reference_brace = searchScene() #searrches the scene for the "Spawnwer" object and populates the reference_blocks list
        own['init'] = True
    else: spawn() #spawns in a random block in a random position every time the controller is triggered and sets it's linear velocity
        
