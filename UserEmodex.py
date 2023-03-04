#-------------------------------------------------------------------------------
# Name:        UserEmodex.py
# Purpose: determining the user's emotions and goals
#
# Author:      The Schim
#
# Created:     03/03/2023
# Copyright:   (c) The Schim 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# user_heart.py

user_heart = {
    "emotions": {
        "comfort": 0,
        "familiarity": 0,
        "change": 0,
        "discomfort": 0
    },
    "body": {
        "comfort": 0,
        "familiarity": 0,
        "change": 0,
        "discomfort": 0
    },
    "environment": {
        "comfort": 0,
        "familiarity": 0,
        "change": 0,
        "discomfort": 0
    },
    "intentions": {
        "comfort": 0,
        "familiarity": 0,
        "change": 0,
        "discomfort": 0
    },
    "the_other": {
        "comfort": 0,
        "familiarity": 0,
        "change": 0,
        "discomfort": 0
    },
    "social_group": {
        "comfort": 0,
        "familiarity": 0,
        "change": 0,
        "discomfort": 0
    },
    "focus": {
        "emotions": 0,
        "body": 0,
        "environment": 0,
        "intentions": 0,
        "the_other": 0,
        "social_group": 0
    }
}

def set_heart(user_heart, key, subkey, value):
    if key in user_heart and subkey in user_heart[key]:
        if isinstance(value, int) and 0 <= value <= 5:
            user_heart[key][subkey] = value
        elif key == "focus" and subkey in user_heart[key] and isinstance(value, int) and 0 <= value <= 1:
            user_heart[key][subkey] = value
        else:
            print("Error: Invalid value. Please enter an integer between 0 and 5, or between 0 and 1 for focus.")
    else:
        print("Error: Invalid key or subkey.")


# user_yearning.py

user_yearning = {
    "emotions": {
        "comfort": 0,
        "familiarity": 0,
        "change": 0
    },
    "body": {
        "comfort": 0,
        "familiarity": 0,
        "change": 0
    },
    "environment": {
        "comfort": 0,
        "familiarity": 0,
        "change": 0
    },
    "intentions": {
        "comfort": 0,
        "familiarity": 0,
        "change": 0
    },
    "the_other": {
        "comfort": 0,
        "familiarity": 0,
        "change": 0
    },
    "social_group": {
        "comfort": 0,
        "familiarity": 0,
        "change": 0
    },
    "focus": {
        "emotions": 0,
        "body": 0,
        "environment": 0,
        "intentions": 0,
        "social_group": 0
    }
}

def set_user_yearning(key, subkey, value):
    if key in user_yearning and subkey in user_yearning[key]:
        if isinstance(value, int) and 0 <= value <= 5:
            user_yearning[key][subkey] = value
        else:
            print("Error: Invalid value. Please enter an integer between 0 and 5.")
    else:
        print("Error: Invalid key or subkey.")
