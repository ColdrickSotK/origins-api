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

from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_restful import Api

from origins.api.v1.tech import TechTree

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(TechTree, '/v1/tech')

@app.route('/images/<path:path>')
def send_image(path):
    return send_from_directory('../images', path)

if __name__ == "__main__":
    app.run(debug=True)