import json
from transforms import FFT_json,convert_json_to_array

def load_json_array_from_file(filename):
    return json.loads(open(filename,'r').read())

def test():
    arr = load_json_array_from_file('data.txt')
    Y = convert_json_to_array(arr,'y')
    print FFT_json(arr)

test()
