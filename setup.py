from setuptools import setup, find_packages

with open('README.txt') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

import os
import imp

mod_path = os.path.abspath('iscompatible.py')
mod = imp.load_source('iscompatible', mod_path)
version = mod.__version__


classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities'
]


setup(
    name='iscompatible',
    version=version,
    description='Python versioning with requirements.txt syntax',
    long_description=readme,
    author='Marcus Ottosson',
    author_email='marcus@abstractfactory.com',
    url='https://github.com/mottosso/iscompatible',
    license=license,
    packages=find_packages(),
    zip_safe=False,
    classifiers=classifiers
)
