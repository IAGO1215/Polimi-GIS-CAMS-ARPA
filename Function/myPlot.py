import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from matplotlib.axes import Axes
from matplotlib import colors

import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.feature as cfeature

from cartopy.mpl.geoaxes import GeoAxes
GeoAxes._pcolormesh_patched = Axes.pcolormesh

from matplotlib.lines import Line2D

import geopandas as gpd
import os
cwd = os.getcwd()
cwd_NUTS = cwd + "\\NUTS"

shp_prov1 = gpd.read_file(cwd_NUTS+"\\NUTS_BN_01M_2021_4326_LEVL_1.shp")  
shp_prov2 = gpd.read_file(cwd_NUTS+"\\NUTS_BN_01M_2021_4326_LEVL_2.shp") 

def plot_Threshold(ds_variable,d_timescale):
    if d_timescale == "Daily": 
        if ds_variable == 'NO2':
            d_threshold = 25
        elif ds_variable == 'PM10':
            d_threshold = 45
        elif ds_variable == 'O3':
            d_threshold = 100
        elif ds_variable == 'PM25':
            d_threshold = 15
    elif d_timescale == "Annual":
        if ds_variable == 'NO2':
            d_threshold = 10
        elif ds_variable == 'PM10':
            d_threshold = 10
        elif ds_variable == 'O3':
            d_threshold = 60
        elif ds_variable == 'PM25':
            d_threshold = 5
    else: 
        print("Neither 'Daily' nor 'Annual'!")
        return
    return d_threshold

def plot_ThresholdMap(data_array, longitude, latitude, projection, long_name, vmin, vmax, threshold, GoodColor, BadColor,set_global=True, lonmin=-180, lonmax=180, latmin=-90, latmax=90):
    """ 
    Visualizes a xarray.DataArray with matplotlib's pcolormesh function.
    
    Parameters:
        data_array(xarray.DataArray): xarray.DataArray holding the data values
        longitude(xarray.DataArray): xarray.DataArray holding the longitude values
        latitude(xarray.DataArray): xarray.DataArray holding the latitude values
        projection(str): a projection provided by the cartopy library, e.g. ccrs.PlateCarree()
        color_scale(str): string taken from matplotlib's color ramp reference
        unit(str): the unit of the parameter, taken from the NetCDF file if possible
        long_name(str): long name of the parameter, taken from the NetCDF file if possible
        vmin(int): minimum number on visualisation legend
        vmax(int): maximum number on visualisation legend
        set_global(boolean): optional kwarg, default is True
        lonmin,lonmax,latmin,latmax(float): optional kwarg, set geographic extent is set_global kwarg is set to 
                                            False

    """
    fig=plt.figure(figsize=(20, 10))
    ax = plt.axes(projection=projection)

    img = plt.pcolormesh(longitude, latitude, data_array, 
                    cmap=colors.ListedColormap([GoodColor,BadColor]), 
                    transform=ccrs.PlateCarree(),
                    norm=colors.BoundaryNorm([vmin,threshold,vmax],colors.ListedColormap([GoodColor,BadColor]).N),
                    shading='auto'
                    )

    ax.add_feature(cfeature.BORDERS, edgecolor='black', linewidth=1)
    ax.add_feature(cfeature.COASTLINE, edgecolor='black', linewidth=1)

    if (projection==ccrs.PlateCarree()):
        ax.set_extent([lonmin, lonmax, latmin, latmax], projection)
        gl = ax.gridlines(draw_labels=True, linestyle='--')
        gl.top_labels=False
        gl.right_labels=False
        gl.xformatter=LONGITUDE_FORMATTER
        gl.yformatter=LATITUDE_FORMATTER
        gl.xlabel_style={'size':14}
        gl.ylabel_style={'size':14}

    if(set_global):
        ax.set_global()
        ax.gridlines()
 
    custom_lines = [Line2D([0], [0], color='g', lw=4),
                Line2D([0], [0], color='r', lw=4),
                Line2D([0],[0],color='w',lw=4)]

    ax.legend(custom_lines, ['Below Threshold ' + str(threshold) + ' μg/m3','Above Threshold ' + str(threshold) + ' μg/m3', 'Missing Data or Out of RoI'], loc='lower left')
    ax.set_title(long_name, fontsize=20, pad=20.0)

    return fig, ax

