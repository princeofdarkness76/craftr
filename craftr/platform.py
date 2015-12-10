# Copyright (C) 2015  Niklas Rosenstein
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from craftr import path
import sys

if sys.platform.startswith('linux'):
  std = 'Posix'
  ident = 'linux'
  name = 'Linux'

  obj = lambda x: path.addsuffix(x, '.o')
  bin = lambda x: x
  lib = lambda x: path.addprefix(path.addsuffix(x, '.a'), 'lib')
  dll = lambda x: path.addsuffix(x, '.so')
elif sys.platform.startswith('win32'):
  std = 'NT'
  ident = 'win'
  name = 'Windows'

  obj = lambda x: path.addsuffix(x, '.obj')
  bin = lambda x: path.addsuffix(x, '.exe')
  lib = lambda x: path.addsuffix(x, '.lib')
  dll = lambda x: path.addsuffix(x, '.dll')
elif sys.platform.startswith('cygwin'):
  std = 'Posix'
  ident = 'cygwin'
  name = 'Cygwin'

  obj = lambda x: path.addsuffix(x, '.o')
  bin = lambda x: path.addsuffix(x, '.exe')
  lib = lambda x: path.addprefix(path.addsuffix(x, '.a'), 'lib')
  dll = lambda x: path.addsuffix(x, '.dll')
elif sys.platform.startswith('darwin'):
  std = 'Posix'
  ident = 'mac'
  name = 'Darwin'

  obj = lambda x: path.addsuffix(x, '.o')
  bin = lambda x: x
  lib = lambda x: path.addprefix(path.addsuffix(x, '.a'), 'lib')
  dll = lambda x: path.addsuffix(x, '.dylib')
else:
  error('unsupported platform "{0}"'.format(sys.platform))
