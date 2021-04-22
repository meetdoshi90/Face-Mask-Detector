from app import app, auth
from app.utils import gen
from flask import render_template, Response

# select the camera you want to interface
# if you are using pi camera
# then uncomment the second import
# and comment the first one

# from camera.web_cam import VideoCamera
from camera.pi_cam import VideoCamera

@app.route('/')
@app.route('/normal_camera')
def index():
    return render_template('index.html')


@auth.required
@app.route('/face_mask_detection')
def face_mask():
    return render_template('face_mask.html')


@auth.required
@app.route('/video_feed/<type>')
def video_feed(type):
    return Response(gen(VideoCamera(), type=type),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

