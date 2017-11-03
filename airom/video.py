import subprocess
import os

def OpenPose(runid):
    pypath = os.getcwd()
    rundir = '{}/runs/{}/'.format(pypath, runid)
    inputvid = rundir+'inputvideo.avi'
    transcodedvid = rundir+'transcodedvideo.avi'
    outputvid = rundir+'outputvideo.avi'

    # first transcode
    subprocess.call(['ffmpeg', '-y','-i', inputvid, transcodedvid])
    var = ['./build/examples/openpose/openpose.bin',
                     '--no_display',
                     '--video ' + transcodedvid,
                     '--write_video ' + outputvid,
                     '--write_images ' + rundir + '/frames',
                     '--write_images_format \'jpg\'',
                     '--write_keypoint_json ' + rundir + '/json']
    print(var)
    run = " ".join(var)
    subprocess.run(run, shell=True, cwd="/home/mahasen/lib/openpose")
#    subprocess.call(
                   # ['./build/examples/openpose/openpose.bin',
                   #  '\-\-no_display',
                   #  '\-\-video {}'.format(transcodedvid),
                   #  '\-\-write_video {}'.format(outputvid),
                   #  '\-\-write_images {}/{}'.format(rundir, 'frames'),
                   #  '\-\-write_images_format \'jpg\'',
                   #  '\-\-output {}/{}'.format(rundir,'json')],cwd='/home/mahasen/lib/openpose',shell=True)

