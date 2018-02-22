# -*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

tests_require = []

invenio_db_version = '>=1.0.0b8,<1.1.0'

extras_require = {
    # Databases
    'mysql': [
        'invenio-db[mysql]' + invenio_db_version,
        ],
    'postgresql': [
        'invenio-db[postgresql]' + invenio_db_version,
        ],
    # Elasticsearch
    'elasticsearch5': [
        'elasticsearch>=5.0.0,<6.0.0',
        'elasticsearch-dsl>=5.0.0,<6.0.0',
    ],
    'docs': [
        'Sphinx>=1.5.1',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for name, reqs in extras_require.items():
    if name in ('mysql', 'postgresql', 'elasticsearch5'):
        continue
    extras_require['all'].extend(reqs)

setup_requires = []

install_requires = [
    'invenio-app>=1.0.0b1,<1.1.0',
    'invenio-base>=1.0.0a15,<1.1.0',
    'invenio-config>=1.0.0b3,<1.1.0',
    'invenio-jsonschemas>=1.0.0a5,<1.1.0',
    'invenio-records-rest>=1.0.0b1,<1.1.0',
    'invenio-records[mysql]>=1.0.0b2',
    'invenio-rest[cors]>=1.0.0b2',
    'invenio-search>=1.0.0a10,<1.1.0',
    'redis>=2.10.0',
]

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join("cern_search_rest", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

setup(
    name='cern-search-rest',
    version=version,
    description='CERN Search as a Service',
    long_description=readme + '\n\n' + history,
    license='GPLv3',
    author='CERN',
    author_email='cernsearch.support@cern.ch',
    url='http://search.cern.ch/',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'invenio_config.module': [
            'cern_search_rest = cern_search_rest.config',
        ],
        'invenio_search.mappings': [
            'records = cern_search_rest.mappings',
        ],
        'invenio_jsonschemas.schemas': [
            'cern_search_rest_schemas = cern_search_rest.jsonschemas'
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Development Status :: 2 - Pre-Alpha',
    ],
)