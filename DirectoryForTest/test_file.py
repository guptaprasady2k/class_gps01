di = {
    'a': 'Apple',
    'b': 'ball',
    'c': 'cat',
    'd': 'dog',
    'e': 'elephant',
    'f': 'frog',
    'g': 'goat',
    'h': 'hen',
    'i': 'iguana',
    'j': 'jellyfish',
    'k': 'kangaroo',
    'l': 'lion',
    'm': 'monkey',
    'n': 'newt',
    'o': 'otter',
    'p': 'penguin',
    'q': 'quail',
    'r': 'rabbit',
    's': 'snake',
    't': 'turtle',
    'u': 'umbrella',
    'v': 'vulture',
    'w': 'whale',
    'x': 'xylophone',
    'y': 'yak',
    'z': 'zebra'
}


str = 'gupta'

for i in str:
    for k,v in di.items():
        if k==i:
            print(di[i][::-1])
