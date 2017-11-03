import subprocess

def ProcessVideo(infile, outdir, options=""):
    subprocess.call(["../openpose/build/examples/openpose/openpose.bin",
                     "--no-display",
                     "--video "+infile, "--output "+outdir])
    
