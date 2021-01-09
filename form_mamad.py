from os import listdir
from os.path import isfile, join
import json

dir = './single_data_set'
files = [join(dir, f) for f in listdir(dir)
         if isfile(join(dir, f)) and f[-4:].lower() == '.txt']


for i in range(len(files)):
    with open(files[i], 'r') as target:
        data = [int(item) for item in target.read().split('\n')[0:-1]]
        # print(data)
        inputs = data[0:-1]
        target = data[-1]
        with open(join(dir, str(i) + '.json'), 'w') as targetWrite:
            json.dump({'inputs': inputs, 'result': target}, targetWrite)
