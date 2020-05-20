"""An example of graphene subscriptions
"""

from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='example_graphene_subscription',
    version='0.1.0',
    description='An example of graphene subscriptions',
    long_description=long_description,
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/rob-blackbourn/example-graphene-subscription',
    author='Rob Blackbourn',
    author_email='rob.blackbourn@gmail.com',
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='graphene subscription example',
    packages=find_packages(),
    python_requires='>=3.7, <4',
    install_requires=['graphene==3.0b2']
)
