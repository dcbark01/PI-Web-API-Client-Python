# coding: utf-8

"""
	Copyright 2017 OSIsoft, LLC
	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at
	
	  <http://www.apache.org/licenses/LICENSE-2.0>
	
	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.
"""

from __future__ import absolute_import

import io
import json
import requests

# python 2 and python 3 compatibility library
from six import PY3
from six.moves.urllib.parse import urlencode




class RESTResponse(io.IOBase):
    def __init__(self, resp):

        self.urllib3_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = resp.data




class RESTClientObject(object):
    def __init__(self, verifySsl):
        self.auth = None
        self.verifySsl = verifySsl


    def send_request(self, url, method, body, headers=None,query_params=None):

        """
        Makes the HTTP request using RESTClient.
        """
        if query_params:
            url += '?' + urlencode(query_params)

        if method == "GET":
            response = requests.get(url, auth=self.auth, headers=headers, verify=self.verifySsl)
        elif method == "HEAD":
            response = requests.head(url, auth=self.auth, headers=headers, verify=self.verifySsl)
        elif method == "OPTIONS":
            response = requests.options(url, auth=self.auth, headers=headers, verify=self.verifySsl)
        elif method == "POST":
            response = requests.post(url, json=body, auth=self.auth, headers=headers, verify=self.verifySsl)
        elif method == "PUT":
            response = requests.put(url, json=body, auth=self.auth, headers=headers, verify=self.verifySsl)
        elif method == "PATCH":
            response = requests.patch(url, json=body, auth=self.auth, headers=headers, verify=self.verifySsl)
        elif method == "DELETE":
            response = requests.delete(url, auth=self.auth, headers=headers, verify=self.verifySsl)
        else:
            raise ValueError(
                "http method must be `GET`, `HEAD`, `OPTIONS`,"
                " `POST`, `PATCH`, `PUT` or `DELETE`."
            )

        if not 200 <= response.status_code <= 299:
            raise ApiException(http_resp=response)
        return response



class ApiException(Exception):
    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp != None:
            self.status = http_resp.status_code
            self.reason = http_resp.reason
            self.body = http_resp.content.decode('utf-8')
            self.error = json.loads(self.body)
            self.headers = http_resp.headers
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """
        Custom error messages for exception
        """
        error_message = "({0})\n" \
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message
