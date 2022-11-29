# Polimi-GIS-CAMS-ARPA

We need to retrieve the data from CAMS and ARPA (Interpolated) first, where only the data in the year of 2020 and 2021 are available in the ARPA (Interpolated) dataset, and the data in the year of 2020, 2021 and 2022 are available in the CAMS dataset currently. 

After requesting the data, we need to process the ARPA data (.txt file) first. To be more specific, we need to combine the interpolated ARPA data with the sheet file which contains the geographical coordinate data. 

Then, we need to process the CAMS data (.nc file) before we do analysis to it, such as adjusting its longitude from 0->360 to -180->180, re-formatting its timestamp and calculate averages along its dimensions so that we can transfer the xarray dataset into geopandas geodataframe. 

## 1. Retrieve data from CAMS and ARPA (Interpolated)

- CAMS: Through API (3-year Rolling Archive)
- ARPA: Through direct URL request (2020 and 2021 Available)

## 2. Data Process of ARPA (Interpolated)

1. 

## 3. Data Process of CAMS

This

## 4. Comparison between ARPA and CAMS



## 5. CAMS Upscaling



## 6. Comparison between ARPA and Upscaled CAMS


