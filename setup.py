#-------------------------------------------------------------------------------
# Name:        setup
# Purpose:
#
# Author:      Yavor
#
# Created:
# Copyright:   (c) Yavor
# Licence:     GPLv3
#-------------------------------------------------------------------------------

from distutils.core import setup

setup(name='Snake',
      version='0.2',
      description='Classic Snake game written in Python with default Console UI',
      author='Yavor Papazov',
      author_email='yavorpap@abv.bg',
      packages=['snake', 'snake.tests'],
      test_suite = "tests",
     )
