from platform import system as platform
from setuptools import setup ,find_packages

setup(
    name='NativeNotebooks',
    version='1.0',
    #find and include all packages include not python files
    packages=[
        'NativeNotebooks',
    ],
    include_package_data=True,
    package_data={
        'NativeNotebooks': ['*']
    },
    install_requires=[
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