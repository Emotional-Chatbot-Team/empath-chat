#-------------------------------------------------------------------------------
# Name:        Empathy Dictionary
# Purpose: a simple system to be used with an emotional context recognition AI to drive conversations.
#
# Author:      The Schim
#
# Created:     27/02/2023
# Copyright:   (c) The Schim 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

my_heart = {
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


my_mind = {
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


my_other = {
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

def set_heart(my_heart, key, subkey, value):
    if key in my_heart and subkey in my_heart[key]:
        if isinstance(value, int) and 0 <= value <= 5:
            my_heart[key][subkey] = value
        elif key == "focus" and subkey in my_heart[key] and isinstance(value, int) and 0 <= value <= 1:
            my_heart[key][subkey] = value
        else:
            print("Error: Invalid value. Please enter an integer between 0 and 5, or between 0 and 1 for focus.")
    else:
        print("Error: Invalid key or subkey.")

def set_other(my_other, key, subkey, value):
    if key in my_other and subkey in my_other[key]:
        if isinstance(value, int) and 0 <= value <= 5:
            my_other[key][subkey] = value
        elif key == "focus" and subkey in my_other[key] and isinstance(value, int) and 0 <= value <= 1:
            my_other[key][subkey] = value
        else:
            print("Error: Invalid value. Please enter an integer between 0 and 5, or between 0 and 1 for focus.")
    else:
        print("Error: Invalid key or subkey.")

def calculate_mind(my_heart, my_other):
    mind = {
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

    for key in my_heart:
        for subkey in my_heart[key]:
            if key in my_other and subkey in my_other[key]:
                mind[key][subkey] = (my_heart[key][subkey] + my_other[key][subkey]) / 2

    for key in mind["focus"]:
        if key in ["emotions", "body", "environment", "intentions", "the_other", "social_group"]:
            mind["focus"][key] = int(my_other[key][subkey] and my_heart[key][subkey])
        else:
            mind["focus"][key] = int(my_other[key] and my_heart[key][subkey])

    return mind


my_yearning = {
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


