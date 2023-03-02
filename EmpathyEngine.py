#-------------------------------------------------------------------------------
# Name:        EmpathyEngine.py
# Purpose: choosing the best sentiment to express to reach target emotion.
#
# Author:      The Schim
#
# Created:     01/03/2023
# Copyright:   (c) The Schim 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import csv
from collections import defaultdict

def analyze_emotions(my_mind, my_yearning):
    # Find the shared keys between my_mind and my_yearning
    shared_keys = set(my_mind.keys()) & set(my_yearning.keys())

    # Calculate the average values for each key in my_mind
    avg_values = {}
    for key in shared_keys:
        avg_values[key] = {}
        for subkey in my_mind[key]:
            avg_values[key][subkey] = my_mind[key][subkey] / len(my_mind[key])

    # Load the CSV file and calculate the distances between each emotion and my_yearning
    distances = defaultdict(float)
    with open('GrowingEmotions.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for key in shared_keys:
                for subkey in my_yearning[key]:
                    if subkey in avg_values[key]:
                        emotion_avg = (float(row[key + ' ' + subkey]) + my_mind[key][subkey]) / 2
                        distances[row['sentiment']] += abs(emotion_avg - my_yearning[key][subkey])

    # Sort the emotions by their distances to my_yearning using the quicksort algorithm
    sorted_emotions = sorted(distances.items(), key=lambda x: x[1])

    # Find the emotion with the closest numerical values to my_yearning
    closest_emotion = sorted_emotions[0][0]

    return closest_emotion
