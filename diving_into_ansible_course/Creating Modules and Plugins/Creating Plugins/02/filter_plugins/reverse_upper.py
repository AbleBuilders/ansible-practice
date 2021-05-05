# (c) 2012, Jeroen Hoekx <jeroen@hoekx.be>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import base64
import glob
import hashlib
import json
import ntpath
import os.path
import re
import sys
import time
import uuid
import yaml

import datetime
from functools import partial
from random import Random, SystemRandom, shuffle

from jinja2.filters import environmentfilter, do_groupby as _do_groupby

from ansible.errors import AnsibleError, AnsibleFilterError, AnsibleFilterTypeError
from ansible.module_utils.six import string_types, integer_types, reraise, text_type
from ansible.module_utils.six.moves import shlex_quote
from ansible.module_utils._text import to_bytes, to_native, to_text
from ansible.module_utils.common.collections import is_sequence
from ansible.module_utils.common._collections_compat import Mapping
from ansible.parsing.ajson import AnsibleJSONEncoder
from ansible.parsing.yaml.dumper import AnsibleDumper
from ansible.template import recursive_check_defined
from ansible.utils.display import Display
from ansible.utils.encrypt import passlib_or_crypt
from ansible.utils.hashing import md5s, checksum_s
from ansible.utils.unicode import unicode_wrap
from ansible.utils.vars import merge_hash

display = Display()

UUID_NAMESPACE_ANSIBLE = uuid.UUID('361E6D51-FAEC-444A-9079-341386DA8E2E')

def reverse_upper(string):
        """ Reverse and upper the string. """
        return string[::-1].upper()


class FilterModule(object):
    ''' Ansible core jinja2 filters '''

    def filters(self):
        return {
            'reverse_upper': reverse_upper,
        }
