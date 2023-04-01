from platform import system as platform
from setuptools import setup, find_packages

setup(
    name='NativeNotebooks',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'PyDoTheWorld.template': ['*']
    },
    install_requires=[
        'cli-args-system==1.3',
        'PyDoTheWorld @git+https://github.com/OUIsolutions/PyDoTheWorld.git',
        'PySchemaKey @git+https://github.com/OUIsolutions/PySchemaKey',
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'NativeNotebooks=NativeNotebooks.main:main'
        ]
    },

    url='https://github.com/mateusmoutinho/NativeNotebooks',
    license='MIT',

    description=''
)