# Given an image and a range of motion test this will generate a report.


def testing(folder_img, folder_json):
    with open("airom/report-templates/template-link.svg") as f:   #("report-templates/template.svg", "rw"):
        strn = f.read()
    return strn

options = {
        0: testing,
        }

def postproc(folder_img, folder_json, romt):
    # options = global dictionary
    # romt = report type id
    # options[romt] = function(string, string) -> svg string
    return options[romt](folder_img, folder_json)

