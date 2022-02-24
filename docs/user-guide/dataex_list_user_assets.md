## Get user fcst asset info CLI

This script helps the user to list the user's assets for used in forecast analysis engine.

###Usage
```
$ dataex_get_user_assets.py 
```

The available user assets are shown in tabluar form in the terminal.

###Sample

The following is a sample of the output shown:

|file| identifier | info |
|----------|----------|-------|
| user_asset/some_district_shape.geojson | 78440ef2-1deb-40c0-96b8-9b0953d6absdf4 | {'rec_count': 90, 'unique_fields': ['ADM2_EN', 'ADM2_PCODE']}|
| user_asset/some_District_.json     | c3ac4c6d-ccf4-42fc-8f15-826f51dsaff8 | {'rec_count': 90, 'unique_fields': ['ID_2', 'NAME_2']}|

