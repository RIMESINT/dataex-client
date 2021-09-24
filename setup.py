from setuptools import setup

readme_contents = open('README.md', 'r').read()

scripts_list = [
    'scripts/dataex_get_netcdf_subset_ecmwf_ens.py',
    'scripts/dataex_get_netcdf_subset_ecmwf_hres.py',
    'scripts/dataex_insert_obs_data.py',
    'scripts/dataex_get_obs_data.py',
    'scripts/dataex_fetch_obs_summary.py'
]

setup(
    name = "dataex-client",
    version = "0.1.0",
    python_requires = '>=3.6',
    author = 'nzahasan, anubinda',
    author_email = 'nzahasan@gmail.com, grg.jomle@gmail.com',
    packages = ['client', 'client.auth'],
    include_package_data = True,
    url = "https://github.com/nzahasan/dataex-client",
    license = "MIT",
    description = "Dataex-client API for using services by dataex",
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

