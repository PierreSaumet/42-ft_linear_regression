
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
	This is a game created with Python3.
	It respects the rules of PEP 8.
	Everythings is in English.
	Python rocks.
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def predict(x, slope, intercept):
    return slope * x + intercept

def fct_lineaire_reg():
	print("fct_lineaire_reg\n")
	df = pd.read_csv("data.csv")

	X = df.iloc[0:len(df), 0]
	Y = df.iloc[0:len(df), 1]
	
	slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
	
	# var = input("Donne un chiffre : ")
	# print("predict de {0} = {1}".format(var, predict(X))

	axes = plt.axes()
	axes.grid()
	plt.scatter(X, Y)
	fitline = predict(X, slope, intercept)
	plt.plot(X, fitline, c='r')
	plt.show()



if __name__ == "__main__":
	print("salut entre un chiffre")
	test = input('ici: ')
	print("val = ", test)

	if test == '1':
		fct_lineaire_reg()