def plot_HeatMap(data_array, longitude, latitude, projection, color_scale, unit, long_name, vmin, vmax, set_global=True, lonmin=-180, lonmax=180, latmin=-90, latmax=90):

    fig=plt.figure(figsize=(20, 10))

    ax = plt.axes(projection=projection)
   
    img = plt.pcolormesh(longitude, latitude, data_array, 
                        cmap=plt.get_cmap(color_scale), 
                        transform=ccrs.PlateCarree(),
                        vmin=vmin,
                        vmax=vmax,
                        shading='auto')

    ax.add_feature(cfeature.BORDERS, edgecolor='black', linewidth=1)
    ax.add_feature(cfeature.COASTLINE, edgecolor='black', linewidth=1)

    if (projection==ccrs.PlateCarree()):
        ax.set_extent([lonmin, lonmax, latmin, latmax], projection)
        gl = ax.gridlines(draw_labels=True, linestyle='--')
        gl.top_labels=False
        gl.right_labels=False
        gl.xformatter=LONGITUDE_FORMATTER
        gl.yformatter=LATITUDE_FORMATTER
        gl.xlabel_style={'size':14}
        gl.ylabel_style={'size':14}

    if(set_global):
        ax.set_global()
        ax.gridlines()

    cbar = fig.colorbar(img, ax=ax, orientation='horizontal', fraction=0.04, pad=0.1)
    cbar.set_label(unit, fontsize=16)
    cbar.ax.tick_params(labelsize=14)
    ax.set_title(long_name, fontsize=20, pad=20.0)

    return fig, ax

def plot_ThresholdMap_Prov(data_array, longitude, latitude, projection, long_name, vmin, vmax, threshold, GoodColor, BadColor,set_global=True, lonmin=-180, lonmax=180, latmin=-90, latmax=90):
    fig=plt.figure(figsize=(20, 10))
    ax = plt.axes(projection=projection)

    img = plt.pcolormesh(longitude, latitude, data_array, 
                    cmap=colors.ListedColormap([GoodColor,BadColor]), 
                    transform=ccrs.PlateCarree(),
                    norm=colors.BoundaryNorm([vmin,threshold,vmax],colors.ListedColormap([GoodColor,BadColor]).N),
                    shading='auto'
                    )

    ax.add_feature(cfeature.BORDERS, edgecolor='black', linewidth=1)
    ax.add_feature(cfeature.COASTLINE, edgecolor='black', linewidth=1)

    shp_prov1.plot(ax=ax, color='black')
    shp_prov2.plot(ax=ax, color='black')

    if (projection==ccrs.PlateCarree()):
        ax.set_extent([lonmin, lonmax, latmin, latmax], projection)
        gl = ax.gridlines(draw_labels=True, linestyle='--')
        gl.top_labels=False
        gl.right_labels=False
        gl.xformatter=LONGITUDE_FORMATTER
        gl.yformatter=LATITUDE_FORMATTER
        gl.xlabel_style={'size':14}
        gl.ylabel_style={'size':14}

    if(set_global):
        ax.set_global()
        ax.gridlines()

    custom_lines = [Line2D([0], [0], color='g', lw=4),
                Line2D([0], [0], color='r', lw=4),
                Line2D([0],[0],color='w',lw=4)]

    ax.legend(custom_lines, ['Below Threshold ' + str(threshold) + ' μg/m3','Above Threshold ' + str(threshold) + ' μg/m3', 'Missing Data or Out of RoI'], loc='lower left')
    ax.set_title(long_name, fontsize=20, pad=20.0)

    return fig, ax

def plot_HeatMap_Prov(data_array, longitude, latitude, projection, color_scale, unit, long_name, vmin, vmax, set_global=True, lonmin=-180, lonmax=180, latmin=-90, latmax=90):

    fig=plt.figure(figsize=(20, 10))

    ax = plt.axes(projection=projection)
   
    img = plt.pcolormesh(longitude, latitude, data_array, 
                        cmap=plt.get_cmap(color_scale), 
                        transform=ccrs.PlateCarree(),
                        vmin=vmin,
                        vmax=vmax,
                        shading='auto')

    ax.add_feature(cfeature.BORDERS, edgecolor='black', linewidth=1)
    ax.add_feature(cfeature.COASTLINE, edgecolor='black', linewidth=1)

    shp_prov1.plot(ax=ax, color='black')
    shp_prov2.plot(ax=ax, color='black')

    if (projection==ccrs.PlateCarree()):
        ax.set_extent([lonmin, lonmax, latmin, latmax], projection)
        gl = ax.gridlines(draw_labels=True, linestyle='--')
        gl.top_labels=False
        gl.right_labels=False
        gl.xformatter=LONGITUDE_FORMATTER
        gl.yformatter=LATITUDE_FORMATTER
        gl.xlabel_style={'size':14}
        gl.ylabel_style={'size':14}

    if(set_global):
        ax.set_global()
        ax.gridlines()

    cbar = fig.colorbar(img, ax=ax, orientation='horizontal', fraction=0.04, pad=0.1)
    cbar.set_label(unit, fontsize=16)
    cbar.ax.tick_params(labelsize=14)
    ax.set_title(long_name, fontsize=20, pad=20.0)

    return fig, ax