from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='ringo_evaluation',
      version=version,
      description="Evaluation extension for the ringo webframework",
      long_description="""The evaluation extension can be used to do
      evaluations on the data of other modules in ringo""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='ringo pyramid extension',
      author='Torsten Irlaender',
      author_email='torsten.irlaender@googlemail.com',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'ringo'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
