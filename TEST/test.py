
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

"""
    tests for ft_linear_regression
"""

import pandas as pd         # read csv
import os                   # check if file is empty

def check_file():
    file_name  = "data.csv"
    # Check if the file name is data.csv
    if file_name != "data.csv":
        return True

    # Check if the file is empty
    if os.stat(file_name).st_size  == 0:
        return True 
    return False


def calcul_devirees_partielles(anc_theta_0, anc_theta_1):
    M = len(X)
    derivee_thetat_0 = float(0)
    derivee_thetat_1 = float(0)



def load_dataset():
    dataFrame = pd.read_csv("data.csv")
    print("DataFrame: \n{}\n".format(dataFrame))

    # Kilometrage
    X = dataFrame.iloc[0:len(dataFrame), 0]
    # Price
    Y = dataFrame.iloc[0:len(dataFrame), 1]

    print("X = \n{}\n".format(X))
    print("Y = \n{}\n".format(Y))

    # Calcul derive partielles
    M = len(X)
    print("Taille dataser = {}".format(M))

def main():
    print("Testing reading data.csv:\n")

    if check_file() == True:
        print("Error in the dataset file\n")
    else:
        print("No error in the dataset file =)\n")

    load_dataset()
    # calcul_derive_partielles()


if __name__ == "__main__":
    main()