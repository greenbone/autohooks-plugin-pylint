from io import StringIO, BytesIO, FileIO
import sys

cmd = ['pylint', 'autohooks/plugins/pylint/pylint.py']
import subprocess

# status = subprocess.call(cmd)
iofile = 'tmp.txt'
# status = subprocess.call(cmd, stdout=iofile)
# blah blah lots of code ...

status = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = status.communicate()
print(out.decode(encoding='utf-8'))
print(err.decode(encoding='utf-8'))
