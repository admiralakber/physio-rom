import numpy as np
# Given an image and a range of motion test this will generate a report.

# ------------------------------ UTILITIES

def getJointROM(data, joint_ind):
    # Get extremal values of a given joint_ind
    # data : output from getAnglesInDir
    # joint_ind : index to joint. In order: 'Right elbow','Left elbow','Right Shoulder','Left Shoulder','Right Knee','Left Knee','Right Hip','Left Hip'
    return {'min': np.nanmin(data['angles'][:,joint_ind]),'max':np.nanmax(data['angles'][:,joint_ind])}

def getJointROM_frames(data, joint_ind, num_frames):
    # Tries to get a series of imags which show the ROM of a given joint by selecting rendered frames that are closest to linearly spaced values of the joint angle between its extremal values
    # data : output from getAnglesInDir
    # joint_ind : index to joint 
    # num_frames : number of frames to retrieve showing ROM

    # Get ROM
    rom = getJointROM(data,joint_ind)

    # Get ideal list of linearly spaced angles
    frame_angles_ideal = np.linspace(rom["min"],rom["max"],num=num_frames)

    # Get list of angles closest to ideal and their frame indices
    frame_angles_inds = np.nanargmin(np.abs(np.subtract(frame_angles_ideal.reshape(len(frame_angles_ideal),1),data["angles"][:,joint_ind])),axis=1)
    frame_angles = data["angles"][:,joint_ind][frame_angles_inds]
    frame_angles_sign = data["angles_sign"][:,joint_ind][frame_angles_inds]
    frame_angles_conf = data["confidence"][:,joint_ind][frame_angles_inds]


    return {'angles_ideal':frame_angles_ideal,'angles':frame_angles,
            'angles_frame_inds':frame_angles_inds,'angles_sign':frame_angles_sign,
            'angles_conf':frame_angles_conf}


# ------------------------------ POSTPROCESS
def cleanFloats(x): return str(int(round(x,0)))

def testing(data):
    with open("airom/report-templates/template-link.svg") as f:   
        strn = f.read()
    return strn

def elbowJointROM(data):
    with open("airom/report-templates/elbow-template.svg") as f:   
        strn = f.read()
    processed = getJointROM_frames(data, 0, 3)
    strn = strn.replace("testmin", cleanFloats(180-processed['angles'][0]))
    strn = strn.replace("testmax", cleanFloats(processed['angles'][2]))
    strn = strn.replace("testrom", cleanFloats(processed['angles'][2]-processed['angles'][0]))
    strn = strn.replace("testconf", str(round((processed['angles_conf'][1]+processed['angles_conf'][2])/2.0,2)))
    # embed stages of the motion
    return strn

options = {
        0: testing,
        1: elbowJointROM
        }

options["test"] = testing
options["elbow"] = elbowJointROM

def postproc(data, romt):
    # options = global dictionary
    # romt = report type id
    # options[romt] = function(string, string) -> svg string
    return options[romt](data)

