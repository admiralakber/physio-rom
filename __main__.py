import flask
import airom.postproc
import airom.camera
import cv2

app = flask.Flask(__name__)

@app.route("/")
def main():
    return flask.Response("Welcome... TO AI ROM")

@app.route("/process")
def uploadvideo():
    # need the full stack dev
    pass

@app.route("/airom/getframe", methods=['GET'])
def getframe():
    runid = flask.request.args.get('runid')
    return flask.Response(runid)

@app.route("/airom/getangle", methods=['GET'])
def getangle():
    runid = flask.request.args.get('runid')
    pass

@app.route('/airom/getvideo', methods=['GET'])
def getvideo():
    runid = flask.request.args.get('runid')
    camera = airom.camera.Camera(runid)
    return flask.Response(airom.camera.YieldCamera(camera),
                          mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/airom/playvideo', methods=['GET'])
def getvideo():
    runid = flask.request.args.get('runid')
    camera = airom.camera.PlayRunID(runid)
    return flask.Response(camera,
                          mimetype='multipart/x-mixed-replace; boundary=frame')
    

@app.route("/airom/getreport")
def getreport():
    return flask.Response(airom.postproc.postproc("","", 0))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)

