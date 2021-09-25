import os
from setuptools import setup
from dataex_client_core.CONFIG import VERSION


base_path = os.path.dirname(os.path.realpath(__file__))

readme_contents = open('README.md', 'r').read()

scripts_list = [ 
                x for x in os.listdir(f'{base_path}/scripts/') \
                if x.startswith('dataex') and x.endswith('.py')
            ]

setup(
    name = "dataex-client",
    version = VERSION,
    python_requires = '>=3.6',
    author = 'nzahasan, anubinda',
    author_email = 'nzahasan@gmail.com, grg.jomle@gmail.com',
    packages = ['dataex_client_core'],
    include_package_data = True,
    url = "https://github.com/nzahasan/dataex-client",
    license = "MIT",
    description = "Dataex API client",
    long_description = readme_contents ,
    scripts =  scripts_list,
    install_requires=[
        "pandas",
        "yaspin",
        "click",
        "openpyxl",
        "requests",
    ]
)

