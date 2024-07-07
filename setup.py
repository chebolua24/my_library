from setuptools import setup, find_packages

with open("example_package_me/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='example_package_me',
    version='0.0.1',
    author='Your Name',
    author_email='your.email@example.com',
    description='An example package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[],
)
