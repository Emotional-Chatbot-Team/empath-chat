#-------------------------------------------------------------------------------
# Name:        Yearning set
# Purpose: setting the Yearning Value of the Emodex
#
# Author:      The Schim
#
# Created:     27/02/2023
# Copyright:   (c) The Schim 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import Emodex

def set_yearning_value(key, subkey, value):
    if key in my_yearning and subkey in my_yearning[key]:
        if isinstance(value, int) and 0 <= value <= 4:
            my_yearning[key][subkey] = value
        else:
            print("Error: Invalid value. Please enter an integer between 0 and 4.")
    else:
        print("Error: Invalid key or subkey.")

print("Please answer the following questions to figure out how you want to feel:")
set_yearning_value("emotions", "comfort", int(input("How comfortable do you want your emotions to be on a scale of 0 to 4? ")))
set_yearning_value("emotions", "familiarity", int(input("How familiar do you want your emotions to be on a scale of 0 to 4? ")))
set_yearning_value("emotions", "change", int(input("How changing or dynamic do you want your emotions to be on a scale of 0 to 4? ")))
set_yearning_value("body", "comfort", int(input("How comfortable do you want your body to be on a scale of 0 to 4? ")))
set_yearning_value("body", "familiarity", int(input("How familiar do you want your bodily sensations to be on a scale of 0 to 4? ")))
set_yearning_value("body", "change", int(input("How changing or dynamic do you want your bodily sensations to be on a scale of 0 to 4? ")))
set_yearning_value("environment", "comfort", int(input("How comfortable do you want your current environment to be on a scale of 0 to 4? ")))
set_yearning_value("environment", "familiarity", int(input("How familiar do you want your environment to be on a scale of 0 to 4? ")))
set_yearning_value("environment", "change", int(input("How changing or dynamic do you want your environment to be on a scale of 0 to 4? ")))
set_yearning_value("intentions", "comfort", int(input("How comfortable do you want your intentions to be on a scale of 0 to 4? ")))
set_yearning_value("intentions", "familiarity", int(input("How familiar or familiarity-seeking do you want your intentions to be on a scale of 0 to 4? ")))
set_yearning_value("intentions", "change", int(input("How changing or dynamic do you want your intentions to be on a scale of 0 to 4? ")))
set_yearning_value("the_other", "comfort", int(input("How comfortable do you want 'the other' to make you on a scale of 0 to 4? ")))
set_yearning_value("the_other", "familiarity", int(input("How familiar do you want 'the other' to be on a scale of 0 to 4? ")))
set_yearning_value("the_other", "change", int(input("How changing or dynamic do you want 'the other' to be on a scale of 0 to 4? ")))
set_yearning_value("social_group", "comfort", int(input("How comfortable do you want your social group to be on a scale of 0 to 4? ")))
set_yearning_value("social_group", "familiarity", int(input("How familiar do you want your social group to be on a scale of 0 to 4? ")))
set_yearning_value("social_group", "change", int(input("How changing or dynamic do you want your social group to be on a scale of 0 to 4? ")))
focus_on_emotions = int(input("write '1' if you want to be focused to be on maintaining or changing your  emotions, or else write '0'. "))
focus_on_body = int(input("write '1' if you want to be focused to be on maintaining or changing how your  body feels, or else write '0'. "))
focus_on_environment = int(input("write '1' if you want to be focused to be on maintaining or changing your  environment, or else write '0'. "))
focus_on_intentions = int(input("write '1' if you want to be focused on maintaining or changing your  intentions, or else write '0'. "))
focus_on_social_group = int(input("write '1' if you want to be focused on maintaining or changing your social place, or else write '0'. "))

#test the function
set_all_yearning_values()
