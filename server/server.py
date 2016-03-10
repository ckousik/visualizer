from flask import Flask
from load_redis import RedisHelper
app = Flask(__name__)

rhelper = RedisHelper()

@app.route('/load/<filename>', methods = ['GET'])
def get_file(filename):
    key = rhelper.load_file(filename)
    if key is None:
        return json.dumps({ "error" : "Could not load file"});
    else:
        return json.dumps({ "key" : key})

app.run()
