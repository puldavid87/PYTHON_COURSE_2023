from setuptools import setup

setup(  
name='Messages',
version='1.0',
description='A test package',
author='Paul D. Rosero',
author_email='paur@itu.dk',
url='https://www.paulrosero-montalvo.com',
packages=['message','message.hello','message.bye'],
scripts=['test.py']
)