import rasterio
from rasterio.merge import merge
from rasterio.io import MemoryFile
import numpy as np
import os

def band_composite(raster1_path, raster2_path, output_path):
    # Open the first raster (e.g., a 4-band image)
    with rasterio.open(raster1_path) as src1:
        bands1 = [src1.read(i) for i in range(1, src1.count + 1)]
        meta = src1.meta.copy()

    # Open the second raster (1-band)
    with rasterio.open(raster2_path) as src2:
        band2 = src2.read(1) # Assuming the second raster has only 1 band

        # Ensure the rasters have the same dimensions
        if src1.width != src2.width or src1.height != src2.height:
            raise ValueError("The rasters have different dimensions. Resample them first.")

    # Update metadata for the output file
    meta.update({
        "count": len(bands1) + 1  # Total bands
    })

    # Write the output raster
    with rasterio.open(output_path, "w", **meta) as dst:
        # Write the 4 bands from the first raster
        for i, band in enumerate(bands1, start=1):
            dst.write(band, i)
            
        # Write the single band from the second raster
        dst.write(band2, len(bands1) + 1)
        
    print(f"Composite raster created at {output_path}")


# --- Execution Block ---

# TODO: Replace the placeholder '#Path' values with actual file paths.
raster1_path = '#Path' 
raster2_path = '#Path'
output_path = '#Path'

# Perform band compositing
band_composite(raster1_path, raster2_path, output_path)