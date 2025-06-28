# [...] more code before

            # Verify existing points within the selected region
            if MSLP_sliced.size > 0 and not np.isnan(MSLP_sliced).all():

                # Finds the index relative to minimum values within th ebox
                min_index = np.nanargmin(MSLP_sliced.values)        # ignores nan
                min_value = MSLP_sliced.values.ravel()[min_index]   # minimum value

                # Converts from 1D two 2D
                lat_index, lon_index = np.unravel_index(min_index, MSLP_sliced.values.shape)

                # Gets lat/lon points relative to each minimum value
                lat_sel = lat_t[lat_index, lon_index]
                lon_sel = lon_t[lat_index, lon_index]

                # Add those values in lists
                mslp_points.append(min_value)
                lat_points.append(lat_sel)
                lon_points.append(lon_sel)
                time_steps.append(t)