import utils
# Given an image and a range of motion test this will generate a report.


def testing(data):
    with open("airom/report-templates/template-link.svg") as f:   
        strn = f.read()
    return strn

def elbowJointROM(data):
    with open("airom/report-templates/template-embed.svg") as f:   
        strn = f.read()
    getJointROM_frames(data, 0, 3)
    # calculate range of motion and linspac  set (maxVal, minVal, confVal)
    strn = strn.replace("TemplateTitle", "Elbow Joint Range of Motion")
    strn = strn.replace("MetricLabel1", "Maximum Range of Motion")
    strn = strn.replace("MetricLabel2", "Minimum Range of Motion")
    strn = strn.replace("MetricLabel3", "Confidence")
    strn = strn.replace("Metric1", str(maxVal))
    strn = strn.replace("Metric2", str(minVal))
    strn = strn.replace("Metric3", str(confVal))
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

