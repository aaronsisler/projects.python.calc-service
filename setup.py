from setuptools import setup, find_packages

setup(
    name="add-two-integers",
    version="0.1.0",
    packages=find_packages(include=("src"), exclude=("src/local-app")),
    py_modules=["requests"]
)
