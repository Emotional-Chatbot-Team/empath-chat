#-------------------------------------------------------------------------------
# Name:        BotEmodex.py
# Purpose: setting the bot's emotions and goals
#
# Author:      The Schim
#
# Created:     03/03/2023
# Copyright:   (c) The Schim 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

bot_heart = {
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


bot_empathy = {
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


bot_other = {
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
        if isinstance(value, float) and 0 <= value <= 5:
            my_heart[key][subkey] = value
        elif key == "focus" and subkey in my_heart[key] and isinstance(value, int) and 0 <= value <= 1:
            my_heart[key][subkey] = value
        else:
            print("Error: Invalid value. Please enter an integer between 0 and 5, or between 0 and 1 for focus.")
    else:
        print("Error: Invalid key or subkey.")

def set_bot_other(bot_other, key, subkey, value):
    if key in my_other and subkey in my_other[key]:
        if isinstance(value, float) and 0 <= value <= 5:
            my_other[key][subkey] = value
        elif key == "focus" and subkey in my_other[key] and isinstance(value, float) and 0 <= value <= 1:
            my_other[key][subkey] = value
        else:
            print("Error: Invalid value. Please enter an float between 0 and 5, or between 0 and 1 for focus.")
    else:
        print("Error: Invalid key or subkey.")

def calculate_empathy(bot_heart, bot_other):
    empathy = {
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

    for key in bot_heart:
        for subkey in bot_heart[key]:
            if key in bot_other and subkey in bot_other[key]:
                empathy[key][subkey] = (bot_heart[key][subkey] + bot_other[key][subkey]) / 2

    for key in empathy["focus"]:
        if key in ["emotions", "body", "environment", "intentions", "the_other", "social_group"]:
            empathy["focus"][key] = int(bot_other[key][subkey] and bot_heart[key][subkey])
        else:
            empathy["focus"][key] = int(bot_other[key] and bot_heart[key][subkey])

    return empathy


bot_yearning = {
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


bot_other_yearning = {
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


