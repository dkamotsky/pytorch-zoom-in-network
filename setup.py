from setuptools import find_packages, setup

setup(
    name='pytorch-zoom-in-network',
    packages=find_packages(exclude=['tests', 'tests.*']),
    setup_requires=['wheel'],
    version='0.0.1',
    description="Efficient Classification of Very Large Images with Tiny Objects.",
    author='timqqt @ github',
    author_email='dkamotsky@gmail.com'
)
