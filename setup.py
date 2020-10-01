# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in india_tcs_206c_1h/__init__.py
from india_tcs_206c_1h import __version__ as version

setup(
	name='india_tcs_206c_1h',
	version=version,
	description='Implementing TCS - 206C(1H) Introduced by Finance Act, 2020 in India.',
	author='aerele',
	author_email='hello@aerele.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
