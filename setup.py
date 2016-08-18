from setuptools import setup, find_packages
import sys, os

version = '0.2'

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
          'ringo>=0.17.0',
          'ezodf',
          'py3o.renderers.pyuno'
      ],
      entry_points="""
      # -*- Entry points: -*-
      [babel.extractors]
      tableconfig = ringo.lib.i18n:extract_i18n_tableconfig
      formconfig = formbar.i18n:extract_i18n_formconfig
      """,
      message_extractors = {'ringo_evaluation': [
            ('**.py', 'python', None),
            ('templates/**.html', 'mako', None),
            ('templates/**.mako', 'mako', None),
            ('**.xml', 'formconfig', None),
            ('**.json', 'tableconfig', None),
            ('static/**', 'ignore', None)]},
      )
