# Copyright 2018 Adam Coldrick
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

from flask_restful import Resource
import yaml


with open('data/tech.yaml') as f:
    techtree = yaml.load(f).get('techs', {})

TECHS = {}
for tech in techtree:
    for name, spec in tech.items():
        TECHS[name] = spec


class TechTree(Resource):
    def get(self):
        return TECHS