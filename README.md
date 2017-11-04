#TITLE: Physio-ROM: Computer vision, AI Range of Motion Reports

## What is Physio ROM

## Installation

This package requires the installation and compilation of the openpose software
suite. This is detailed in the [openpose
documentation](https://github.com/CMU-Perceptual-Computing-Lab/openpose/tree/master/doc). The dependencies for this package are listed in requirements.txt.

Auto-setup is set up via the python virtualenv. Install python virtualenv and run the
following

=make env=
=. env/bin/activate=
=make getreqs=

## Usage

Server Usage
Start the flask server by running:
=python __main__.py=
The server side implementation has, thus far only been tested on unix systems. We
cannot guarantee. Certain linux distros may require running the code in sudo, because 
in-browser web camera streaming only functions in web ports (apparently security reasons)



Further detailed usage information is included in the doc/ folder.

## Third-party dependencies

Third-party dependencies that have been used or modified for this
project that have their own software licence include:

| Software | Copyright | Licence | Link | Use              |
| openpose | -         | LGPL    | -    | Pose detection   |
| caffe    | -         | BSD     | -    | ML framework     |
| numpy    | -         | BSD     | -    | Faster searching |
| flask    | -         | BSD     | -    | web serving      |
|          |           |         |      |                  |

## Copyright and Licence
Copyright (C) 2017 Aqeel Akber and collaborators - All Rights Reserved

You should have received a copy of the [licence][LICENCE] with this file. If not,
please write to: Aqeel Akber <aqeel.akber@gmail.com>. This licence
applies to all files held under the copyright of this project
only and not third-party dependencies.

If you believe that anything in this project infringes your
copyright, please contact us with your information and a detailed
description of your intellectual property, including the specific
place in this project where you believe your intellectual property is
being infringed.

## Contributing ♥

Those interested, see [CONTRIBUTING][CONTRIBUTING.org] for guidelines.
