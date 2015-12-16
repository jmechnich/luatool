from setuptools import setup
from codecs import open
from os import path
from luatool import version

here = path.abspath(path.dirname(__file__))

long_description = ''
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='luatool',
    version=version,
    description='A tool for uploading lua scripts to the ESP8266 with nodemcu firmware.',
    long_description=long_description,
    url='https://github.com/4refr0nt/luatool',
    author='Victor Brutskiy',
    author_email='4refr0nt@gmail.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Embedded Systems',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'pyserial',
    ],
    scripts=[
        'luatool.py',
    ],
)
