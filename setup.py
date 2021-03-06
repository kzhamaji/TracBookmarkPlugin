#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2010-2012 Yoshiyuki Sugimoto <s.yosiyuki@gmail.com>
# Copyright (C) 2012-2013 Jun Omae <jun66j5@gmail.com>
# Copyright (C) 2012-2013 Ryan J Ollos <ryan.j.ollos@gmail.com>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from setuptools import setup

extra = {}

try:
    from trac.util.dist  import  get_l10n_cmdclass
    cmdclass = get_l10n_cmdclass()
    if cmdclass:
        extra['cmdclass'] = cmdclass
        extractors = [
            ('**.py',                'python', None),
            ('**/templates/**.html', 'genshi', None),
        ]
        extra['message_extractors'] = {
            'tracbookmark': extractors,
        }
# i18n is implemented to be optional here
except ImportError:
    pass

setup(
    name='TracBookmark',
    version='0.1',
    packages=['tracbookmark'],
    package_data={'tracbookmark' : [
        'templates/*.html', 'htdocs/*.*', 'htdocs/js/*.js', 'htdocs/css/*.css',
        'locale/*/LC_MESSAGES/*.mo',
    ]},
    exclude_package_data={'': ['tests/*']},
    test_suite = 'tracbookmark.tests.suite',
    author='Yoshiyuki Sugimoto',
    maintainer = 'Yoshiyuki Sugimoto',
    maintainer_email = 's.yosiyuki@gmail.com',
    license='BSD 3-clause',
    url='http://trac-hacks.org/wiki/BookmarkPlugin',
    description='A plugin bookmark Trac resources.',
    entry_points = {'trac.plugins': ['tracbookmark = tracbookmark']},
    **extra
    )
