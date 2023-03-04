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
import BotEmodex
from BotEmodex import bot_heart
from BotEmodex import bot_other
from BotEmodex import bot_yearning
from BotEmodex import bot_other_yearning
from BotEmodex import bot_empathy
import csv
from collections import defaultdict

def analyze_emotions(bot_heart, bot_other, bot_yearning, bot_other_yearning):
    # Calculate the averages
    avg1 = {}
    for key in bot_heart.keys():
        avg1[key] = (bot_other[key] + bot_heart[key]) / 2

    avg2 = {}
    for key in bot_yearning.keys():
        avg2[key] = (bot_other_yearning[key] + bot_yearning[key]) / 2

    # Load the CSV file and calculate the distances
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
                distance1 = 0
                distance2 = 0
                for key in avg1.keys():
                    if key in row.keys():
                        distance1 += abs(float(row[key]) - avg1[key])
                    if key + '_discomfort' in row.keys():
                        distance1 += abs(float(row[key + '_discomfort']) - avg1[key])

                for key in avg2.keys():
                    if key in row.keys():
                        distance2 += abs(float(row[key]) - avg2[key])
                    if key + '_discomfort' in row.keys():
                        distance2 += abs(float(row[key + '_discomfort']) - avg2[key])

                discomfort_score = sum(float(row[key]) for key in row.keys() if ' discomfort' in key)

                if discomfort_score <= 1:
                    distance = abs(distance1 - distance2)
                    distances[row['sentiment']] += distance

                    discomfort_scores[row['sentiment']] += discomfort_score

    # Filter out sentiments with a discomfort score of 2 or higher
    filtered_emotions = {}
    for emotion in distances.keys():
        if discomfort_scores[emotion] <= 1:
            filtered_emotions[emotion] = distances[emotion]

    # Sort the remaining emotions by their distances to the averages
    sorted_emotions = sorted(filtered_emotions.items(), key=lambda x: x[1])

    # Find the sentiment that is closest to the averages
    for emotion, _ in sorted_emotions:
        if discomfort_scores[emotion] <= 1:
            return emotion

    return 'neutral' if not sorted_emotions else sorted_emotions[0][0]


#how to run the code:
 # Call the analyze_emotions function with your input variables
#result = analyze_emotions(bot_heart, bot_other, bot_yearning, bot_other_yearning)

 # Print the result
#print(result)
