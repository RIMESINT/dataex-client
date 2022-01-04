
VERSION='0.1.0'

BASE_URL                       = 'https://dataex.rimes.int/'
GET_ECMWF_HRES_REGION_DATA_URL = BASE_URL + 'forecast_anls/get_ecmwf_hres_region_data/'
GET_ECMWF_ENS_REGION_DATA_URL  = BASE_URL + 'forecast_anls/get_ecmwf_ens_region_data/'
GET_TOKEN_URL                  = BASE_URL + 'user_auth/get_token/'
CHECK_TOKEN_URL                = BASE_URL + 'user_auth/check_token/'
GET_OBS_DATA_URL               = BASE_URL + 'obs_data/get_obs_data/'
INSERT_OBS_DATA_URL            = BASE_URL + 'obs_data/insert_obs_data/'
GET_COUNTRY_INFO_URL           = BASE_URL + 'obs_data/country_list/'
GET_STATION_INFO_URL           = BASE_URL + 'obs_data/station_list/'
GET_PARAMETER_INFO_URL         = BASE_URL + 'obs_data/parameter_list/'
GET_NETCDF_SUBSET_URL          = BASE_URL + 'forecast_sub/get_netcdf_subset/'
FETCH_OBS_SUMMARY_URL          = BASE_URL + 'obs_data/get_obs_data_summary/'
GET_NETCDF_SUBSET_ENS_URL      = BASE_URL + 'forecast_sub/get_netcdf_subset_ens/'
CHECK_REDUCERS_URL             = BASE_URL + 'forecast_anls/check_reducers/'
GET_USER_ASSETS_URL            = BASE_URL + 'forecast_anls/get_user_fcst_assets/'