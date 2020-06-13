from flask import Flask, render_template, Response, redirect, url_for, jsonify, request
from camera import VideoCamera
from statistics import mode
import camera
import cv2

app = Flask(__name__, static_url_path='/static/')

video_stream = VideoCamera()


def MostCommon(list):
    try:
        return(mode(list))
    except:
        return '19'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video.html', methods=['GET', 'POST'])
def demo():
    if request.method == 'POST':
        return redirect(url_for('trying'))
    return render_template('video.html')


@app.route('/try.html')
def trying():
    return render_template('try.html', age=MostCommon(camera.AgeList))


def gen(camera):
    camera = VideoCamera()
    count_frames = 0
    while count_frames < 15:
        frame = camera.get_frame()
        count_frames += 1
        yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n'
        yield frame
        yield b'\r\n\r\n'


@app.route('/video_feed')
def video_feed():
    return Response(gen(video_stream),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port="5000")
