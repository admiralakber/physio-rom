import numpy as np
# Given an image and a range of motion test this will generate a report.

# ------------------------------ UTILITIES

def getJointROM(data, joint_ind):
    # Get extremal values of a given joint_ind
    # data : output from getAnglesInDir
    # joint_ind : index to joint. In order: 'Right elbow','Left elbow','Right Shoulder','Left Shoulder','Right Knee','Left Knee','Right Hip','Left Hip'
    return {'min': np.min(data['angles'][:,joint_ind]),'max':np.max(data['angles'][:,joint_ind])}

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
    frame_angles_inds = np.argmin(np.abs(np.subtract(frame_angles_ideal.reshape(len(frame_angles_ideal),1),data["angles"][joint_ind])),axis=1)
    frame_angles = data["angles"][joint_ind][frame_angles_inds]
    frame_angles_sign = data["angles_sign"][joint_ind][frame_angles_inds]
    frame_angles_conf = data["confidence"][joint_ind][frame_angles_inds]


    return {'angles_ideal':frame_angles_ideal,'angles':frame_angles,
            'angles_frame_inds':frame_angles_inds,'angles_sign':frame_angles_sign,
            'angles_conf':frame_angles_conf}


# ------------------------------ POSTPROCESS

def testing(data):
    with open("airom/report-templates/template-link.svg") as f:   
        strn = f.read()
    return strn

def elbowJointROM(data):
    with open("airom/report-templates/template-embed.svg") as f:   
        strn = f.read()
    processed = getJointROM_frames(data, 0, 3)
    strn = strn.replace("TemplateTitle", "Elbow Joint Range of Motion")
    strn = strn.replace("MetricLabel1", "Minimum Range of Motion")
    strn = strn.replace("MetricLabel2", "Maximum Range of Motion")
    strn = strn.replace("MetricLabel3", "Confidence")
    strn = strn.replace("Metric1", str(processed['angles'][0]))
    strn = strn.replace("Metric2", str(processed['angles'][1]))
    strn = strn.replace("Metric3", str(processed['angles'][2]))
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

