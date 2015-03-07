#!/usr/bin/env python

import os

source_files = '*.jemdoc'
conf_files = 'mysite.conf'
compilation_command = 'python jemdoc.py -c {0} {1}'.format(conf_files, source_files)

print compilation_command
os.system(compilation_command)