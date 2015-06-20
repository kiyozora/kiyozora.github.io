#!/usr/bin/env python

import os

source_files = '*.jemdoc'

conf_files = 'mysite.conf'
cs61b_conf_files = 'cs61b.conf'

compilation_command = 'python jemdoc.py -c {0} {1}'.format(conf_files, source_files)
cs61b_compilation_command = 'python ../jemdoc.py -c {0} {1}'.format(cs61b_conf_files, source_files)

print compilation_command
os.system(compilation_command)

os.chdir('cs61b')

print cs61b_compilation_command
os.system(cs61b_compilation_command)