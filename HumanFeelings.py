#-------------------------------------------------------------------------------
# Name:        User's Feelings
# Purpose: determining how the other aka the User feels
#
# Author:      The Schim
#
# Created:     27/02/2023
# Copyright:   (c) The Schim 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import Emodex

def set_other_value(key, subkey, value):
    if key in my_other and subkey in my_other[key]:
        if isinstance(value, int) and 0 <= value <= 4:
            my_other[key][subkey] = value
        else:
            print("Error: Invalid value. Please enter an integer between 0 and 4.")
    else:
        print("Error: Invalid key or subkey.")

print("Please answer the following questions to set your 'The Other' values:")
set_other_value("emotions", "comfort", int(input("How comfortable are your emotions on a scale of 0 to 4? ")))
set_other_value("emotions", "familiarity", int(input("How familiar are your emotions on a scale of 0 to 4? ")))
set_other_value("emotions", "change", int(input("How changing or dynamic are your emotions on a scale of 0 to 4? ")))
set_other_value("emotions", "discomfort", int(input("How uncomfortable are your emotions on a scale of 0 to 4? ")))
set_other_value("body", "comfort", int(input("How comfortable is your body on a scale of 0 to 4? ")))
set_other_value("body", "familiarity", int(input("How familiar are your bodily sensations on a scale of 0 to 4? ")))
set_other_value("body", "change", int(input("How changing or dynamic are your bodily sensations on a scale of 0 to 4? ")))
set_other_value("body", "discomfort", int(input("How uncomfortable is your body on a scale of 0 to 4? ")))
set_other_value("environment", "comfort", int(input("How comfortable is your current environment on a scale of 0 to 4? ")))
set_other_value("environment", "familiarity", int(input("How familiar is your environment on a scale of 0 to 4? ")))
set_other_value("environment", "change", int(input("How changing or dynamic is your environment on a scale of 0 to 4? ")))
set_other_value("environment", "discomfort", int(input("How uncomfortable is your environment on a scale of 0 to 4? ")))
set_other_value("intentions", "comfort", int(input("How comfortable are your intentions on a scale of 0 to 4? ")))
set_other_value("intentions", "familiarity", int(input("How familiar or familiarity-seeking are your intentions on a scale of 0 to 4? ")))
set_other_value("intentions", "change", int(input("How changing or dynamic are your intentions on a scale of 0 to 4? ")))
set_other_value("intentions", "discomfort", int(input("How uncomfortable are your intentions on a scale of 0 to 4? ")))
set_other_value("the_other", "comfort", int(input("How comfortable does The Other make you on a scale of 0 to 4? ")))
set_other_value("the_other", "familiarity", int(input("How familiar is The Other on a scale of 0 to 4? ")))
set_other_value("the_other", "change", int(input("How changing or dynamic is The Other on a scale of 0 to 4? ")))
set_other_value("the_other", "discomfort", int(input("How uncomfortable does The Other make you on a scale of 0 to 4? ")))
set_other_value("social_group", "comfort", int(input("How comfortable is your social group on a scale of 0 to 4? ")))
set_other_value("social_group", "familiarity", int(input("How familiar is your social group on a scale of 0 to 4? ")))
set_other_value("social_group", "change", int(input("How changing or dynamic is your social group on a scale of 0 to 4? ")))
set_other_value("social_group", "discomfort", int(input("How uncomfortable is your social group on a scale of 0 to 4? ")))

print("Please answer the following questions to determine your current focuses:")
set_focus_value("emotions", int(input("Write '1' if you are focused on maintaining or changing your emotions, or else write '0': ")))
set_focus_value("body", int(input("Write '1' if you are focused on maintaining or changing how your body feels, or else write '0': ")))
set_focus_value("environment", int(input("Write '1' if you are focused on maintaining or changing your environment, or else write '0': ")))
set_focus_value("intentions", int(input("Write '1' if you are focused on maintaining or changing your intentions, or else write '0': ")))
set_focus_value("the_other", int(input("Write '1' if you are focused on maintaining or changing The Other, or else write '0': ")))
set_focus_value("social_group", int(input("Write '1' if you are focused on maintaining or changing your social place, or else write '0': ")))