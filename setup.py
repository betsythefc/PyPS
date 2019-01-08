#! /usr/bin/env python

from setuptools import setup

setup(
    name="pyps",
    version="0.1",
    description="Powershell cmdlets implemented in Python.",
    url="https://github.com/betsythefc/PyPS",
    author="Bryce McNab",
    author_email="me@brycemcnab.com",
    license="GNU GPL v3",
    packages=["pyps"],
    scripts=[
        "pyps/Get-ChildItem"
    ]
)
