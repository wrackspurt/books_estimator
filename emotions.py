import text2emotion as te

tex = 'happy'

emotions = te.get_emotion(tex)
if emotions['Angry'] + emotions['Fear'] + emotions['Happy'] + emotions['Sad'] + emotions['Surprise'] == 0.0:
    print('sad')

emotions_dict = {'anger': [], 'fear': [], 'happiness': [], 'sadness': [], 'surprise': []}

emotions_dict['anger'].append(emotions['Angry'])
print(emotions_dict)