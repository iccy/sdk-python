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

from openstack import resource
from openstack.telemetry import telemetry_service


class Resource(resource.Resource):
    base_path = '/v2/resources'
    service = telemetry_service.TelemetryService()

    # Supported Operations
    allow_retrieve = True
    allow_list = True

    # Properties
    first_sample_at = resource.prop('first_sample_timestamp')
    last_sample_at = resource.prop('last_sample_timestamp')
    links = resource.prop('links')
    metadata = resource.prop('metadata')
    project_id = resource.prop('project_id')
    source = resource.prop('source')
    user_id = resource.prop('user_id')
    _resource_id = resource.prop('resource_id')

    @property
    def id(self):
        try:
            val = self._resource_id
        except AttributeError:
            val = None
        return val

    def __repr__(self):
        return "resource: %s" % (self._attrs)