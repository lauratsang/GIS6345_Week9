import arcpy

SAVI_raster = arcpy.sa.SAVI("L8_SactoCA_6_8_18.tif",5,4,0.33)

SAVI_raster
