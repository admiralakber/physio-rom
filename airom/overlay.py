#import matplotlib as mpl
#mpl.use('Agg')
#import matplotlib.pyplot as plt

import PIL

#from matplotlib.patches import Arc

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import airom.camera
import airom.process

plt.rcParams["figure.figsize"]= (24,16)

def OverlayAngles(runid, joint):
    frames = airom.camera.GetFrameFileNames(runid)
    angles = airom.process.GetAllAngles(runid)

    fig, ax = plt.subplots(1)
    for num, frame in enumerate(frames):
        im = np.array(PIL.Image.open(frame),dtype=np.uint8)
        ax.imshow(im)
        armlength = np.sum(np.abs(angles["v1s"][num]),axis=1)[joint]*2/3
        theta2 = np.rad2deg(np.arctan2(angles["v1s"][num][joint][1], angles["v1s"][num][joint][0]))
        theta1 = np.rad2deg(np.arctan2(angles["v2s"][num][joint][1], angles["v2s"][num][joint][0]))
        ang_center = angles["pose_kps"][num][joint+3][0:2];

        ax.text(ang_center[0],ang_center[1],"%4.1f°" % angles["angles"][num][joint],color='w',fontweight='bold',fontsize=38)
        ax.add_patch(patches.Arc(ang_center, armlength, armlength, theta1=theta1, theta2=theta2, edgecolor='w', lw=8))

        # Hide axis
        plt.axis('off')
        rundir = "runs/{}/overlayed/".format(runid)
        plt.savefig(rundir+"video_%012d_overlayed.jpg" % num)
        plt.cla()

def overlayAngle(data,joint_ind,im_in,im_out):
    # data : output from getAnglesInDir
    # joint_ind : index to joint 
    # im_in : filename to process
    # im_out : file out
    # Load image
    im = np.array(Image.open(im_in), dtype=np.uint8)

    # Create figure and axe
    fig,ax = plt.subplots(1)

    # Display the image
    ax.imshow(im)
    # Get radius of arc
    armLength = np.sum(np.abs(data["v1"][joint_ind]))*2/3
    # Get angles relative to horizontal
    theta2 = np.rad2deg(np.arctan2(data["v1"][joint_ind][1],data["v1"][joint_ind][0]));
    theta1 = np.rad2deg(np.arctan2(data["v2"][joint_ind][1],data["v2"][joint_ind][0]));
    # Write angle label and show arc
    ax.text(A["pose_kp"][jointInd][1][0]-80,A["pose_kp"][jointInd][1][1]-10,"%4.1f°" % A["angles"][0],color='w',fontweight='bold',fontsize=16)
    ax.add_patch(Arc(A["pose_kp"][jointInd][1], armLength, armLength,theta1=theta1, theta2=theta2, edgecolor='r', lw=3))
    # Hide axis
    plt.axis('off')
    plt.savefig(im_out)
