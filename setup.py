# coding: utf-8

"""
    42videobricks

    42videobricks is a Video Platform As A Service (VPaaS)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "42videobricks-python-client"
VERSION = "1.1.2"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 1.10.5, < 2",
    "aenum"
]

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name=NAME,
    version=VERSION,
    description="Official Pyhton client library for 42videobricks API",
    author="42videobricks",
    url="http://www.42videobricks.com",
    keywords=["42videobricks", "video", "api", "client", "sdk", "rest"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    # 42videobricks-python-client
    Official Pyhton client library for 42videobricks API.

    42videobricks is a Video Platform As A Service (VPaaS).

    Get documentation in the [Github readme](https://github.com/42videobricks/42videobricks-nodejs-client#readme).
    """,  # noqa: E501
    package_data={"Api42Vb": ["py.typed"]},
)
