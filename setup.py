from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MOVIE-RECOMMENDER",
    version="0.1",
    author="Mokshagna",
    packages=find_packages(),
    include_package_data=True
)   