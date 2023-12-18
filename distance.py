# Import Packages
import geopy.distance

def dist(coord_1_lat, coord_1_lon, coord_2_lat, coord_2_lon):
	# This function calculates the distance between 2 locations
	coords_1 = (coord_1_lat, coord_1_lon)
	coords_2 = (coord_2_lat, coord_2_lon)

	return geopy.distance.distance(coords_1, coords_2).km