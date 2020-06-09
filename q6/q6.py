from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

import numpy as np

# Points in Polygon problem, implenting Ray casting algorithm with Shapely where you extend a ray from infinity to the probe point
# And if this ray intersects with the polygon an odd number of times then it is inside 
# Else if it intersects 0 or even number of times, it is outside

# Originally wanted to use matplotlib path library to do this problem but realized that function has an open issue with points on edge of polygon
# depending on the direction of construction of polygon @ https://github.com/matplotlib/matplotlib/issues/9704, hence using Shapely 


def parse_input(points_str, polygon_str):
    points_arr = np.loadtxt(points_str, dtype=np.int) # N x 2 2d array
    polygon_vertices = np.loadtxt(polygon_str, dtype=np.int) #N x 2 2d array
    return points_arr, polygon_vertices
    
def check_location(points_str, polygon_str):
    points, polygon_vertices = parse_input(points_str, polygon_str)
    polygon = Polygon(polygon_vertices)
    flags = np.empty([1, points.shape[0]], dtype = "U7") # array to add the result in a unicode string encoding
    for i in range(points.shape[0]): 
        if (polygon.contains(Point((points[i])))): # Ray casting algorithm library function used as explained above
            flags[0][i] = 'inside'
        else:
            flags[0][i] = 'outside'
            
    result = np.concatenate((points, flags.T), axis = 1)
    #print(flags)
    #print(result)
    write_data(result)

def write_data(arr):
    np.savetxt("output_question_6", arr, fmt="%s")

def main():
    check_location("input_question_6_points", "input_question_6_polygon")
    


main()
