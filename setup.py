from setuptools import setup ,find_packages

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='orm_database',
   version='0.1',
   description='This module is written to launch your programs with any database you want in the shortest time ',
   license="MIT",
   long_description=long_description,
   author='SISRSIS',
   author_email='virussisrsis@gmail.com',
   url="https://github.com/sisrsis/orm-database",
   packages=find_packages(),  #same as name
   install_requires=['asyncpg','motor'], #external packages as dependencies

)