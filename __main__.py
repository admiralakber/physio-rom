import matplotlib
matplotlib.use("Agg")

import flask
import werkzeug.utils
import uuid
import os

#import airom.video
#import airom.camera
#import airom.process
#import airom.postprocess
import airom

app = flask.Flask(__name__)

@app.route("/")
def main():
    return flask.render_template('index.html')

# ------------------------------ UPLOADER

@app.route('/upload')
def upload_file():
    return flask.render_template('upload.html')


@app.route('/index.html')
def main_index():
    return flask.render_template('index.html')

@app.route('/js/main.js')
def main_js():
    return flask.render_template('js/main.js')

@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if flask.request.method == 'POST':
        f = flask.request.files['file']
        runid = uuid.uuid1().int
        if not os.path.exists("runs/"+str(runid)):
            os.makedirs("runs/"+str(runid))
            os.makedirs("runs/"+str(runid)+"/json")
            os.makedirs("runs/"+str(runid)+"/frames")
            os.makedirs("runs/"+str(runid)+"/overlayed")
        else:
            return flask.jsonify({"result" : "failed", "reason" : "RUNID Clash, try again soon"})

        f.save('runs/{}/{}'.format(runid, "inputvideo.avi"))

    return flask.jsonify({"result": "success", "runid": str(runid)})

# ------------------------------ COMPUTE

@app.route("/process", methods=['GET'])
def process():
    # I am the stack.
    runid = flask.request.args.get('runid')
    airom.video.OpenPose(runid, computedir = "/ubuntu/physio-rom/openpose")
    return flask.jsonify({"result": "process finished"})

# ------------------------------ VIDEO / IMAGING

@app.route("/airom/getframe", methods=['GET'])
def getframe():
    runid = flask.request.args.get('runid')
    framenum = int(flask.request.args.get('frame'))
    frame = airom.camera.GetFrameRunID(runid, framenum)
    return flask.Response(frame,
                          mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/airom/playvideo', methods=['GET'])
def playvideo():
    runid = flask.request.args.get('runid')
    fps = int(flask.request.args.get('fps'))
    camera = airom.camera.PlayRunID(runid, fps)
    return flask.Response(camera,
                          mimetype='multipart/x-mixed-replace; boundary=frame')


# ------------------------------ COMPUTING ANGLES

@app.route("/airom/getangle", methods=['GET'])
def getangle():
    runid = flask.request.args.get('runid')
    framenum = int(flask.request.args.get('frame'))
    angle = airom.process.GetPoseAngle(runid, framenum)
    return flask.jsonify(airom.romutils.NumpyToList(angle))

# ------------------------------ REPORT GENERATOR

@app.route("/airom/getreport", methods=['GET'])
def getreport():
    runid = flask.request.args.get('runid')
    report = flask.request.args.get('report')
    return flask.Response(airom.postprocess.postproc(airom.process.GetAllAngles(runid), report))

# ------------------------------ OVERLAY

@app.route('/airom/getoverlay', methods=['GET'])
def getoverlay():
    runid = flask.request.args.get('runid')
    joint = int(flask.request.args.get('joint'))
    airom.overlay.OverlayAngles(runid,joint)
    return flask.jsonify({"result": "process finished"})


@app.route('/airom/playoverlay', methods=['GET'])
def playvideo_overlay():
    runid = flask.request.args.get('runid')
    fps = int(flask.request.args.get('fps'))
    camera = airom.camera.PlayRunIDOverlayed(runid, fps)
    return flask.Response(camera,
                          mimetype='multipart/x-mixed-replace; boundary=frame')

# ------------------------------ RUN THE API

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, threaded=True, debug=True)

