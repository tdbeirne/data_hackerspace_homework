#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np

def histogram_times(filename):
    #I'm importing inside the method because all the code must go here
    import re

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        time_list = []
        for row in csv_reader:
            time_list.append(row[1])

    count = 0
    while count < len(time_list):
        if ":" not in time_list[count]:
            del time_list[count]
        else:
            count += 1

    #now that entries missing a colon are gone
    #lets fix the rows with C's in them
    pattern = re.compile(r'^[^0-9]*')
    for x in range(0, len(time_list)):
        time_list[x] = re.sub(pattern, '', time_list[x])

    hour_list = [0] * 24

    for time in time_list:
        to_int = int(time.split(":")[0])
        if int(to_int < 24 and to_int >= 0):
            hour_list[to_int] += 1

    return hour_list

def weigh_pokemons(filename, weight):
    with open(filename) as json_file:
        #load json data
        json_data = json.load(json_file)

        #create pokemon name list
        poke_list = []

        for pokemon in json_data["pokemon"]:
            #add "kg" to match string
            if pokemon["weight"] == str(weight) + " kg":
                #append to list if weight is equal
                poke_list.append(str(pokemon["name"]))

        return poke_list


def single_type_candy_count(filename):
    with open(filename) as json_file:
        #load json data
        json_data = json.load(json_file)

        candy_counter = 0

        for pokemon in json_data["pokemon"]:
            if len(pokemon["type"]) == 1 and "candy_count" in pokemon:
                candy_counter += pokemon["candy_count"]

        return candy_counter


def reflections_and_projections(points):
    #make sure to use floats Tom!
    #copy input array
    edited_array = points

    #flip array over y = 1
    edited_array[1] = ((edited_array[1] - 1.0) * -1.0) + 1.0

    #set up rotate array for rotation
    rotate_array = np.array([[0.0, -1.0], [1.0, 0.0]])
    #rotate the array
    edited_array = np.matmul(rotate_array, edited_array)

    #set up for projection of vectors onto y = 3x
    #this is the front constant in the projection equation
    #1 / (3^2 + 1) = (1/10) = 0.1
    front_constant = 0.1
    project_array = np.array([[1.0, 3.0], [3.0, 9.0]])
    #project the vectors
    edited_array = np.matmul((front_constant * project_array), edited_array)

    #round the array to make it look cleaner
    edited_array = np.around(edited_array, decimals = 4)

    return edited_array


def normalize(image):
    #copy input
    normalized_array = image

    #get min and max of array
    minimum = np.amin(image)
    maximum = np.amax(image)

    #normalize the array
    normalized_array = (255 / (maximum - minimum)) * (normalized_array - minimum)

    return normalized_array


def sigmoid_normalize(image, a):
    #copy input
    normalized_array = image

    #get min and max of array
    minimum = np.amin(image)
    maximum = np.amax(image)

    #normalize the array
    normalized_array = 255.0 / (1.0 + np.exp(-1.0 / (a ** (normalized_array - 128.0))))

    return normalized_array
