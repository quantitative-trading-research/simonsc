from os.path import dirname, join

from setuptools import find_packages, setup


def read_file(file):
    with open(file, "rt") as f:
        return f.read()


with open(join(dirname(__file__), 'simonsc/VERSION.txt'), 'rb') as f:
    version = f.read().decode('ascii').strip()
    

setup(
    name='simonsc',
    version=version,
    description='simonsc',
    packages=find_packages(exclude=[]),
    author='quantitative trading research',
    author_email='yujiangallen@126.com',
    license='Apache License v2',
    package_data={'': ['*.*']},
    url='https://github.com/quantitative-trading-research/simonsc',
    install_requires=read_file("requirements.txt").strip(),
    zip_safe=False,
    #entry_points={
    #    'console_scripts': [
    #        'simons-download-data = simonsc.cmd.download:main',
    #    ],
    #},
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
	'Programming Language :: Python :: 3.8',
    ],
)



