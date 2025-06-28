# [...] more code before 

                # Select WSPD within the new box:
                if label != 'ERA5':
                    WSPD_sliced = WSPD_t.sel(lat=slice(lower_lat_WIND, upper_lat_WIND), lon=slice(left_lon_WIND, right_lon_WIND))
                elif label == 'ERA5':
                    WSPD_sliced = WSPD_t.sel(lat=slice(upper_lat_WIND,lower_lat_WIND), lon=slice(left_lon_WIND, right_lon_WIND))
                
                if WSPD_sliced.size > 0 and not np.isnan(WSPD_sliced).all():
                    # Find the maximum WSPD within the new box
                    max_wspd = np.nanmax(WSPD_sliced.values)
                    wspd_points.append(max_wspd)
                else:
                    # If no valid WSPD points, append NaN
                    print(f"No valid WSPD points found for {label} at timestep {t}. Skipping...")
                    wspd_points.append(np.nan)