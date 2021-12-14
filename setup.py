from setuptools import setup
from dataexclient import __version__

readme_contents = open('README.md', 'r').read()

scripts_list = [ 
    "scripts/dataex_init.py",
    "scripts/dataex_get_obs_data.py",
    "scripts/dataex_list_reducers.py",
    "scripts/dataex_netcdf_subset.py",
    "scripts/dataex_insert_obs_data.py",
    "scripts/dataex_obs_station_list.py",
    "scripts/dataex_list_user_assets.py",
    "scripts/dataex_obs_data_summary.py",
    "scripts/dataex_list_country_info.py",
    "scripts/dataex_obs_parameter_list.py",
    "scripts/dataex_region_data_analysis.py",
]


setup(
    name = "dataex-client",
    version = __version__,
    python_requires = '>=3.6',
    author = 'nzahasan, anubinda',
    author_email = 'nzahasan@gmail.com, grg.jomle@gmail.com',
    packages = ['dataexclient'],
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

