#-------------------------------------------------------------------------------
# Name:        New Emotions pass through
# Purpose: a dictionary variable for storing articles of emotion for learning new emotion.
#
# Author:      The Schim
#
# Created:     27/02/2023
# Copyright:   (c) The Schim 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def create_emotional_lesson():
    # Define the Emotional_Lesson dictionary
    Emotional_Lesson = {}

    # Define default example 1
    example1 = {}
    example1['sentiment'] = ''
    example1['words'] = ''
    Emotional_Lesson['example1'] = example1

    # Define default example 2
    example2 = {}
    example2['sentiment'] = ''
    example2['words'] = ''
    Emotional_Lesson['example2'] = example2

    return Emotional_Lesson

def update_emotional_lesson(Emotional_Lesson, sentiment, words, example_num):
    # Check that example_num is valid
    if example_num not in ['example1', 'example2']:
        print('Error: example_num must be "example1" or "example2"')
        return Emotional_Lesson

    # Check that the sentiment for example2 matches the sentiment for example1
    if example_num == 'example2' and sentiment != Emotional_Lesson['example1']['sentiment']:
        print('Error: New sentiment does not match existing sentiment for example1')
        return Emotional_Lesson

    # Update the Emotional_Lesson dictionary with the new sentiment and words
    Emotional_Lesson[example_num]['sentiment'] = sentiment
    Emotional_Lesson[example_num]['words'] = words

    return Emotional_Lesson
