# coding: utf-8

import os

import os.path

from setuptools import setup

## Variáveis locais

from src.setup import classifiers
from src.setup import description
from src.setup import license
from src.setup import name
from src.setup import url
from src.setup import version
from src.setup import author
from src.setup import author_email
from src.setup import maintainer
from src.setup import maintainer_email
from src.setup import keywords

## Funções locais

def readme():
	with open('README.rst') as f:
		return f.read()

## Variáveis estáticas

plugins = [
		s for s in os.listdir('plugins') if
			os.path.exists(os.path.join('plugins', s, 'plugin.py'))
	]

protocols = [
		s for s in os.listdir('src/protocols') if
			os.path.exists(os.path.join('src/protocols', s, 'protocol.py'))
	]

dependency_links = []

packages = [
		'paloma',
		'paloma.plugins',
		'paloma.protocols',
	] + \
	['paloma.plugins.'+s for s in plugins] + \
	['paloma.protocols.'+s for s in protocols]

package_dir = {
		'paloma': 'src',
		'paloma.plugins': 'plugins',
		'paloma.protocols': 'src/protocols',
	}

scripts = [
		'bin/test.py',
	]

test_suite = ''

tests_require = ''

install_requires = ''

extras_require = ''

package_data = ''

data_files = ''

entry_points = ''

## Setups
setup(
	author=author,
	author_email=author_email,
	classifiers=classifiers,
	dependency_links=dependency_links,
	description=description,
	include_package_data=True,
	license=license,
	long_description=readme(),
	maintainer=maintainer,
	maintainer_email=maintainer_email,
	name=name,
	packages=packages,
	package_dir=package_dir,
	scripts=scripts,
	test_suite=test_suite,
	tests_require=tests_require,
	url=url,
	version=version,
	zip_safe=False,
	keywords=keywords,
	install_requires=install_requires,
	extras_require=extras_require,
	package_data=package_data,
	data_files=data_files,
	entry_points=entry_points,
)

