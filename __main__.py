import flask
from werkzeug.utils import secure_filename

import airom.camera
import airom.process
import airom.postprocess

app = flask.Flask(__name__)

@app.route("/")
def main():
    return flask.Response("Welcome... TO AI ROM")

# ------------------------------ UPLOAD / PROCESSOR

@app.route('/upload')
def upload_file():
    return flask.render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if flask.request.method == 'POST':
         f = flask.request.files['file']
         f.save('runs/'+secure_filename(f.filename))
    return "Upload Successful"

@app.route("/process")
def uploadvideo():
    # need the full stack dev
    pass

# ------------------------------ VIDEO / IMAGING

@app.route("/airom/getframe", methods=['GET'])
def getframe():
    runid = int(flask.request.args.get('runid'))
    framenum = int(flask.request.args.get('frame'))
    frame = airom.camera.GetFrameRunID(runid, framenum)
    return flask.Response(frame,
                          mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/airom/playvideo', methods=['GET'])
def payvideo():
    runid = int(flask.request.args.get('runid'))
    fps = int(flask.request.args.get('fps'))
    camera = airom.camera.PlayRunID(runid, fps)
    return flask.Response(camera,
                          mimetype='multipart/x-mixed-replace; boundary=frame')
    

# ------------------------------ COMPUTING ANGLES

@app.route("/airom/getangle", methods=['GET'])
def getangle():
    runid = int(flask.request.args.get('runid'))
    framenum = int(flask.request.args.get('frame'))
    angle = airom.process.GetPoseAngle(runid, framenum)
    return flask.jsonify(angle)
    



# ------------------------------ REPORT GENERATOR


@app.route("/airom/getreport", methods=['GET'])
def getreport():
    runid = flask.request.args.get('runid')
    report = flask.request.args.get('report')
    return flask.Response(airom.postprocess.postproc("", report))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)

