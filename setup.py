import os
import os.path
from setuptools import setup


def read(fname):
    if os.path.exists(fname):
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    else:
        return ""


setup(
    name="pyad_Trinity",
    version="0.5.16",
    author="Zakir Durumeric",
    author_email="zakird@gmail.com",
    maintainer="Zakir Durumeric",
    maintainer_email="zakird@gmail.com",
    download_url="https://github.com/BradHeff/pyad_Trinity/",
    url="https://github.com/BradHeff/pyad_Trinity/",
    description="An Object-Oriented Active Directory management framework built on ADSI",
    license="Apache License, Version 2.0",
    keywords="python microsoft windows active directory AD adsi",
    packages=["pyad_Trinity"],
    long_description=read("README.rst"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows",
        "Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP",
    ],
    install_requires=[
        "setuptools",
        "future",
    ],
)
