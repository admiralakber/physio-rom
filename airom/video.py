import subprocess

def VideoToJSON(infile, outdir, options=""):
    subprocess.call(["../openpose/build/examples/openpose/openpose.bin",
                     "--no-display", "--write_images"+outdir,
                     "--video "+infile, "--output "+outdir])
