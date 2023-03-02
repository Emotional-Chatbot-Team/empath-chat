#-------------------------------------------------------------------------------
# Name:        emotional database manager
# Purpose:
#
# Author:      The Schim
#
# Created:     27/02/2023
# Copyright:   (c) The Schim 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import Emotional_lesson
import csv

def add_new_emotion():
    emotion_name = input("Enter the name of the new emotion: ")
    emotion_example_1 = input("Enter an example of something that causes this emotion: ")
    emotion_example_2 = input("Enter another example of something that causes this emotion: ")
    while True:
        try:
            emotion_values = []
            emotion_values.append(emotion_name)
            emotion_values.append(input("How comfortable are your emotions on a scale of 0 to 4? "))
            emotion_values.append(input("How familiar are your emotions on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how changing or dynamic are your emotions on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how uncomfortable are your emotions on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how comfortable is your body on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how familiar are your bodily sensations on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how changing or dynamic are your bodily sensations on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how uncomfortable is your body on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how comfortable is your current environment on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how familiar is your environment on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how changing or dynamic is your environment on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how uncomfortable is your environment on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how comfortable are your intentions on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how familiar or familiarity-seeking are your intentions on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how changing or dynamic are your intentions on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how uncomfortable are your intentions on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how comfortable does the other make you on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how familiar is the other on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how changing or dynamic is the other on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how uncomfortable does the other make you on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how comfortable is your social group on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how familiar is your social group on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how changing or dynamic is your social group on a scale of 0 to 4? "))
            emotion_values.append(input("When you are feeling this way how uncomfortable is your social group on a scale of 0 to 4? "))
            emotion_values.append(input("Write '1' if you are focused on maintaining or changing your emotions, or else write '0': "))
            emotion_values.append(input("Write '1' if you are focused on maintaining or changing how your body feels, or else write '0': "))
            emotion_values.append(input("Write '1' if you are focused on maintaining or changing your environment, or else write '0': "))
            emotion_values.append(input("Write '1' if you are focused on maintaining or changing your intentions, or else write '0': "))
            emotion_values.append(input("Write '1' if you are focused on maintaining or changing your interaction with others, or else write '0': "))
            emotion_values.append(input("Write '1' if you are focused on maintaining or changing your social environment, or else write '0': "))

            # Open the CSV file for appending
            with open('emotions.csv', mode='a', newline='') as emotions_file:
                fieldnames = ['sentiment', 'emotion comfort', 'emotion familiarity', 'emotion dynamism',
                              'emotion discomfort', 'body comfort', 'body familiarity', 'body dynamism',
                              'body discomfort', 'environment comfort', 'environment familiarity',
                              'environment dynamism', 'environment discomfort', 'intention comfort',
                              'intention familiarity', 'intention dynamism', 'intention discomfort',
                              'other comfort', 'other familiarity', 'other dynamism', 'other discomfort',
                              'social comfort', 'social familiarity', 'social dynamism', 'social discomfort',
                              'focus on emotion', 'focus on body', 'focus on environment', 'focus on intention',
                              'focus on other', 'focus on social place']
                csv_writer = csv.DictWriter(emotions_file, fieldnames=fieldnames)

                # Check if emotion name already exists
                existing_emotions = []
                existing_emotion_values = []
                emotions_file.seek(0)  # Reset the file reader to the beginning of the file
                csv_reader = csv.DictReader(emotions_file)
                for row in csv_reader:
                    existing_emotions.append(row['sentiment'])
                    existing_emotion_values.append([row['emotion comfort'], row['emotion familiarity'], row['emotion dynamism'], row['emotion discomfort'],
                                                    row['body comfort'], row['body familiarity'], row['body dynamism'], row['body discomfort'],
                                                    row['environment comfort'], row['environment familiarity'], row['environment dynamism'], row['environment discomfort'],
                                                    row['intention comfort'], row['intention familiarity'], row['intention dynamism'], row['intention discomfort'],
                                                    row['other comfort'], row['other familiarity'], row['other dynamism'], row['other discomfort'],
                                                    row['social comfort'], row['social familiarity'], row['social dynamism'], row['social discomfort'],
                                                    row['focus on emotion'], row['focus on body'], row['focus on environment'], row['focus on intention'],
                                                    row['focus on other'], row['focus on social place']])
                new_emotion_values = [emotion_name] + emotion_values[1:]
                if new_emotion_values in existing_emotion_values:
                    # Update the existing emotion name to match the new emotion name
                    row_index = existing_emotion_values.index(new_emotion_values)
                    row = csv_reader[row_index]
                    row['sentiment'] = emotion_name
                else:
                    if emotion_name in existing_emotions:
                        if input("An emotion with this name already exists. Would you like to change the name associated with the existing values or update the existing values to match the new emotion? (enter 'change' or 'update'): ") == 'change':
                            emotion_name = input("Enter a new name for your emotion: ")
                        else:
                            # Update the existing values to match the new emotion
                            emotions_file.seek(0)  # Reset the file reader to the beginning of the file
                            for row in csv_reader:
                                if row['sentiment'] == emotion_name:
                                    row['emotion comfort'] = emotion_values[1]
                                    row['emotion familiarity'] = emotion_values[2]
                                    row['emotion dynamism'] = emotion_values[3]
                                    row['emotion discomfort'] = emotion_values[4]
                                    row['body comfort'] = emotion_values[5]
                                    row['body familiarity'] = emotion_values[6]
                                    row['body dynamism'] = emotion_values[7]
                                    row['body discomfort'] = emotion_values[8]
                                    row['environment comfort'] = emotion_values[9]
                                    row['environment familiarity'] = emotion_values[10]
                                    row['environment dynamism'] = emotion_values[11]
                                    row['environment discomfort'] = emotion_values[12]
                                    row['intention comfort'] = emotion_values[13]
                                    row['intention familiarity'] = emotion_values[14]
                                    row['intention dynamism'] = emotion_values[15]
                                    row['intention discomfort'] = emotion_values[16]
                                    row['other comfort'] = emotion_values[17]
                                    row['other familiarity'] = emotion_values[18]
                                    row['other dynamism'] = emotion_values[19]
                                    row['other discomfort'] = emotion_values[20]
                                    row['social comfort'] = emotion_values[21]
                                    row['social familiarity'] = emotion_values[22]
                                    row['social dynamism'] = emotion_values[23]
                                    row['social discomfort'] = emotion_values[24]
                                    row['focus on emotion'] = emotion_values[25]
                                    row['focus on body'] = emotion_values[26]
                                    row['focus on environment'] = emotion_values[27]
                                    row['focus on intention'] = emotion_values[28]
                                    row['focus on other'] = emotion_values[29]
                                    row['focus on social place'] = emotion_values[30]
                                    break
                            else:
                                # Append the new emotion to the CSV file
                                csv_writer.writerow({'sentiment': emotion_name, 'emotion comfort': emotion_values[1], 'emotion familiarity': emotion_values[2],
                                'emotion dynamism': emotion_values[3], 'emotion discomfort': emotion_values[4],
                                'body comfort': emotion_values[5], 'body familiarity': emotion_values[6],
                                'body dynamism': emotion_values[7], 'body discomfort': emotion_values[8],
                                'environment comfort': emotion_values[9], 'environment familiarity': emotion_values[10],
                                'environment dynamism': emotion_values[11], 'environment discomfort': emotion_values[12],
                                'intention comfort': emotion_values[13], 'intention familiarity': emotion_values[14],
                                'intention dynamism': emotion_values[15], 'intention discomfort': emotion_values[16],
                                'other comfort': emotion_values[17], 'other familiarity': emotion_values[18],
                                'other dynamism': emotion_values[19], 'other discomfort': emotion_values[20],
                                'social comfort': emotion_values[21], 'social familiarity': emotion_values[22],
                                'social dynamism': emotion_values[23], 'social discomfort': emotion_values[24],
                                'focus on emotion': emotion_values[25], 'focus on body': emotion_values[26],
                                'focus on environment': emotion_values[27], 'focus on intention': emotion_values[28],
                                'focus on other': emotion_values[29], 'focus on social place': emotion_values[30]})
            return emotion_name, emotion_example_1, emotion_example_2
        except Exception as e:
            print("An unknowable eldritch error has occurred:", e)