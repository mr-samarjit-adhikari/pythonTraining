import os
from flask import Flask

app = Flask(__name__)
#app.add_url_rule('/', 'hello')

@app.route('/')
def hello_world():
    return "<font color=red size=36><b>Hello world</b></font>"

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 5000)))