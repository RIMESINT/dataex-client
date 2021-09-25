import os
from setuptools import setup
from dataex_client_core.CONFIG import VERSION


base_path = os.path.dirname(os.path.realpath(__file__))

readme_contents = open('README.md', 'r').read()

scripts_list = [ 
        'scripts/dataex_fetch_obs_summary.py',             
        'scripts/dataex_get_obs_data.py',
        'scripts/dataex_get_country_info.py',              
        'scripts/dataex_get_station_list.py',
        'scripts/dataex_get_netcdf_subset_ecmwf_ens.py',   
        'scripts/dataex_insert_obs_data.py',
        'scripts/dataex_get_netcdf_subset_ecmwf_hres.py'
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

