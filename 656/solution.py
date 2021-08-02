#!/usr/bin/env python3

import numpy as np
import random as rand

#Get value of adjacent points
def adjacent_points(point, matrix):
	x = point[0]
	y = point[1]
	adj = []
	x_max, y_max = matrix.shape
	for i in range(x-1,x+2):
		for j in range(y-1,y+2):
			if (i >= 0 and j >= 0) and (i< x_max and j < y_max): # ensures that the adjacent points are within the valid range
				adj.append([i,j])
	return adj


#change color of adjacent points, if they are of the same color
def recolor(point, matrix, color):
	original_color = matrix[point[0]][point[1]]
	matrix[point[0]][point[1]] = color
	for adj_point in adjacent_points(point, matrix):
		if matrix[adj_point[0]][adj_point[1]] == original_color:
			matrix[adj_point[0]][adj_point[1]]= color			
	return matrix

#Generate a matrix of random colors
def generate_matrix(shape):
	colors = ['R','B','G']
	matrix = []
	for i in range(0,shape[0]):
		row = []
		for j in range(0,shape[1]):
			row.append(rand.choice(colors))
		matrix.append(row)
	return np.array(matrix)


#Solution testing
alt_colors = ['W','Y','P']
mat_size = 4

mat = generate_matrix((mat_size,mat_size))

print("-----------------------")
print("Original Matrix")
print(mat)
print("-----------------------")

selected_color = rand.choice(alt_colors)
print("New color selected: ",selected_color)

selected_point = rand.sample(range(0,mat_size),2)
print("Random point selected: ", selected_point)

print("-----------------------")
print("Recolored Matrix")
print(recolor(selected_point,mat,selected_color))



	