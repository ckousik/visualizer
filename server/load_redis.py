import redis
import hashlib
from data_files import load_json_array_from_file

class RedisHelper:
    def __init__(self):
        self.r_server = None
        self.keys = []
        try:
            self.r_server = redis.Redis('localhost')
        except Exception as e:
            print e

    def set(self,key,data):
        self.r_server.set(key,data)

    def get(self,key):
        self.r_server.get(key)

    def create_key(self,filename):
        r = hashlib.sha224(filename).hexdigest()
        return r

    def load_file(self,filename):
        key = self.create_key(filename)
        if key in self.keys:
            return key
        else:
            try:
                arr = load_json_array_from_file(filename)
                self.keys.append(key)
                self.set(key,arr)
                return key
            except Exception as e:
                print e
                return None
