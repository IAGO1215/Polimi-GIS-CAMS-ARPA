# Polimi-GIS-CAMS-ARPA

We need to retrieve the data from CAMS and ARPA first, where only the data in the year of 2020 and 2021 are available in the ARPA (Interpolated) dataset, and the data in the year of 2020, 2021 and 2022 are available in the CAMS dataset currently. 

## 1. Retrieve data from CAMS and ARPA

- CAMS: Through API (3-year Rolling Archive). The data are stored in .nc format. 
- ARPA (Ground Sensor): Through Socrata API method to retrieve data in the current year or the data from previous year in .csv format. The data from ground sensors are not used in later process in this project but might be useful in other case studies. 
- ARPA (Interpolated): Through direct URL request (2020 and 2021 Available). The data are stored in .txt format compressed in zip files. 

## 2. Data Process of ARPA (Interpolated)

1. Unzip the files either manually or through scripts. 
2. Import the data and the sheet file which contains the information of geographical coordinates (UTM).
3. Join the data with the sheet file, as a result of which, we will obtain a geopandas dataframe which contains the concentration of air pollutants at each geographical coordinate. 
4. Calculate the monthly averages and export the data to .csv files. 

## 3. Data Process of CAMS

1. Import the data, adjust its longitude format and timestamp format and calculate the monthly averages. 
2. Mask the data with Lombardy shapefile. 
3. Export the data to .nc files. 

## 4. Comparison between ARPA and CAMS

1. Import the .csv files and the .nc files exported in the last two steps above. 
2. Calculate the averages and standard variances of each dataset and perform the F-Test and T-Test to these values, to verify if there is a significant difference between them. 
3. Calculate the Pearson correlation coefficient between these two datasets, to check if they have a strong relationship or no. 
4. Export these statistical data to .csv files. 

## 5. CAMS Upscaling

1. Upscale the CAMS dataset from spatial resolution 0.1°x0.1° up to 0.01°x0.01°. 
2. Perform the T-Test and F-Test to verift that the upscaled model is feasible, whose averages and standard variances are not significantly different from those of the original one. 
3. Export the upscaled dataset. 

## 6. Comparison between ARPA and Upscaled CAMS

1. Import the ARPA dataset and the upscaled CAMS dataset. 
2. Calculate the residuals at each pixel between the ARPA dataset and the upscaled CAMS dataset. 
3. Calculate the biases between these two datasets. 
