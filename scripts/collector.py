from bge import logic


def collect(cont):
    collision_sensor = cont.sensors['Collision']
    hit_list = collision_sensor.hitObjectList

    for game_object in hit_list:
        game_object.endObject()
