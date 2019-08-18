from setuptools import setup

setup(
    name='Rubik',
    url='https://github.com/josemariasosa/rubik',
    author='Jose Maria Sosa',
    author_email='jose.skedar@gmail.com',
    py_modules=['rubik'],
    install_requires=['pandas'],
    version='2.0',
    license='MIT',
    description='A set of very useful tools for data wrangling and data processing that could be used with the Python library Pandas.',
    long_description=open('README.md').read()
)
