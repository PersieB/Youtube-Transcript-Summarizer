from flask import Flask

# define a variable to hold you app
app = Flask(__name__)

# define your resource endpoints
app.route('/')
def index_page():
    return "Hello world"


# server the app when this file is run
if __name__ == '__main__':
    app.run()