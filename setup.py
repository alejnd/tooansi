from setuptools import setup, find_packages

setup(
    name='tooansi',
    version='1.0',
    author ="Alejandro Murciano",
    author_email='alejnd@gmail.com',
    url='https://github.com/alejnd/tooansi',
    long_description=__doc__,
    #packages=['tooansi'],
    #package_dir={'flask': 'flask'},
    packages=find_packages(),
    #include_package_data=True,
    scripts = ["run.py","config.py","setup.py","test_tooansi.py","png2ansi.py"],
    zip_safe=False,
    install_requires=['Flask']
)