#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

#####################################
# Programme Python 3 Type           #
# Autor: Pierre Saumet, Paris, 2022 #
# Licence: GPL                      #
#####################################

#####################################
# Informations:
"""
	This is a program created with Python3.
	It respects the rules of PEP 8.
	Everythings is in English.
	Python rocks.
"""

import os
from os.path import exists
import matplotlib.pyplot as plt
import pandas as pd


COST_RECORDER = []
learning_rate_ALPHA = float(0.1)
initial_theta_0 = float(0)
initial_theta_1 = float(0)
nombre_iterations = 1000



def ft_exit(err_nbr):
	if err_nbr == 1:
		print("Error with the dataset from data.csv file\n")
		exit()
	if err_nbr == 0:
		print("Error\n")
		exit()

def	get_data():
	# Check if the file exist
	if exists("data.csv") == False:
		ft_exit(1)
	# Check if the file is empty
	if os.stat("data.csv").st_size == 0:
		ft_exit(1)
	# Get a Dataframe from data.csv
	dataFrame = pd.read_csv("data.csv")
	# Check nbr of columns
	if len(dataFrame.columns) != 2:
		ft_exit(1)
	# Check if columns have same size of items
	X = dataFrame.iloc[0:len(dataFrame), 0]
	Y = dataFrame.iloc[0:len(dataFrame), 1]
	if len(X) != len(Y):
		ft_exit(1)
	else:
		return [X, Y]

def normalize_item(item, datas):
	return (item - datas.min()) / (datas.max() - datas.min())
	
		
def normalize_datas(X, Y):
	X_tmp = list()
	for i in range(len(X)):
		X_tmp.append(normalize_item(X[i], X))
	Y_tmp = list()
	for i in range(len(Y)):
		Y_tmp.append(normalize_item(Y[i], Y))
	return [X_tmp, Y_tmp]
		
"""
	Algorithm
"""
def ft_cost(theta_0, theta_1, X, Y):
	global_cost  = 0
	for i in range(len(X)):
		cost_i = ((theta_0 + (theta_1 * X[i])) - Y[i]) * ((theta_0 + (theta_1 * X[i])) - Y[i]) 
		global_cost+= cost_i
	return (1/ (2 * len(X))) * global_cost


def ft_partial_derivative(old_theta_0, old_theta_1, X, Y, M):
	derivee_theta_0 = 0.0
	derivee_theta_1 = 0.0
	for i in range(0, len(X)):
		derivee_theta_0 += float(((old_theta_0 + (old_theta_1 * X[i])) - float(Y[i])))
		derivee_theta_1 += (((old_theta_0 + (old_theta_1 * X[i]))) - float(Y[i])) * float(X[i])
	derivee_theta_0 = (1 / M) * derivee_theta_0
	derivee_theta_1 = ( 1 / M) * derivee_theta_1
	return [derivee_theta_0, derivee_theta_1]

def ft_new_theta(old_theta_0, old_theta_1, X, Y, M):
	[derivee_theta_0, derivee_theta_1] = ft_partial_derivative(old_theta_0, old_theta_1, X, Y, M)
	nouvelle_theta_0 = old_theta_0 - (learning_rate_ALPHA * derivee_theta_0)
	nouvelle_theta_1 = old_theta_1 - (learning_rate_ALPHA * derivee_theta_1)
	COST_RECORDER.append(ft_cost(nouvelle_theta_0, nouvelle_theta_1, X, Y))
	return [nouvelle_theta_0, nouvelle_theta_1]

def ft_gradiant_descent(X, Y, M):
	tmp_theta_0 = initial_theta_0
	tmp_theta_1 = initial_theta_1
	for i in range(nombre_iterations):
		[nouvelle_theta_0, nouvelle_theta_1] = ft_new_theta(tmp_theta_0, tmp_theta_1, X, Y, M)
		tmp_theta_0 = nouvelle_theta_0 
		tmp_theta_1 = nouvelle_theta_1
	return [tmp_theta_0, tmp_theta_1]


if __name__ == "__main__":
	[X_old, Y_old] = get_data()
	[X, Y] = normalize_datas(X_old, Y_old)
	print("Result = {}".format([X, Y]))
	print(type([X, Y]))

	[final_theta_0, final_theta_1] = ft_gradiant_descent(X, Y, len(X))
	print("After {0} iterations theta_0 = {1}, theta_1 = {2}".format(nombre_iterations, final_theta_0, final_theta_1))


	stopping_threshold = 1e-6
	print(stopping_threshold)
	xx = []
	yy = []

	for i in range(len(COST_RECORDER)):
		xx.append(i)
		yy.append(COST_RECORDER[i])
	
	axes = plt.axes()
	axes.grid()
	plt.figure(1)
	plt.xlabel('Nombre d\'iterations')
	plt.ylabel('Cout d\'erreur global')
	plt.scatter(xx,yy)
	plt.figure(2)
	plt.plot(X_old, Y_old, 'bo')
	plt.xlabel('Mileage')
	plt.ylabel('Price')
	# print("Cost recorder = {}".format(COST_RECORDER))
	plt.show()


"""
trucs relous
	1) comprendre les fonctions lineraires
	2 ) ompnredre les fonctions lineaire regresivves
	3 )tester avec librairies
	4 ) teser sans
	5 ) pb normaliser les donnes
	6) test ? check ?


"""