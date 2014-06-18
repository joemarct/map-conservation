#!/usr/bin/env python

from distutils.core import setup

setup(name='conservation_mapping',
      version='1.0',
      description='Mapping of residue conservation scores into structure',
      author='Joemar Taganna',
      author_email='joemar.ct@gmail.com',
      url='http://www.joemartaganna.com',
      scripts=['map_conservation.py'],
      data_files=[('src/map-conservation', ['conservation_mapping_script_base.txt'])],
      setup_requires=['score-conservation'],
      dependency_links=[
          'git+https://github.com/joemarct/score-conservation.git'
      ]
     )