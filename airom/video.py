import subprocess

def OpenPose(runid):
    rundir = "runs/{}/".format(runid)
    inputvid = rundir+"inputvideo.avi"
    transcodedvid = rundir+"transcodedvideo.avi"
    outputvid = rundir+"outputvideo.avi"

    # first transcode
    subprocess.call(["ffmpeg", "-i", "-y", inputvid, transcodedvid])

    subprocess.call(["openpose/build/examples/openpose/openpose.bin",
                     "--no-display",
                     "--video " + transcodedvid,
                     "--write_video " + outputvid,
                     "--write_images " + rundir + "/frames",
                     "--write_images_format \"jpg\"",
                     "--output " + rundir + "/json"])

                     

