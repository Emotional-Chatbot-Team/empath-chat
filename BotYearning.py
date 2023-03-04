#-------------------------------------------------------------------------------
# Name:        BotYearning.py
# Purpose: giving the bot a driving motive.
#
# Author:      The Schim
#
# Created:     03/03/2023
# Copyright:   (c) The Schim 2023
# Licence:     <the bot to want its licence>
#-------------------------------------------------------------------------------
import BotEmodex
from BotEmodex import bot_yearning

def set_yearning_value(key, subkey, value):
    if key in bot_yearning and subkey in bot_yearning[key]:
        if isinstance(value, float) and 0 <= value <= 4:
            bot_yearning[key][subkey] = value
        else:
            print("Error: Invalid value. Please enter an integer between 0 and 4.")
    else:
        print("Error: Invalid key or subkey.")

print("Please answer the following questions to figure out how you want to feel:")
set_yearning_value("emotions", "comfort", float(input("How comfortable do you want the bot to want its emotions to be on a scale of 0 to 4? ")))
set_yearning_value("emotions", "familiarity", float(input("How familiar do you want the bot to want its emotions to be on a scale of 0 to 4? ")))
set_yearning_value("emotions", "change", float(input("How changing or dynamic do you want the bot to want its emotions to be on a scale of 0 to 4? ")))
set_yearning_value("body", "comfort", float(input("How comfortable do you want the bot to want its body to be on a scale of 0 to 4? ")))
set_yearning_value("body", "familiarity", float(input("How familiar do you want the bot to want its bodily sensations to be on a scale of 0 to 4? ")))
set_yearning_value("body", "change", float(input("How changing or dynamic do you want the bot to want its bodily sensations to be on a scale of 0 to 4? ")))
set_yearning_value("environment", "comfort", float(input("How comfortable do you want the bot to want its current environment to be on a scale of 0 to 4? ")))
set_yearning_value("environment", "familiarity", float(input("How familiar do you want the bot to want its environment to be on a scale of 0 to 4? ")))
set_yearning_value("environment", "change", float(input("How changing or dynamic do you want the bot to want its environment to be on a scale of 0 to 4? ")))
set_yearning_value("intentions", "comfort", float(input("How comfortable do you want the bot to want its intentions to be on a scale of 0 to 4? ")))
set_yearning_value("intentions", "familiarity", float(input("How familiar or familiarity-seeking do you want the bot to want its intentions to be on a scale of 0 to 4? ")))
set_yearning_value("intentions", "change", float(input("How changing or dynamic do you want the bot to want its intentions to be on a scale of 0 to 4? ")))
set_yearning_value("the_other", "comfort", float(input("How comfortable do you want 'the other' to make you on a scale of 0 to 4? ")))
set_yearning_value("the_other", "familiarity", float(input("How familiar do you want 'the other' to be on a scale of 0 to 4? ")))
set_yearning_value("the_other", "change", float(input("How changing or dynamic do you want 'the other' to be on a scale of 0 to 4? ")))
set_yearning_value("social_group", "comfort", float(input("How comfortable do you want the bot to want its social group to be on a scale of 0 to 4? ")))
set_yearning_value("social_group", "familiarity", float(input("How familiar do you want the bot to want its social group to be on a scale of 0 to 4? ")))
set_yearning_value("social_group", "change", float(input("How changing or dynamic do you want the bot to want its social group to be on a scale of 0 to 4? ")))
focus_on_emotions = float(input("write '1' if you want to be focused to be on maintaining or changing the bot to want its  emotions, or else write '0'. "))
focus_on_body = float(input("write '1' if you want to be focused to be on maintaining or changing how the bot to want its  body feels, or else write '0'. "))
focus_on_environment = float(input("write '1' if you want to be focused to be on maintaining or changing the bot to want its  environment, or else write '0'. "))
focus_on_intentions = float(input("write '1' if you want to be focused on maintaining or changing the bot to want its  intentions, or else write '0'. "))
focus_on_social_group = float(input("write '1' if you want to be focused on maintaining or changing the bot to want its social place, or else write '0'. "))

#test the function
set_all_yearning_values()
