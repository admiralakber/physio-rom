import flask
from werkzeug.utils import secure_filename
import airom.postprocess
import airom.camera

app = flask.Flask(__name__)

@app.route("/")
def main():
    return flask.Response("Welcome... TO AI ROM")

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

@app.route("/airom/getframe", methods=['GET'])
def getframe():
    runid = flask.request.args.get('runid')
    framenum = int(flask.request.args.get('frame'))
    frame = airom.camera.GetFrameRunID(runid, framenum)
    return flask.Response(frame,
                          mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/airom/getangle", methods=['GET'])
def getangle():
    runid = flask.request.args.get('runid')
    pass

@app.route('/airom/playvideo', methods=['GET'])
def payvideo():
    runid = flask.request.args.get('runid')
    fps = flask.request.args.get('fps')
    camera = airom.camera.PlayRunID(runid, int(fps))
    return flask.Response(camera,
                          mimetype='multipart/x-mixed-replace; boundary=frame')
    

@app.route("/airom/getreport", methods=['GET'])
def getreport():
    runid = flask.request.args.get('runid')
    report = flask.request.args.get('report')
    return flask.Response(airom.postprocess.postproc("", report))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)

