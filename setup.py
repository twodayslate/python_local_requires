import setuptools
import os

setuptools.setup(
    name="mmodule",
    version="1.0.0",
    author="EverWatch",
    author_email="zgorak@everwatchsolutions.com",
    description="An example of local requires",
    packages=setuptools.find_packages(),
    # https://github.com/pypa/pip/issues/6658#issuecomment-506841157
    install_requires=["smodule@file://localhost{}".format(os.path.dirname(os.path.abspath(__file__)))+"/external/smodule"],
    python_requires=">=3.6",
)