from flask import Flask


simple_app = Flask(__name__)


@simple_app.route('/')
def index():
    return 'Hello world'


if __name__ == '__main__':
    simple_app.run(host='0.0.0.0')
