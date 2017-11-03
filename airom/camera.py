import time
import glob


def LoadFrames(runid):
    frames = glob.glob("runs/{}/frames/*.jpg".format(runid))
    frames = sorted(frames, key = lambda x: int(x.split("/")[-1].split("_")[1]))
    frames = list(map(lambda x: open(x, 'rb').read(), frames))
    return frames

def GetFrameRunID(runid, frame = 0):
    frames = LoadFrames(runid)
    try:
        frame = frames[frame]
    except:
        frame = frames[-1]
        
    yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def PlayRunID(runid, fps):
    frames = LoadFrames(runid)
    while True:
        for frame in frames:
            time.sleep(1.0/fps)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
