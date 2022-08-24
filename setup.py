from setuptools import setup, find_packages

setup(
    name='mutagenMP4',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'mutagen',
    ],
    entry_points='''
    [console_scripts]
    mutagenMP4=mutagenMP4:main
    '''
)
