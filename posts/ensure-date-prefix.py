#!/usr/bin/env python3
"""
Rename blog post files to start with the publishing date (YYYY-MM-DD-...)
"""
import glob
import subprocess

for pat in '*.rst', '*.md':
    for fn in glob.glob(pat):
        with open(fn) as fd:
            for line in fd:
                if line.startswith('.. date:'):
                    parts = line.split(':', 1)
                    date, time = parts[-1].split()
                    date = date.replace('/', '-')
                    if not fn.startswith(date):
                        new_fn = '{}-{}'.format(date, fn)
                        print('Renaming', fn, 'to', new_fn)
                        subprocess.check_call(['git', 'mv', fn, new_fn])
