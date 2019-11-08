from setuptools import setup, find_packages
from termcolors import __version__

NAME = 'termcolors'

if __name__ == '__main__':
    setup(
        name=NAME,
        version=__version__,
        packages=find_packages(),
        python_required=">=3.6",
        url="https://github.com/AlexBrin/" + NAME,
        license="MIT",
        author='Alexander Gorenkov',
        author_email='g.a.androidjc2@ya.ru',
        description='Simple and lightweight package for coloring text in the CLI',
        classifiers=[
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "License :: OSI Approved :: MIT License"
        ]
    )
