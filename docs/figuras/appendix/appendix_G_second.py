def creating_USA_mask(lat_array, lon_array):
    # Step 1: Load the shapefile of countries from Natural Earth
    countries = gpd.read_file("/mnt/beegfs/bianca.fusinato/monan/MASTERS_RESULTS/new_helene_outputs/shapefiles_usa/ne_10m_admin_0_countries.shp")

    # Extract latitude and longitude from the input arrays
    lon = lon_array
    lat = lat_array

    # Step 2: creating new latitude and logitude vectors
    lon2d, lat2d = np.meshgrid(lon, lat)

    # Step 3: Filter the shapefile to keep only the United States polygon
    usa = countries[countries['ADMIN'] == 'United States of America']

    # Step 4: Flatten the lat/lon grid and create Point geometries for each coordinate
    points = gpd.GeoSeries([Point(xy) for xy in zip(lon2d.ravel(), lat2d.ravel())])

    # Step 5: Create a GeoDataFrame from the points with the appropriate CRS
    gdf_points = gpd.GeoDataFrame(geometry=points, crs="EPSG:4326")

    # Step 5: Check which points are within the United States polygon (land mask)
    land_mask_flat = gdf_points.within(usa.unary_union)

    # Step 6: Reshape the 1D mask back to the original 2D grid shape and return it
    land_mask = land_mask_flat.values.reshape(lat2d.shape)

    return land_mask