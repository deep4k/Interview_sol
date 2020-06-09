# Name : Deepak Buddha (Citizen)

# Labelling connected components in a pixel array / Image Segmentation problem
# Excellent resource that helped in understanding connectivity https://aishack.in/tutorials/labelling-connected-components-example/
# While a DFS/Flood fill pure python approach could work, a SciPy or a openCV implementation is more efficient,in this example, SciPy is used

import numpy as np
from scipy.ndimage.measurements import label

# The SciPy method 'label' here takes a input array and a filter structure (the connectivity matrix) and 
# Performs the Rosenfeld and Pfaltz in 1966 union find algorithm where it uses two passes to label connected components
# The first pass checks neighborhood of pixels, labels them and maintains an equivalency list that updates multiple labels connected in the second pass

# This method checks row wise which is why transpose is used to meet question requirements

# returns a numpy array
def parse_data(str):
    return np.loadtxt(str, dtype=np.int) # default delimiter is a whitespace
    
def find_components(eight_neighbour, str):
    arr = np.array(parse_data(str))
    #test
    #arr = np.array([[0,0,1,1],[1,1,0,0],[0,0,0,0],[0,1,1,0],[0,1,1,1]], dtype=np.int) 
    arr1 = arr.transpose() # require to transpose as the example in the question sheet checks for components in the same column instead of traditionally checking rows
    filter = None # the default filter for SciPy label is centrosymmetric matrix with squared connectivity of 1 aka Von Neumann neighborhood (which is 4 connectivity)
    
    if (eight_neighbour):
        filter = np.ones((3, 3), dtype=np.int) # if 8 connectivity requested, we make a Moore neighborhood centrosymmetric matrix 
    labeled, ncomponents = label(arr1, filter) # transposed matrix checked row wise 
    labeled1 = labeled.transpose() # transpose back to get original matrix ranks and files
    #print(labeled1)
    #print(ncomponents)
    write_data(labeled1)
 
 # output_question_4_n8 = 8 connectivity used in output file
 # output_question_4_n4 = 4 connectivity used in output file
def write_data(arr):
    np.savetxt("output_question_4_n8.txt", arr, fmt="%d")
   
   
# parameters for this program
# Bool eight_neighbour: True for 8 connectivity, false for 4
# input file name
def main():
    find_components(True, "input_question_4")
main()
    
    
    
    

