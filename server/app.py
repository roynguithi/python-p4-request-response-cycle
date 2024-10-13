from flask import Flask, request, current_app, g, make_response
import os

app = Flask(__name__)

# Before Request Hook: Setup the app path in 'g' for the lifetime of each request
@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

# View function for the index route
@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    
    # Creating a response body
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''
    
    # Using make_response to structure the response
    return make_response(response_body, 200)

if __name__ == '__main__':
    # Start the application with the specified port and debug mode
    app.run(port=5555, debug=True)
