import romutil
# Given an image and a range of motion test this will generate a report.


def testing(data):
    with open("airom/report-templates/template-link.svg") as f:   
        strn = f.read()
    return strn

def elbowJointROM(data):
    with open("airom/report-templates/template-embed.svg") as f:   
        strn = f.read()
    (maxVal, minVal, confVal) = (1, 1, 1)
    # calculate range of motion and linspac  set (maxVal, minVal, confVal)
    strn.replace("TemplateTitle", "Elbow Joint Range of Motion")
    strn.replace("metricLabel1", "Maximum Range of Motion")
    strn.replace("metricLabel2", "Minimum Range of Motion")
    strn.replace("metricLabel3", "Confidence")
    strn.replace("metric1", string(maxVal))
    strn.replace("metric2", string(minVal))
    strn.replace("metric3", string(confVal))
    # embed stages of the motion
    return strn

options = {
        0: testing,
        1: elbowJointROM 
        }

def postproc(data, romt):
    # options = global dictionary
    # romt = report type id
    # options[romt] = function(string, string) -> svg string
    return options[romt](data)

