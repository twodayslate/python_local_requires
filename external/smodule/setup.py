import setuptools
import os


setuptools.setup(
    name="smodule",  # Replace with your own username
    version="1.0.0",
    author="EverWatch",
    author_email="zgorak@everwatchsolutions.com",
    description="An OpenC2 Implementation of POD",
    long_description="A very long description\ngoes here",
    long_description_content_type="text/markdown",
    url="http://10.1.11.45/zrgorak/cerberus-pod-openc2-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)