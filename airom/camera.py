import time
import cv2
import glob

class Camera(object):
    def __init__(self, runid):
        self.frames = glob.glob("runs/{}/frames/*.jpg".format(runid))
        self.frames = list(map(lambda x: open(x, 'rb').read(), self.frames))
        self.framenumber = 0

    def GetFrame(self):
        try:
            frame = self.frames[self.framenumber]
            self.framenumber += 1
        except: 
            self.framenumber = 0
            frame = self.frames[self.framenumber]
        return frame

def YieldCamera(camera):
    while True:
        frame = camera.GetFrame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def PlayRunID(runid):
    frames = glob.glob("runs/{}/frames/*.jpg".format(runid))
    frames = list(map(lambda x: open(x, 'rb').read(), self.frames))

    while True:
        for frame in frames:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
