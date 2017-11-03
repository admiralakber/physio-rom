# Given an image and a range of motion test this will generate a report.


def testing(folder_img, folder_json):
    with f as open("test-template.svg", "rw"):
        strn = f.read()
    return strn

options = {
        0: testing,
        1: shoulder
        }

def postproc(folder_img, folder_json, romt):
    return options[romt](folder_img, folder_json)

