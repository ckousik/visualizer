from random import uniform
import json

class Point:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def toJSON(self):
        return json.dump({'x':self.x , 'y': self.y});

    @staticmethod
    def getJSONPoint(x,y):
        return json.dump({'x':x, 'y':y })

    @staticmethod
    def getDict(x,y):
        return {'x':x , 'y':y}

def populateFile(count,min,max,filename):
    points = []
    while count:
        y = uniform(min,max)
        points.append(Point.getDict(count,y))
        count = count - 1
    open(filename,'w').write(str(json.dumps(points)))

#populateFile(10000,20,100,'data.txt')


if __name__ == 'main' :
    populateFile(10000,20,100,'data.txt')
