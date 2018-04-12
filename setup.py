from setuptools import setup, find_packages

from libjtracker import __version__ as version

name = "jtracker"

setup(
    name=name,
    version=version,
    author="Richard Hawkins",
    author_email="hurricanerix@gmail.com",
    description="JTracker",
    license="MIT License",
    keywords="tracker mod json",
    url="http://github.com/hurricanerix/jtracker",
    packages=['libjtracker', 'test'],
    scripts=['bin/jtracker'],
    classifiers=[
        '2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Environment :: Console',
    ],
    install_requires=[],
)
