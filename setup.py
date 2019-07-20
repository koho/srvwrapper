from setuptools import setup


setup(
    name='srvwrapper',
    version='1.0',
    description='srvwrapper wraps any applications to run as Windows Service',
    author='Gerhard Tan',
    author_email='gerhard.gh.ta@gmail.com',
    url=None,
    py_modules=['srvwrapper'],
    entry_points={
        "console_scripts": [
            "srvwrapper=srvwrapper:main",
        ],
    },
    data_files=[('Scripts', ['ServiceWrapper.exe'])],
)
