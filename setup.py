import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


def readall(*args):
    with open(os.path.join(here, *args), encoding='utf8') as fp:
        return fp.read()


README = readall('README.md')

setup(
    name='srvwrapper',
    version='1.2',
    description='srvwrapper wraps any applications to run as Windows Service',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Gerhard Tan',
    author_email='gerhard.gh.ta@gmail.com',
    url='https://github.com/koho/srvwrapper',
    py_modules=['srvwrapper'],
    entry_points={
        "console_scripts": [
            "srvwrapper=srvwrapper:main",
        ],
    },
    data_files=[('Scripts', ['ServiceWrapper.exe'])],
)
