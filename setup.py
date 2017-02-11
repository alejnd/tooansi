from setuptools import setup, find_packages

setup(
    name='tooansi',
    version='1.0',
    author ="Alejandro Murciano",
    author_email='alejnd@gmail.com',
    url='https://github.com/alejnd/tooansi',
    long_description=__doc__,
    #py_modules=['server'],
    packages=find_packages(),
    install_requires=['flask','pillow'],
    zip_safe=False,
    entry_points = {'console_scripts': [ 'tooansi = tooansi.run:main' ]},
)
