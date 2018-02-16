import numpy as np
import json,glob,os

def LoadPoseJSON(runid):
    posejson = glob.glob("runs/{}/json/*.json".format(runid))
    posejson = sorted(posejson, key = lambda x: int(x.split("/")[-1].split("_")[1]))
    posejson = list(map(lambda x: json.load(open(x)), posejson))
    return posejson

def GetPoseAngle(runid, frame = 0):
    posejson = LoadPoseJSON(runid)
    try:
        return GetFrameAngles(posejson, frame)
    except IndexError:
        return GetFrameAngles(posejson, -1)

def PlayPoseAngles(runid, fps):
    posejson = LoadPoseJSON(runid)
    while True:
        for frame in posejson:
            time.sleep(1.0/fps)
            yield GetAngles(frame)

            
def GetAllAngles(runid):
    # Processes all the JSON files in a directory by calculating angles, etc.
    # Wraps getAngles

    # Get list of files
    #fileList = []
    #for file in os.listdir(dirName):
    #    if file.endswith(".json"):
    #        fileList.append(file)

    # Sort file list
    #fileList = sorted(fileList,key=lambda x: int(x[-27:-15]))

    posejson = LoadPoseJSON(runid)
    
    # Get angles, etc. for all files
    dataList   = [GetFrameAngles(posejson, frame) for frame, i in enumerate(posejson)]

    # Concatenate arrays
    angles = np.array([x["angles"] for x in dataList])
    angles_sign = np.array([x["angles_sign"] for x in dataList])
    confidence = np.array([x["confidence"] for x in dataList])
    v1s = np.array([x["v1"] for x in dataList])
    v2s = np.array([x["v2"] for x in dataList])
    posekps = np.array([x["pose_kp"] for x in dataList])
    
    # Other
    joint_labels = dataList[0]["joint_labels"]
    return {"joint_labels": joint_labels,
            "angles": angles,
            "angles_sign": angles_sign,
            "confidence": confidence,
            "v1s" : v1s,
            "v2s" : v2s,
            "pose_kps" : posekps}

def GetFrameAngles(posejson, frame = 0):
    # Calculates joint angles, confidence intervals, cross-prodcut sign etc.

    # Load JSON
    #with open(fname) as json_data:
    #    data_all = json.load(json_data)

    ## AQEEL -- Now handled by GetPoseAngle

    # Get first person
    data = posejson[frame]['people'][0]

    # Get pose keypoints and reshape
    pose_kp_raw = data['pose_keypoints']
    pose_kp = np.array(pose_kp_raw).reshape([18,3])

    # Define Joints
    joint_labels=['Right elbow','Left elbow','Right Shoulder','Left Shoulder','Right Knee','Left Knee','Right Hip','Left Hip']
    joints  = [[2,3,4],[5,6,7],[3,2,1],[6,5,1],[8,9,10],[11,12,13],[11,8,9],[8,11,12]]

    # Get array of 3x3 arrays of points from pose_kp corresponding to each joint
    pose_kp_joints = np.array([pose_kp[i,0:2] for i in joints])

    # Define confidence in a joint as quadrature of confidence of each body part
    pose_kp_joints_confidence = np.array([np.sqrt(np.mean(np.square(pose_kp[i,2:3]))) for i in joints])

    # Define vectors with origin at joint
    v1 = pose_kp_joints[:,0,:]-pose_kp_joints[:,1,:]
    v2 = pose_kp_joints[:,2,:]-pose_kp_joints[:,1,:]

    # Compute joint angle
    absProb = np.multiply(np.sqrt(np.sum(np.power(v1,2),axis=1)),np.sqrt(np.sum(np.power(v2,2),axis=1)))
    angles  = np.arccos(np.divide(np.sum(np.multiply(v1,v2),axis=1),absProb))*180/np.pi

    # Compute cross product sign
    angles_sign = np.sign(np.subtract(np.multiply(v1[:,0],v2[:,1]),np.multiply(v1[:,1],v2[:,0])))

    return {"frame": frame,
            "joint_labels": joint_labels,
            "angles": angles,
            "angles_sign": angles_sign,
            "confidence": pose_kp_joints_confidence,
            "v1": v1,
            "v2": v2,
            "pose_kp": pose_kp}

