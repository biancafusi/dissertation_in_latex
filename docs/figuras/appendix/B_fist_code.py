# Reference dataset: best track (NOAA)
NOAA = xr.open_dataset(NOAA_path)
time = NOAA.time.sel(time=slice(initial_day, final_day))
NOAA_hourly = NOAA.sel(time=time)
MSLP = NOAA_hourly.mslp
lat = NOAA_hourly.lat
lon = NOAA_hourly.lon
# Stores NOAA's tracking
lat_points_NOAA, lon_points_NOAA, mslp_points_NOAA = [], [], []
for t in range(0, len(time), 1):
    lon_array_sel = lon.isel(time=t)
    lat_array_sel = lat.isel(time=t)
    lon_points_NOAA.append(lon_array_sel.values)
    lat_points_NOAA.append(lat_array_sel.values)
    mslp_points_NOAA.append(MSLP.isel(time=t).values)