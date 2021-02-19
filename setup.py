"""Blaster setup.

The blaster setup module commonly containing Python packaging code.
"""

from setuptools import setup, find_packages

from blaster.metadata import __name__, __version__

setup(
    name=__name__,
    version=__version__,
    description='Blast off a list of tasks concurrently calling each tasks '
                'methods defined',
    url='https://github.com/ryankwilliams/blaster',
    author='Ryan Williams',
    author_email='rwilliams5262@gmail.com',
    license='GPLv3',
    package_dir={'': '.'},
    packages=find_packages('.'),
    python_requires='~=3.6',
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3'
    ]
)
