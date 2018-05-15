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

from setuptools import setup, find_packages

NAME = "osisoft.pidevclub.piwebapi"
VERSION = "1.1.4"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["six >= 1.10", "requests", "requests-kerberos", "pandas>=0.20.3", "setuptools >= 21.0.0"]

setup(
    name=NAME,
    version=VERSION,
    description="PI Web API client library for Python (2017 R2)",
    url="https://github.com/osimloeff/PI-Web-API-Client-Python",
    keywords=["PI Web API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    author='Marcos Vainer Loeff',
    author_email='mloeff@osisoft.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable'
    ],
    long_description="""\
    PI Web API client library for Python (2017 R2)
    """
)
