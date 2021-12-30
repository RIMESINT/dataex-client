
DataEx users can upload their own shape files and use the forecast analysis engine to perform analysis using the shapefile. Below, we explain how you can upload your shapefile. 

### User assets
Go to DataEx home page then click on user profile tab to get a drop down menu and select profile view. This will take you to your user profile page where you can see your user details, permissions, account settings and also assets.


![profile view image](/img/profileview.png){ align=centre, width=800 }

Click on the "Assets" tab to visit your assets list page. (<a href="{{ interwiki.mapshaper }}"> DataEx > User Profile > Assets</a> ) 

![asset list image](/img/asset_list_page.png){ align=centre, width=800 }


### Convert Shapefile to GeoJson 
Before uploading the shapefiles like GeoJson you must ensure the following:

- Shapefile is in Geographic Co-ordinate system
- Shapefile doesn't contain any invalid geometry

If your shapefile is very large or you need to convert it to GeoJson format then you can make use of <a href="{{ interwiki.mapshaper }}">Mapshaper</a>. Below is the webpage you will see after clicking on the link. 

 
![map shaper](/img/mapshaper.png){ align=right, width=800 }

You can either drop the file directly or just click on the select button to upload from your local folder. After selecting the file you want to use, click on import to load the map data.

![select shape file](/img/selectshapefile.png){ align=right, width=800 }

After importing the shapefile, you can view the map contained in the shape file.up
 ![map loaded](/img/maploaded.png){ align=left, width=800 }
 
 Click on the simplify tab to open the simplification menu. Select a method from the options given and click apply. 
 
 ![simplify](/img/simplify.png){ align=right, width=800 }
 
 Then, using a horizontal scroll bar you can choose how much you would like to simplify the lines. 
 
 ![simplified map](/img/simplifiedmap.png){ align=right, width=800 }
 
After settling on the desired simplification level, just click on export tab to get a menu from which you can choose GeoJson and export to a GeoJson file.

![export map](/img/exportmap.png){ align=right, width=800 }

After exporting, you will have simplified your shapefile and converted it to a GeoJson format and reduced its size as well.

### Upload shapefile
To upload this file into DataEx, go back to profile view page and click on assets tab. There you can click on the add button to get the upload box. 

![export map](/img/add_button.png){ align=right, width=800 }


Browse for the shapefile you want to upload and click on the upload button inside the popup box,

![export map](/img/upload_asset.png){ align=right, width=800 }

### Delete shapefile

Shapefiles will be displayed row by row in the assets page. At the right end of each row there is a button. Click on it to get a delete option.  

![export map](/img/delete_asset.png){ align=right, width=800 }

It will delete the asset displayed in that row. 







