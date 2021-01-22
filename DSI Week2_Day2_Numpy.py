
# coding: utf-8

# # 100 numpy exercises
# 
# This is a collection of exercises that have been collected in the numpy mailing list, on stack overflow
# and in the numpy documentation. The goal of this collection is to offer a quick reference for both old
# and new users but also to provide a set of exercises for those who teach.
# 
# 
# If you find an error or think you've a better way to solve some of them, feel
# free to open an issue at <https://github.com/rougier/numpy-100>.

# File automatically generated. See the documentation to update questions/answers/hints programmatically.

# Run the `initialize.py` module, then for each question you can query the
# answer or an hint with `hint(n)` or `answer(n)` for `n` question number.

# In[ ]:


get_ipython().run_line_magic('run', 'initialise.py')


# #### 1. Import the numpy package under the name `np` (★☆☆)

# In[5]:


import numpy as np


# #### 2. Print the numpy version and the configuration (★☆☆)

# In[7]:


print (np.__version__)


# #### 3. Create a null vector of size 10 (★☆☆)

# In[9]:


vector_null = np.zeros(10)
print(vector_null)


# ###### Function version

# In[17]:


def vector_null_func(num):
    the_vector = np.zeros(num)
    return the_vector


# In[18]:


vector_null_func(10)


# #### 4. How to find the memory size of any array (★☆☆)

# In[12]:


#Because it said memory size of ANY array | Could simply be the attribute{.size}
def memory_size(array):
    ms = array.size
    return ms


# In[132]:


vector_null = np.zeros(10)
memory_size(vector_null)


# #### 5. How to get the documentation of the numpy add function from the command line? (★☆☆)

# In[14]:


help(np.add)


# #### 6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)

# In[22]:


my_null_vector = vector_null_func(10)
my_null_vector[4] = 1
my_null_vector


# #### 7. Create a vector with values ranging from 10 to 49 (★☆☆)

# In[25]:


ten_49_array = np.arange(start=10, stop=49, step=9, dtype=float) #Attributes just to make sure i know what I'm doing :)
ten_49_array


# #### 8. Reverse a vector (first element becomes last) (★☆☆)

# In[115]:


flipped_ten_49_array = ten_49_array[::-1] #What is the issue with .invert
flipped_ten_49_array


# In[122]:


np.flip(ten_49_array, axis=0) #


# In[ ]:


np.


# #### 9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)

# In[123]:


the_matrix = np.arange(9).reshape(3,3)
the_matrix


# In[127]:


np.flip(np.flip(the_matrix, axis=0),axis=1)


# #### 10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)

# In[61]:


not_zero_list = [1,2,0,0,4,0]
not_zero_array = np.array(not_zero_list)


# In[59]:


def non_zero_elements(array): # Check Logic
    non_zero_list = []
    for i in enumerate(array):
        if i != 0:
            index = i.index
            non_zero_list.append(index)
    return non_zero_list


# In[63]:


non_zero_indices = np.nonzero(not_zero_array)
non_zero_indices


# #### 11. Create a 3x3 identity matrix (★☆☆)

# In[74]:


array1 = np.array([1, 0, 0])
array2 = np.array([0, 1, 0])
array3 = np.array([0, 0, 1])
my_matrix = np.array([array1,array2,array3])
my_matrix


# #### 12. Create a 3x3x3 array with random values (★☆☆)

# In[76]:


my_bigger_matrix = np.random.rand(3, 3, 3)
my_bigger_matrix


# #### 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)

# In[78]:


ten_by10 = np.random.rand(10,10)
ten_by10


# In[81]:


the_min = print("The min is: {}.".format(ten_by10.min()))


# In[82]:


the_max = print("The max is: {}.".format(ten_by10.max()))


# #### 14. Create a random vector of size 30 and find the mean value (★☆☆)

# In[84]:


rando_size_30 = np.random.rand(30)
rando_size_30
mean_value = len(rando_size_30)/sum(rando_size_30)
print("The mean value is: {}.".format(mean_value))


# #### 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)

# In[94]:


array_2dv1 = np.array([[1, 1, 1],[1, 0, 1], [1, 1, 1]])
array_2dv2 = np.array([[1, 1, 1, 1],[1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]])
array_2dv3 = np.array([[1, 1, 1, 1, 1],[1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]])

print(array_2dv3)


# #### 16. How to add a border (filled with 0's) around an existing array? (★☆☆)

