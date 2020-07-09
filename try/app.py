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


@app.route('/frame.html')
def frames():
    key = 1
    for emotion in camera.EmotionList:
        camera.EmotionDict[key] = emotion
        key += 1
    return render_template('frame.html', table=camera.EmotionDict, emo=MostCommon(camera.EmotionList))


@app.route('/try.html', methods=['GET', 'POST'])
def trying():
    exact = MostCommon(camera.EmotionList)
    emotions = camera.EmotionList.count(exact)
    try:
    	percentage = float((emotions/len(camera.EmotionList))*100)
    except:
    	percentage = 0		
    return render_template('try.html', age=MostCommon(camera.AgeList), gender=MostCommon(camera.GenderList), emotion=MostCommon(camera.EmotionList), perc=percentage)


@ app.route('/plot_png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@ app.route('/plot_pie')
def plot_pie():
    fig = create_pie()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def gen():
    camera = VideoCamera()
    while True:
        count_frames = 0
        video = cv2.VideoCapture(0)
        while cv2.waitKey(1) < 0 and not None:
            hasFrame, img = video.read()
            if not hasFrame:
                cv2.waitKey()
                break
            frame = camera.get_frame(img)
            count_frames += 1
            yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n'
            yield frame
            yield b'\r\n\r\n'
            if count_frames == 20:
                break
        video.release()
        cv2.destroyAllWindows


def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    camera.EmotionDict[0] = "0"
    key=1
    for emotion in camera.EmotionList:
        camera.EmotionDict[key] = emotion
        key+=1
   # ys = ["0","Neutral", "Happy", "Surprised","Angry", "Sad",  "Disgusted", "Fearful"]
   # xs = []
    #axis.set_title(r'Bar Plot')
    #axis.set_xlabel('Emotions')
    #axis.set_ylabel('Number of Frames')
    #axis.bar(xs, ys)
    axis.bar(camera.EmotionDict.keys(),camera.EmotionDict.values() )
    return fig

    

def create_pie():
    fig = Figure()
    ax1 = fig.add_subplot()
    emotions = ["Neutral", "Happy", "Surprised",
                "Angry", "Sad",  "Disgusted", "Fearful"]
    xs = [x for x in emotions if camera.EmotionList.count(x) is not 0]
    ys = [camera.EmotionList.count(x) for x in xs]
    ax1.pie(ys,  labels=xs, autopct='%1.1f%%', shadow=False, startangle=90)
    ax1.axis('equal')
    return fig


@ app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port="5000")
