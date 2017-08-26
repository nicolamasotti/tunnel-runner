from bge import logic
import pickle

scores_file_path = logic.expandPath('//scores/scores.txt')


def _saveScoresToFile(scores_file_path, scores):
    scores_file = open(scores_file_path, 'wb')
    pickle.dump(scores, scores_file)
    scores_file.close()


def _loadScoresFromFile(scores_file_path):
    try:
        file = open(scores_file_path, 'rb')
        return pickle.load(file)
    except IOError:
        print('Unable to load scores.txt at "{}":'.format(scores_file_path))
        print('...will create one at game over')
        return []

scores = _loadScoresFromFile(scores_file_path)


def display():
    scene = logic.getCurrentScene() 
    writer = scene.objectsInactive['Writer']
    name = logic.globalDict['Name']
    last_score = logic.globalDict['Score']
    entry = (name, last_score)
    scores.append(entry)

    # we have to sort scores, but scores it's a list of tuples
    scores.sort(key = lambda entry : entry[1], reverse = True)

    last_entry_index = scores.index(entry)

    for entry, i in zip (scores, range(10)):
        spawened_in_writer = scene.addObject(writer, writer)
        spawened_in_writer.localScale = writer.localScale
        spawened_in_writer.worldPosition.y -= 0.5*i
        spawened_in_writer.text = '{:d} - {:s} - {:.3f}'.format(i+1, entry[0], entry[1])
        if i == last_entry_index:
            spawened_in_writer.state = 1

    _saveScoresToFile(scores_file_path, scores)
            
def setName():
    scene = logic.getCurrentScene()
    name = scene.objects['Name']
    logic.globalDict["Name"] = name.text.strip()

def setScore():
    scene = logic.getCurrentScene()
    last_score = scene.objects['Timer']['Text']
    logic.globalDict['Score'] = last_score
