# setup.py

from setuptools import setup, find_packages

setup(
    name="utlib",
    version="0.1.1",
    author="Myroslav Repin",
    author_email="myroslavrepin@gmail.com",
    description="A utility library that contains useful functions, decoraters and more",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MyroslavRepin/utlib",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
