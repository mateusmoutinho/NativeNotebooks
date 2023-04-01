from platform import system as platform
from distutils.core import setup, find_packages

setup(
    name='NativeNotebooks',
    version='1.0',
    packages=find_packages(),
    package_data={
        'PyDoTheWorld.template': ['*']
    },
    install_requires=[
        'cli-args-system==1.3',
        'PyDoTheWorld @git+https://github.com/OUIsolutions/PyDoTheWorld.git',
        'PySchemaKey @git+https://github.com/OUIsolutions/PySchemaKey',
        'pyyaml',
    ],

    url='https://github.com/mateusmoutinho/NativeNotebooks',
    license='MIT',

    description=''
)