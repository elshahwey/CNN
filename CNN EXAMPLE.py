#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
input_red = np.array([
    [0, 0, 0, 0],
    [0, 156, 155, 156],
    [0, 153, 154, 157],
    [0, 0, 0, 0]
])

input_green = np.array([
    [0, 0, 0, 0],
    [0, 167, 166, 167],
    [0, 164, 165, 168],
    [0, 0, 0, 0]
])

input_blue = np.array([
    [0, 0, 0, 0],
    [0, 163, 162, 163],
    [0, 160, 161, 164],
    [0, 0, 0, 0]
])
kernel_red = np.array([[-1, -1, 1], [0, 1, -1], [0, 1, 1]])
kernel_green = np.array([[1, 0, 0], [1, -1, -1], [1, 0, -1]])
kernel_blue = np.array([[0, 1, 1], [0, 1, 0], [1, -1, 1]])
bias = 1
def convolve(input_channel, kernel):
    output_height = input_channel.shape[0] - kernel.shape[0] + 1
    output_width = input_channel.shape[1] - kernel.shape[1] + 1
    output = np.zeros((output_height, output_width))
    
    for i in range(output_height):
        for j in range(output_width):
            output[i, j] = np.sum(input_channel[i:i+kernel.shape[0], j:j+kernel.shape[1]] * kernel)
    
    return output
output_red = convolve(input_red, kernel_red)
output_green = convolve(input_green, kernel_green)
output_blue = convolve(input_blue, kernel_blue)
output_combined = output_red + output_green + output_blue
output_final = output_combined + bias
print("Final Output Matrix:")
print(output_final)


# In[ ]:





# In[ ]:




