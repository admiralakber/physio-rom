import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
from matplotlib.patches import Arc

def overlayAngle(data,joint_ind,im_in,im_out):
    # data : output from getAnglesInDir
    # joint_ind : index to joint 
    # im_in : filename to process
    # im_out : file out
    # Load image
    im = np.array(Image.open(imname), dtype=np.uint8)

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
