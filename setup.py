##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name='z3c.pdftemplate',
    version='0.2.1dev',
    author="Stephan Richter and the Zope Community",
    author_email="zope-dev@zope.org",
    description="PDF Template",
    long_description=(
        read('README.rst')
        + '\n\n.. contents::\n\n' +
        read('src', 'z3c', 'pdftemplate', 'README.txt')
        + '\n\n' +
        read('CHANGES.txt')
    ),
    license="ZPL 2.1",
    keywords="zope3 pdf rml reportlab template",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope :: 3'],
    url='http://pypi.python.org/pypi/z3c.pdftemplate',
    packages=find_packages('src'),
    include_package_data=True,
    package_dir={'': 'src'},
    namespace_packages=['z3c'],
    extras_require=dict(
        test=[
            'zope.app.testing',
            'zope.principalannotation',
            'zope.copypastemove',
            'zope.app.container',
            'zope.app.folder',
        ],
    ),
    install_requires=[
        'setuptools',
        'z3c.rml',
        'reportlab >= 3.0',
        'zope.app.pagetemplate',
        'zope.app.publisher',
        'zope.component',
        'zope.interface',
        'zope.publisher',
        'zope.schema',
    ],
    zip_safe=False,
)
