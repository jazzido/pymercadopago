# encoding: utf-8
from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pymercadopago',
      version=version,
      description="Python client for MercadoPago services",
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'requests >=0.13.2'
          ],
      author='Manuel Aristarán',
      author_email='jazzido@jazzido.com',
      url='http://github.com/jazzido/pymercadopago'
      )
