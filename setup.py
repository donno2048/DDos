from setuptools import setup,find_packages
setup(
    name='DDos',
    version='1.0.3',
    description='DDos any site',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/donno2048/DDos',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    author='Elisha Hollander',
    install_requires=['fake-useragent'],
    classifiers=['Programming Language :: Python :: 3'],
    entry_points={ 'console_scripts': [ 'ddos=DDos.__main__:main', 'DDos=DDos.__main__:main' ] }
)
