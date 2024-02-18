from setuptools import setup, find_packages

setup(
   name='pdf_analyzer',
   version='1.0',
   description='Pdf Analyzer',
   author='Jorge Martin',
   author_email='jorge.martin.izquierdo@alumnos.upm.es',
   packages=find_packages(),  #same as name
   install_requires=['requirements.txt'], #external packages as dependencies
)