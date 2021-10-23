from setuptools import setup
setup(
    name = 'cfscli',
    version = '0.1.0',
    packages = ['cfscli'],
    entry_points = {
        'console_scripts': [
            'cfscli = cfscli.__main__:main'
        ]
    })