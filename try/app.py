from flask import Flask, render_template, Response, redirect, url_for, jsonify, request
from camera import VideoCamera
from statistics import mode
import camera
import cv2
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__, static_url_path='/static/')

video_stream = VideoCamera()


def MostCommon(list):
    try:
        return(mode(list))
    except:
        return 'No list'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video.html', methods=['GET', 'POST'])
def demo():
    if request.method == 'POST':
        return redirect(url_for('trying'))
    return render_template('video.html')


@app.route('/try1.html', methods=['POST'])
def trying1():
    return redirect(url_for('plot_png'))


@app.route('/try2.html', methods=['POST'])
def trying2():
    return redirect(url_for('plot_pie'))


@app.route('/try.html', methods=['GET', 'POST'])
def trying():
    return render_template('try.html', age=MostCommon(camera.AgeList), gender=MostCommon(camera.GenderList), emotion=MostCommon(camera.EmotionList))


@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/plotpie.png')
def plot_pie():
    fig = create_pie()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def gen(camera):
    camera = VideoCamera()
    count_frames = 0
    while count_frames < 40:
        frame = camera.get_frame()
        count_frames += 1
        yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n'
        yield frame
        yield b'\r\n\r\n'


def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = ["Neutral", "Happy", "Surprised",
          "Angry", "Sad",  "Disgusted", "Fearful"]
    ys = [camera.EmotionList.count(x) for x in xs]
    axis.bar(xs, ys)
    return fig


def create_pie():
    fig = Figure()
    ax1 = fig.add_subplot()
    emotions = ["Neutral", "Happy", "Surprised",
                "Angry", "Sad",  "Disgusted", "Fearful"]
    xs = [x for x in emotions if camera.EmotionList.count(x) is not None]
    ys = [camera.EmotionList.count(x) for x in xs]
    ax1.pie(ys,  labels=xs, autopct='%1.1f%%', shadow=False, startangle=90)
    ax1.axis('equal')
    return fig


@app.route('/video_feed')
def video_feed():
    return Response(gen(video_stream),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port="5000")
