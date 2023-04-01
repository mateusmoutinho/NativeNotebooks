from platform import system as platform
from setuptools import setup

setup(
    name='NativeNotebooks',
    version='1.0',
    packages=[
        'NativeNotebooks',
        'NativeNotebooks.templates',
    ],
    include_package_data=True,
    package_data={
        'NativeNotebooks.templates': ['*']
    },
    install_requires=[
        'cli-args-system==1.3',
        'PyDoTheWorld @git+https://github.com/OUIsolutions/PyDoTheWorld.git',
        'PySchemaKey @git+https://github.com/OUIsolutions/PySchemaKey',
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'notebook=NativeNotebooks.exec:main'
        ]
    },

    url='https://github.com/mateusmoutinho/NativeNotebooks',
    license='MIT',

    description=''
)