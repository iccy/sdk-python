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
import six

from openstack import format


class BoolInt(format.Formatter):
    @classmethod
    def deserialize(cls, value):
        """Convert an integer to a boolean"""
        if isinstance(value, bool):
            return value
        if value is None:
            return False
        expr = int(value)
        if 1 == expr:
            return True
        elif 0 == expr:
            return False
        else:
            raise ValueError("Unable to deserialize boolean integer: %s"
                             % value)

    @classmethod
    def serialize(cls, value):
        """Convert a boolean to an integer"""
        if isinstance(value, six.integer_types):
            if int(value) == 0 or int(value) == 1:
                return int(value)
        raise ValueError("Unable to serialize boolean integer: %s"
                         % value)
