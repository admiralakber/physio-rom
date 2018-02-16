import subprocess
import os

def OpenPose(runid, computedir="openpose"):
    pypath = os.getcwd()
    rundir = '{}/runs/{}/'.format(pypath, runid)
    inputvid = rundir+'inputvideo.avi'
    transcodedvid = rundir+'transcodedvideo.avi'
    outputvid = rundir+'outputvideo.avi'

    # transcode
    subprocess.run(["ffmpeg", "-y", "-i", inputvid, "-qscale:v", "2","-r", "6", transcodedvid])

    # openpose command
    openpose = ["./build/examples/openpose/openpose.bin",
                "-display=0 ",
                "-number_people_max=1 "
                "--video {}".format(transcodedvid),
                "--write_video {}".format(outputvid),
                "--write_images_format \"jpg\"",
                "--write_images {}/{}".format(rundir, "frames"),
                "--write_keypoint_json {}/{}".format(rundir, "json")]

    # Options for high-precision
    #            "--net_resolution ","1312x736",
    #            "--scale_number ","2",
    #            "--scale_gap", "0.25",

    # Run on compute node Mahasen
    subprocess.run(" ".join(openpose), shell = True, cwd = computedir)

    return

