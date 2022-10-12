from google.colab import drive
import sys
import os
import shlex

import launch

commandline_args = os.environ.get('COMMANDLINE_ARGS', "")
args = shlex.split(commandline_args)

if "--dgrive" in args:
    drive.mount('/content/drive')

if "--requirement" in args:
    launch.prepare_enviroment()

if "--run"  in args:
    launch.start_webui()

if "--ngrok" in args:
    get_ipython().system_raw('./ngrok http 7860 -region=jp &')
