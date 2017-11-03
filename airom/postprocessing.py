import rom-util
# Given an image and a range of motion test this will generate a report.


def testing(data):
    with open("airom/report-templates/template-link.svg") as f:   
        strn = f.read()
    return strn

def shoulder(data):
    with open("airom/report-templates/template-embed.svg") as f:   
        strn = f.read()
    # calculate range of motion and linspace
    # embed stages of the motion
    # find and replace the min max and confidence
    return strn

options = {
        0: testing,
        1: shoulder
        }

def postproc(data, romt):
    # options = global dictionary
    # romt = report type id
    # options[romt] = function(string, string) -> svg string
    return options[romt](data)

