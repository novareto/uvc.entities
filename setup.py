# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


def text(path):
    with open(path) as f:
        text = f.read()
    return text

version = '0.3.dev0'
readme = text(os.path.join('src', 'uvc', 'entities', 'README.txt'))
history = text(os.path.join('docs', 'HISTORY.txt'))

install_requires = [
    'cromlech.browser',
    'dolmen.menu',
    'setuptools',
    'zope.interface',
    ]

tests_require = [
    ]

setup(name='uvc.entities',
      version=version,
      description="Uvc Web Framework interfaces definitions.",
      long_description="%s\n\n%s" % (readme, history),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='UVC',
      author='Novareto GmbH',
      author_email='',
      url='http://www.novareto.de',
      license='ZPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['uvc'],
      include_package_data=True,
      zip_safe=False,
      tests_require=tests_require,
      install_requires=install_requires,
      extras_require={'test': tests_require},
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
