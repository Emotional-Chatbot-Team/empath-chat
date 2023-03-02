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
    discomfort_scores = defaultdict(float)
    distances = defaultdict(float)
    with open('GrowingEmotions.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            valid_sentiment = True
            for subkey in row.keys():
                if 'discomfort' in subkey:
                    if float(row[subkey]) >= 2:
                        valid_sentiment = False
                    if subkey.endswith(' discomfort') and float(row[subkey]) > 1:
                        valid_sentiment = False
            if valid_sentiment:
                for key in shared_keys:
                    for subkey in my_yearning[key]:
                        if subkey in avg_values[key]:
                            emotion_avg = (float(row[key + ' ' + subkey]) + my_mind[key][subkey]) / 2
                            distance = abs(emotion_avg - my_yearning[key][subkey])
                            distances[row['sentiment']] += distance

                    discomfort_subkeys = [k for k in row.keys() if ' discomfort' in k]
                    for subkey in discomfort_subkeys:
                        discomfort_scores[row['sentiment']] += float(row[subkey])

    # Filter out sentiments with a discomfort score of 2 or higher
    filtered_emotions = {}
    for emotion in distances.keys():
        if discomfort_scores[emotion] <= 1:
            filtered_emotions[emotion] = distances[emotion]

    # Sort the remaining emotions by their distances to my_yearning using the quicksort algorithm
    sorted_emotions = sorted(filtered_emotions.items(), key=lambda x: x[1])

    # Find the sentiment that is closest to my_yearning
    for emotion, _ in sorted_emotions:
        if discomfort_scores[emotion] <= 1:
            return emotion

    return 'neutral' if not sorted_emotions else sorted_emotions[0][0]


#how to run the code:
    #result = analyze_emotions(my_mind, my_yearning)
    #print(result)

