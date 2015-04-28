import subprocess
import sys
from subprocess import Popen


num_of_args = len(sys.argv)
binary_file = sys.argv[1]

#| awk -F'[:]' '{print $2}' | awk -F'[ ]' '{print $1}' | tr -d '[[:space:]]'

proc = subprocess.Popen(['arm-linux-gnueabi-objdump','-d',binary_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
while True:
  line = proc.stdout.readline()
  if line != '':
    array = line.rstrip().split(':')
    if len(array) > 1:
        if array[1]:
                array2 =  array[1].split(' ')
                array2 = array2[0].lstrip().rstrip()
                if array2:
                        sc_part = '"'
                        sc_part += '\\x'
                        sc_part += '\\x'.join(a+b for a,b in zip(array2[::2], array2[1::2]))
                        sc_part += '"'
                        print sc_part
  else:
    break
