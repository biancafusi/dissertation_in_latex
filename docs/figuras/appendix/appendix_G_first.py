# [...] more code before
        land_mask_USA = creating_USA_mask(lat_data, lon_data)
        rainfall_USA_only = rainfall.where(land_mask_USA)

        land_mask_not_USA = creating_not_USA_mask(lat_data, lon_data)
        rainfall_not_USA = rainfall.where(land_mask_not_USA)
