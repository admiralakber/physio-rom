import subprocess

def VideoToJSON(infile, runid, options=""):
    subprocess.call(["../openpose/build/examples/openpose/openpose.bin",
                     "--video "+infile, "--no-display",
                     "--write_video runs/{}/video.avi".format(runid),
                     "--write_images runs/{}/frames/".format(runid),
                     "--output runs/{}/json/".format(runid)])

