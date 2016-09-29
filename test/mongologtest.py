#!/Users/SELO/.virtualenvs/mmt_mk2/bin/python
import os
import sys
import subprocess


# p = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)
p = subprocess.Popen("workon mmt_mk2", stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
print output