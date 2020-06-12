from flask import Flask, render_template, Response, jsonify
from camera import VideoCamera
import cv2

app = Flask(__name__)

video_stream = VideoCamera()

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    camera = VideoCamera()
    while camera.get_frame() is not None:
        frame = camera.get_frame()
        yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n'
        yield frame
        yield b'\r\n\r\n'
        print(camera.AgeList)
@app.route('/video_feed')
def video_feed():
    return Response(gen(video_stream),
            mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/button/')
def button_clicked():
    print('Hello world!')
    return redirect('/')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True,port="5000")