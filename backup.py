#!/usr/bin/env python  

from __future__ import print_function
import os
import sys
import shutil
import tarfile
import datetime
from cfgparser import MyConfigParser as mycp
from distutils.dir_util import copy_tree

def get_conf(cfg, section):
    conf = {}
    conf['backup_path'] = cfg.get(section,'backup_path')
    conf['prefix'] = cfg.get(section, 'prefix')
    conf['compress'] = cfg.get(section, 'compress')
    conf['folders'] = cfg.getlist(section, 'backup_folder')
    return conf
    
def copy_dir(from_dir_list , to_dir, filename):
    for dir in from_dir_list:
        dirname = dir.split('/')[-1]
        print("cp %s to %s" % (dir, to_dir))
        today = datetime.date.today().strftime('%Y-%m-%d')
        copy_tree(dir, os.path.join(to_dir, filename, dirname))

def run():
    cfg = mycp()
    cfg.read(os.path.join(os.path.dirname(os.path.abspath(__file__)),'conf.cfg'))
    conf = get_conf(cfg, 'default')
    print(conf)
    today = datetime.date.today().strftime('%Y-%m-%d')
    path = conf['backup_path']
    filename = conf['prefix'] + '_' + today
    copy_dir(conf['folders'], path, filename)

    if conf['compress'] == 'True':
        print('compressing...')
        tar = tarfile.open(os.path.join(path, filename + '.tar.gz'), "w:gz")
        tar.add(os.path.join(path, filename))
        tar.close()
        shutil.rmtree(os.path.join(path, filename), ignore_errors=True)

if __name__ == '__main__':
    run()
