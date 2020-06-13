from flask import Flask, render_template, Response, redirect, url_for, jsonify, request
from camera import VideoCamera
import cv2

app = Flask(__name__, static_url_path='/static/')

video_stream = VideoCamera()


@app.route('/')
def index():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('video.html'))
    return render_template('index.html')


@app.route('/video.html')
def demo():
    return render_template('video.html')


def gen(camera):
    camera = VideoCamera()
    count_frames = 0
    while count_frames < 15:
        frame = camera.get_frame()
        count_frames += 1
        yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n'
        yield frame
        yield b'\r\n\r\n'
        # print(camera.AgeList)


@app.route('/video_feed')
def video_feed():
    return Response(gen(video_stream),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port="5000")
