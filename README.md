# Polimi-GIS-CAMS-ARPA

This case study is focused on the Lombardia regoin, and the goal is to assess the data of air quality from the CAMS (Copernicus Atmosphere Monitoring Service) dataset, considering the ARPA (Agenzia Regionale per la Protezione dell'Ambiente) data as ground truth. 

The air quality data in the year of 2018, 2019, 2020 and 2021 are available in the ARPA (Interpolated) dataset, and the data in the year of 2020, 2021 and 2022 are available in the CAMS dataset currently. There are also ground sensors data from the ARPA dataset, but it is not recommended to use those point vector data to perform the data assessment since it might produce errors due to its insufficient data. 

Additionally, the shapefile of the Lombardy region can be found in the NUTS dataset. And DUSAF dataset is useful to analyze the air quality conditions according to land use. 

## Data Sources

1. CAMS: [European Air Quality Forecast](https://ads.atmosphere.copernicus.eu/cdsapp#!/dataset/cams-europe-air-quality-forecasts?tab=overview)
2. ARPA Ground Sensors: [ARPA Elenco Data Pubblicati](https://www.dati.lombardia.it/widgets/8ask-gxyr)
3. ARPA Interpolated: Sistema Modellistico ARPA Lombardia
4. NUTS: [Shapefiles](https://gisco-services.ec.europa.eu/distribution/v2/nuts/nuts-2021-files.html)
5. DUSAF Landuse: [DUSAF 6.0 (2018)](https://www.geoportale.regione.lombardia.it/metadati?p_p_id=detailSheetMetadata_WAR_gptmetadataportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_detailSheetMetadata_WAR_gptmetadataportlet_uuid=%7B18EE7CDC-E51B-4DFB-99F8-3CF416FC3C70%7D)

## Data Process

### 1. Retrieve data from CAMS and ARPA

- CAMS: Through API (3-year Rolling Archive). The data are stored in .nc format. 
- ARPA (Ground Sensor): Through Socrata API method to retrieve data in the current year or download the data from previous year in .csv format. The data from ground sensors are not used in later process in this project but might be useful in other case studies. 
- ARPA (Interpolated): Through direct URL request (Available from 2018-2021). The data are stored in .txt format compressed in zip files. 

### 2. Data Process of ARPA (Interpolated)

1. Unzip the files either manually or through scripts. 
2. Import the data and the sheet file which contains the information of geographical coordinates (UTM).
3. Join the data with the sheet file, as a result of which, we will obtain a geopandas dataframe which contains the concentration of air pollutants at each geographical coordinate. 
4. Calculate the monthly averages and export the data to .csv files. 

### 3. Data Process of CAMS

1. Import the data, adjust its longitude format and timestamp format and calculate the monthly averages. 
2. Mask the data with Lombardy shapefile. 
3. Export the data to .nc files. 

### 4. Comparison between ARPA and CAMS

1. Import the .csv files and the .nc files exported in the last two steps above. 
2. Calculate the averages and standard variances of each dataset and perform the F-Test and T-Test to these values, to verify if there is a significant difference between them. 
3. Calculate the Pearson correlation coefficient between these two datasets, to check if they have a strong relationship or no. 
4. Export these statistical data to .csv files. 

### 5. CAMS Upscaling

1. Upscale the CAMS dataset from spatial resolution 0.1°x0.1° up to 0.01°x0.01°. 
2. Perform the T-Test and F-Test to verift that the upscaled model is feasible, whose averages and standard variances are not significantly different from those of the original one. 
3. Export the upscaled dataset. 

### 6. Comparison between ARPA and Upscaled CAMS

1. Import the ARPA dataset and the upscaled CAMS dataset. 
2. Calculate the residuals at each pixel between the ARPA dataset and the upscaled CAMS dataset. 
3. Calculate the biases between these two datasets. 
