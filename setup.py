from setuptools import setup, find_packages
import os

setup(
    name='tooansi',
    version='1.0',
    author ="Alejandro Murciano",
    author_email='alejnd@gmail.com',
    url='https://github.com/alejnd/tooansi',
    long_description=__doc__,
    packages=find_packages(),
    py_modules=['run','config','png2ansi'],
    install_requires=['flask','pillow'],
    zip_safe=False,
)