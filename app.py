from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO()

socketio.init_app(app, cors_allowed_origins="*") # allows all origins, not just https

message_storage = []

@socketio.on('connect') #this wrapper is responsible for triggering the following function based on the connect event
def handle_connect():
    print('Client connected')
    
@socketio.on('disconnect') #this wrapper is responsible for triggering the following function based on the disconnect event
def handle_disconnect():
    print('Client disconnected')
    
@socketio.on('message') #this wrapper is responsible for triggering the following function based on the message event
def handle_message(message): #when listening for message event, takes in a message as an argument
    print('Message: ' + message)
    socketio.emit('message', message) #.emit() method broadcasts the message to all connected clients
    message_storage.append(message)
    
@app.route('/')
def home():
    return render_template('base.html')
    

if __name__ == "__main__":
    app.debug = True
    socketio.run(app)