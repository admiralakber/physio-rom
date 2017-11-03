import subprocess
import os

def OpenPose(runid, computedir="openpose"):
    pypath = os.getcwd()
    rundir = '{}/runs/{}/'.format(pypath, runid)
    inputvid = rundir+'inputvideo.avi'
    transcodedvid = rundir+'transcodedvideo.avi'
    outputvid = rundir+'outputvideo.avi'

    # transcode
    subprocess.run(["ffmpeg", "-y", "-i", inputvid, transcodedvid])

    # openpose command
    openpose = ["./build/examples/openpose/openpose.bin",
                "--no_display",
                "--video {}".format(transcodedvid),
                "--write_video {}".format(outputvid),
                "--write_images_format \"jpg\"",
                "--write_images {}/{}".format(rundir, "frames"),
                "--write_keypoint_json {}/{}".format(rundir, "json")]

    # Run on compute node Mahasen
    subprocess.run(" ".join(openpose), shell = True, cwd = computedir)

    return