# In[100]:


help(np.pad)


# In[130]:


zero_filled_borders = np.pad(array_2dv1, pad_width=1, mode="constant", constant_values=0)
zero_filled_borders


# #### 17. What is the result of the following expression? (★☆☆)
# ```python
# 0 * np.nan
# np.nan == np.nan
# np.inf > np.nan
# np.nan - np.nan
# np.nan in set([np.nan])
# 0.3 == 3 * 0.1
# ```

# In[104]:


0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
np.nan in set([np.nan])
0.3 == 3 * 0.1


# #### 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)

# In[112]:


my_zero_matrice = np.zeros((5,5))
my_zero_matrice


# In[129]:


my_zero_matrice[1][0] = 1
my_zero_matrice[2][1] = 2
my_zero_matrice[3][2] = 3
my_zero_matrice[4][3] = 4
my_zero_matrice


# #### 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)

# In[ ]:


my_zero_matrice = np.zeros((8,8))


# #### 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?

# #### 21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)

# #### 22. Normalize a 5x5 random matrix (★☆☆)

# #### 23. Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)

# #### 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)

# #### 25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)

# #### 26. What is the output of the following script? (★☆☆)
# ```python
# # Author: Jake VanderPlas
# 
# print(sum(range(5),-1))
# from numpy import *
# print(sum(range(5),-1))
# ```

# #### 27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)
# ```python
# Z**Z
# 2 << Z >> 2
# Z <- Z
# 1j*Z
# Z/1/1
# Z<Z>Z
# ```

# #### 28. What are the result of the following expressions?
# ```python
# np.array(0) / np.array(0)
# np.array(0) // np.array(0)
# np.array([np.nan]).astype(int).astype(float)
# ```

# #### 29. How to round away from zero a float array ? (★☆☆)

# #### 30. How to find common values between two arrays? (★☆☆)

# #### 31. How to ignore all numpy warnings (not recommended)? (★☆☆)

# #### 32. Is the following expressions true? (★☆☆)
# ```python
# np.sqrt(-1) == np.emath.sqrt(-1)
# ```

# #### 33. How to get the dates of yesterday, today and tomorrow? (★☆☆)

# #### 34. How to get all the dates corresponding to the month of July 2016? (★★☆)

# #### 35. How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)

# #### 36. Extract the integer part of a random array of positive numbers using 4 different methods (★★☆)

# #### 37. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)

# #### 38. Consider a generator function that generates 10 integers and use it to build an array (★☆☆)

# #### 39. Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)

# #### 40. Create a random vector of size 10 and sort it (★★☆)

# #### 41. How to sum a small array faster than np.sum? (★★☆)

# #### 42. Consider two random array A and B, check if they are equal (★★☆)

# #### 43. Make an array immutable (read-only) (★★☆)

# #### 44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)

# #### 45. Create random vector of size 10 and replace the maximum value by 0 (★★☆)

# #### 46. Create a structured array with `x` and `y` coordinates covering the [0,1]x[0,1] area (★★☆)

# #### 47. Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj))

# #### 48. Print the minimum and maximum representable value for each numpy scalar type (★★☆)

# #### 49. How to print all the values of an array? (★★☆)

# #### 50. How to find the closest value (to a given scalar) in a vector? (★★☆)

# #### 51. Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆)

# #### 52. Consider a random vector with shape (100,2) representing coordinates, find point by point distances (★★☆)

# #### 53. How to convert a float (32 bits) array into an integer (32 bits) in place?

# #### 54. How to read the following file? (★★☆)
# ```
# 1, 2, 3, 4, 5
# 6,  ,  , 7, 8
#  ,  , 9,10,11
# ```

# #### 55. What is the equivalent of enumerate for numpy arrays? (★★☆)

# #### 56. Generate a generic 2D Gaussian-like array (★★☆)

# #### 57. How to randomly place p elements in a 2D array? (★★☆)

# #### 58. Subtract the mean of each row of a matrix (★★☆)

# #### 59. How to sort an array by the nth column? (★★☆)

# #### 60. How to tell if a given 2D array has null columns? (★★☆)

# #### 61. Find the nearest value from a given value in an array (★★☆)

# #### 62. Considering two arrays with shape (1,3) and (3,1), how to compute their sum using an iterator? (★★☆)

# #### 63. Create an array class that has a name attribute (★★☆)

