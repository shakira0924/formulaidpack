from setuptools import setup, find_packages

setup(
    name="formulaid",
    version="0.1.0",
    description="A package that provides a list of surfactant choices based on the input characteristics provided by the user.",
    author="Shakira Martínez",
    author_email="shakiram@andrew.cmu.edu",
    license="MIT",
    long_description=open("README.md").read(),
    packages=find_packages(where="formulaidpack"),
    package_dir={"": "FORM"},
    package_data={"FORM": ["*.csv"]},
    scripts=[],
)
