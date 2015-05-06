import sys
import subprocess

command="c:\program files\inkscape\inkscape.com --help"
command=["c:\program files\inkscape\inkscape.exe", "--help"]
try:			
	p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	return_code = p.wait()
	out = p.stdout.read()
	err = p.stderr.read()
	print("Error: "+err)
	print("Output: "+out)
except ImportError:
	print("Something Wrong")
	from popen2 import Popen3
	p = Popen3(cmd, True)
	p.wait()
	rc = p.poll()
	out = p.fromchild.read()
	err = p.childerr.read()