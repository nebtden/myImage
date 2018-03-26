# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

# """Functions for downloading and reading MNIST data."""
# from __future__ import absolute_import
# from __future__ import division
# from __future__ import print_function
#
# import gzip
# import os
# import tempfile
#
# import numpy
# from six.moves import urllib
# from six.moves import xrange  # pylint: disable=redefined-builtin
# import tensorflow as tf
# from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets

import struct

# RGB元素范围(0-1)
def hex_to_rgb(hex_str):
    int_tuple = struct.unpack('BBB', bytes.fromhex(hex_str))
    return tuple([val/255 for val in int_tuple])

print(hex_to_rgb('7BF5BE'))


# RGB元素范围(0-255)

# print(hex2rgb('7BF5BE'))


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

rgb = (123, 23, 34)
print(rgb_to_hex(rgb))
