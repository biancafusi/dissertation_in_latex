dlat, dlon = 2.0, 2.0

# [...] more code before
    for t in range(len(time)):
        MSLP_t = dataset_MSLP.isel(time=t)
        WSPD_t = dataset_WSPD.isel(time=t)

        if label == 'NOAA':
            lon_array_sel = lon_array.isel(time=t)
            lat_array_sel = lat_array.isel(time=t)
            
            lon_points.append(lon_array_sel.values)
            lat_points.append(lat_array_sel.values)

            mslp_points.append(MSLP_t.values)
            wspd_points.append(WSPD_t.values)
            time_steps.append(t)

            lat_points_NOAA = lat_points
            lon_points_NOAA = lon_points

        else:
            # Searching for the minimal value (based on NOAA)
            upper_lat, lower_lat = lat_points_NOAA[t] + dlat, lat_points_NOAA[t] - dlat
            left_lon, right_lon = lon_points_NOAA[t] - dlon, lon_points_NOAA[t] + dlon

           
            lon_sliced = lon_array.sel(lon=slice(left_lon, right_lon))
            if label == 'ERA5':
                lat_sliced = lat_array.sel(lat=slice(upper_lat, lower_lat))
                MSLP_sliced = MSLP_t.sel(lon=slice(left_lon, right_lon), lat=slice(upper_lat,lower_lat))
            else:
                lat_sliced = lat_array.sel(lat=slice(lower_lat,upper_lat))
                MSLP_sliced = MSLP_t.sel(lon=slice(left_lon, right_lon), lat=slice(lower_lat,upper_lat))


            lat_t, lon_t = np.meshgrid(lat_sliced, lon_sliced, indexing='ij')