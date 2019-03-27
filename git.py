import getopt
import sys
import os
import re
import time
import subprocess
import datetime
import shutil
import logging

svncmd = "C:\Program Files\Git\cmd\git.exe"
absfile = "./"
svnauth = [111, 222]
svnauth[1] = 222

# def svnlastrev(absfile, svncmd):
# """returns revision before last revision"""
#    logger.info("svn last review: "+absfile)
#    time0 = time.time()
revlist = subprocess.Popen([svncmd, 'log', absfile], shell=True, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE).stdout.read()
revlist1 = subprocess.Popen([svncmd, 'log', absfile], shell=True, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE).stderr.read()
print(str(revlist))
print(str(revlist1))
# revs = re.findall("r\d+\s", str(revlist))
