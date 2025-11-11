# Rasterio-Band-Compositer
This is a simple Python tool that uses Rasterio to merge two raster files into one. It lets you stack bands from, say, an RGB image with a single-band raster like a DEM or thermal layer, creating a combined multi-band file. Just make sure both rasters have the same pixel size - if not, you’ll need to resample one first. Once you have Rasterio and NumPy installed, you can run the band_composite function with your input files. 

