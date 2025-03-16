from setuptools import setup, find_packages

with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='depthfm',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements,
)