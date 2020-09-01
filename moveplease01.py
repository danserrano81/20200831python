#!/usr/bin/env python3

import shutil
import os

# Makes this the starting directory
os.chdir('/home/student/mycode/')

# Moves raynor to the ceph_storage dir
shutil.move('raynor.obj', 'ceph_storage/')

# prompts user for new name for file
xname = input('What is the new name for kerrigan.obj? ')

# renames the file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)



