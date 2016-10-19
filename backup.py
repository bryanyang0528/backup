#!/usr/bin/env python  

from __future__ import print_function
from subprocess import Popen, PIPE
import os
import gc
import re
import sys
import datetime
from cfgparser import MyConfigParser as mycp


def get_folder(cfg, section, option):
    folders = cfg.getlist(section, option)
    return folders

def get_


def run():
    cfg = mycp()
    cfg.read(os.path.join(os.path.dirname(os.path.abspath(__file__)),'conf.cfg'))
    folders = get_folder(cfg, 'default', 'backup_folder')



if __name__ == '__main__':
    run()
