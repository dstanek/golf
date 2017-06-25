# Copyright 2017 David Stanek <dstanek@dstanek.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# Code Golfing Solutions for http://exercism.io/exercises/python/run-length-encoding/readme

import itertools as I
import re as R

original = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'
expected = '12WB12W3B24WB'

#
# let's do the encoding
#

# obvious
output = []
for char, group in I.groupby(original):
    l = len(list(group))
    if l > 1:
        output.append(str(l))
    output.append(char)
output = ''.join(output)
assert output == expected

# let's optimize (for code size) the loop
output = []
for char, group in ((c, list(g)) for  c, g in I.groupby(original)):
    l = str(len(group)) if len(group) > 1 else ''
    output.extend([l, char])
output = ''.join(output)
assert output == expected

# let's go a little further
output = []
for char, cnt in ((c, len(list(g))) for  c, g in I.groupby(original)):
    output.append('{:d}{}'.format(cnt, char) if cnt > 1 else char)
output = ''.join(output)
assert output == expected

# wtf - one liner - maybe i miss perl after all?
output = ''.join('{}{}'.format(cnt if cnt > 1 else '' , char) for char, cnt in ((c, len(list(g))) for  c, g in I.groupby(original)))
assert output == expected

# kill me now!
o = ''.join('{:d}{}'.format(n, c) if n > 1 else c for c, n in ((c, len(list(g))) for  c, g in I.groupby(original)))
assert o == expected

#
# let's do the decoding
#

encoded = '12WB12W3B24WB'
expected = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'

output = []
for part in R.findall(r'\d*[A-Za-z]', encoded):
    output.extend(part[-1] * int(part[:-1] or 1))
output = ''.join(output)
assert output == expected

output = []
for char, cnt in ((part[-1], int(part[:-1] or 1)) for part in R.findall(r'\d*[A-Za-z]', encoded)):
    output.append(char * cnt)
output = ''.join(output)
assert output == expected

output = ''.join((char * cnt) for char, cnt in ((part[-1], int(part[:-1] or 1)) for part in R.findall(r'\d*[A-Za-z]', encoded)))
assert output == expected

o = ''.join((c * n) for c, n in ((p[-1], int(p[:-1] or 1)) for p in R.findall(r'\d*[A-Za-z]', encoded)))
assert o == expected
