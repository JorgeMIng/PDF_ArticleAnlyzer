from setuptools import setup, find_packages

setup(
   name='pdf_analyzer',
   version='1.0',
   description='Pdf Analyzer',
   author='Jorge Martin',
   author_email='jorge.martin.izquierdo@alumnos.upm.es',
   packages=find_packages(),  #same as name
   install_requires=[dependency.strip() for dependency in open('requirements.txt').readlines()], #external packages as dependencies
)