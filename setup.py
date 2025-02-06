from setuptools import setup, find_packages

setup(
    name="functogui",
    version="0.0.3",
    author="Beltrán Offerrall",
    packages=find_packages(),
    package_data={
        'functogui': ['*.kv'],
    },
    install_requires=[
        'kivy',
        'pyler',
    ],
)
