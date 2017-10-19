from __future__ import print_function
from collections import deque
import sys

class Tail(object):

  def __init__(self, path, lines=20):
    self.lines = lines
    self.path = path

  def print_lines(self, block_size=1024):

    f = open(self.path)
    f.seek(0,2)
    block_end_byte = f.tell()
    blocks = []
    wanted_lines = self.lines
    lines_to_go = self.lines

    while lines_to_go > 0 and block_end_byte > 0:
      if (block_end_byte - block_size > 0):
        f.seek(block_end_byte - block_size)
        blocks.append(f.read(block_size))

      else:
        f.seek(0)
        blocks.append(f.read(block_size))

      lines_found = blocks[-1].count('\n')
      lines_to_go -= lines_found
      block_end_byte -= block_size

    lines = ''.join(blocks[::-1])
    return '\n'.join(lines.splitlines()[-wanted_lines:])

  def print_lines2(self):
    with open(self.path) as f:
      lines = deque(f, self.lines)
    return lines
  
  
  def blocktail(self, block_size=64):
    tail_length = self.lines
    myiter = 0
    blocks = []
    with open(self.path, mode='r') as fh:
      while len(blocks) < (tail_length + 1):
        # Go 2^block_size from the end of file
        fh.seek((-1 * ((2**myiter) * block_size)), 2)
        #print "Reading {} bytes".format((2**myiter) * block_size)
        blocks = fh.read((2**myiter) * block_size).split('\n')
        myiter += 1
    return blocks[-1 * tail_length::]


def main():
  instance = Tail(sys.argv[1])
  instance2 = Tail(sys.argv[1])
  instance3 = Tail(sys.argv[1])
  print('Method 1')
  print(instance.print_lines())
  print()
  print('Method 2')
  lines = instance2.print_lines2()
  for line in lines:
    print(line, end='')
  print('Method 3')
    lines = instance3.blocktail()
  for line in lines:
    print(line, end='')

if __name__ == '__main__':
  main()