# #### 64. Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)? (★★★)

# #### 65. How to accumulate elements of a vector (X) to an array (F) based on an index list (I)? (★★★)

# #### 66. Considering a (w,h,3) image of (dtype=ubyte), compute the number of unique colors (★★★)

# #### 67. Considering a four dimensions array, how to get sum over the last two axis at once? (★★★)

# #### 68. Considering a one-dimensional vector D, how to compute means of subsets of D using a vector S of same size describing subset  indices? (★★★)

# #### 69. How to get the diagonal of a dot product? (★★★)

# #### 70. Consider the vector [1, 2, 3, 4, 5], how to build a new vector with 3 consecutive zeros interleaved between each value? (★★★)

# #### 71. Consider an array of dimension (5,5,3), how to mulitply it by an array with dimensions (5,5)? (★★★)

# #### 72. How to swap two rows of an array? (★★★)

# #### 73. Consider a set of 10 triplets describing 10 triangles (with shared vertices), find the set of unique line segments composing all the  triangles (★★★)

# #### 74. Given a sorted array C that corresponds to a bincount, how to produce an array A such that np.bincount(A) == C? (★★★)

# #### 75. How to compute averages using a sliding window over an array? (★★★)

# #### 76. Consider a one-dimensional array Z, build a two-dimensional array whose first row is (Z[0],Z[1],Z[2]) and each subsequent row is  shifted by 1 (last row should be (Z[-3],Z[-2],Z[-1]) (★★★)

# #### 77. How to negate a boolean, or to change the sign of a float inplace? (★★★)

# #### 78. Consider 2 sets of points P0,P1 describing lines (2d) and a point p, how to compute distance from p to each line i (P0[i],P1[i])? (★★★)

# #### 79. Consider 2 sets of points P0,P1 describing lines (2d) and a set of points P, how to compute distance from each point j (P[j]) to each line i (P0[i],P1[i])? (★★★)

# #### 80. Consider an arbitrary array, write a function that extract a subpart with a fixed shape and centered on a given element (pad with a `fill` value when necessary) (★★★)

# #### 81. Consider an array Z = [1,2,3,4,5,6,7,8,9,10,11,12,13,14], how to generate an array R = [[1,2,3,4], [2,3,4,5], [3,4,5,6], ..., [11,12,13,14]]? (★★★)

# #### 82. Compute a matrix rank (★★★)

# #### 83. How to find the most frequent value in an array?

# #### 84. Extract all the contiguous 3x3 blocks from a random 10x10 matrix (★★★)

# #### 85. Create a 2D array subclass such that Z[i,j] == Z[j,i] (★★★)

# #### 86. Consider a set of p matrices wich shape (n,n) and a set of p vectors with shape (n,1). How to compute the sum of of the p matrix products at once? (result has shape (n,1)) (★★★)

# #### 87. Consider a 16x16 array, how to get the block-sum (block size is 4x4)? (★★★)

# #### 88. How to implement the Game of Life using numpy arrays? (★★★)

# #### 89. How to get the n largest values of an array (★★★)

# #### 90. Given an arbitrary number of vectors, build the cartesian product (every combinations of every item) (★★★)

# #### 91. How to create a record array from a regular array? (★★★)

# #### 92. Consider a large vector Z, compute Z to the power of 3 using 3 different methods (★★★)

# #### 93. Consider two arrays A and B of shape (8,3) and (2,2). How to find rows of A that contain elements of each row of B regardless of the order of the elements in B? (★★★)

# #### 94. Considering a 10x3 matrix, extract rows with unequal values (e.g. [2,2,3]) (★★★)

# #### 95. Convert a vector of ints into a matrix binary representation (★★★)

# #### 96. Given a two dimensional array, how to extract unique rows? (★★★)

# #### 97. Considering 2 vectors A & B, write the einsum equivalent of inner, outer, sum, and mul function (★★★)

# #### 98. Considering a path described by two vectors (X,Y), how to sample it using equidistant samples (★★★)?

# #### 99. Given an integer n and a 2D array X, select from X the rows which can be interpreted as draws from a multinomial distribution with n degrees, i.e., the rows which only contain integers and which sum to n. (★★★)

# #### 100. Compute bootstrapped 95% confidence intervals for the mean of a 1D array X (i.e., resample the elements of an array with replacement N times, compute the mean of each sample, and then compute percentiles over the means). (★★★)
