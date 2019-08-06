import os

from setuptools import find_packages, setup


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name='aal',
    version='0.0.1',
    packages=find_packages(exclude=["venv"]),
    install_requires=["numpy", "shapely", "matplotlib", "pyqt5",
                      "similaritymeasures"],
    url='https://github.com/nbro/aal',
    license='MIT',
    author='nbro',
    author_email='',
    description='A Python package to convert a sequence of points in the XY '
                'space to another sequence of points in the Angle-Arc-Length '
                '(AAL) space.',
    long_description=read("README.md"),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9"
    ]
)
