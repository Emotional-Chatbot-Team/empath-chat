#-------------------------------------------------------------------------------
# Name:        Feedback
# Purpose: For Letting the Robot know when they goofed up
#
# Author:      The Schim
#
# Created:     27/02/2023
# Copyright:   (c) The Schim 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import Emodex

def feedback():
    feedback_sent = False

    while not feedback_sent:
        # Prompt user for feedback and update my_other dictionary
        set_other_value("emotions", "comfort", int(input("How comfortable did this make your emotions on a scale of 0 to 4? ")))
        set_other_value("emotions", "change", int(input("How changing or dynamic did this feel on a scale of 0 to 4? ")))
        set_other_value("emotions", "discomfort", int(input("How uncomfortable did this make you on a scale of 0 to 4? ")))
        set_other_value("body", "comfort", int(input("How comfortable did this make you feel about your body on a scale of 0 to 4? ")))
        set_other_value("body", "change", int(input("How changing or dynamic did this make your bodily sensations on a scale of 0 to 4? ")))
        set_other_value("body", "discomfort", int(input("How uncomfortable did this make your body on a scale of 0 to 4? ")))
        set_other_value("environment", "comfort", int(input("How comfortable did this make you feel about your environment on a scale of 0 to 4? ")))
        set_other_value("environment", "change", int(input("How changing or dynamic did this make your environment on a scale of 0 to 4? ")))
        set_other_value("environment", "discomfort", int(input("How uncomfortable did this make your environment on a scale of 0 to 4? ")))
        set_other_value("intentions", "comfort", int(input("How comfortable did this make your intentions on a scale of 0 to 4? ")))
        set_other_value("intentions", "change", int(input("How changing or dynamic did this inspire your intentions to be on a scale of 0 to 4? ")))
        set_other_value("intentions", "discomfort", int(input("How uncomfortable did this make your intentions on a scale of 0 to 4? ")))
        set_other_value("the_other", "comfort", int(input("How comfortable did this make you feel about me on a scale of 0 to 4? ")))
        set_other_value("the_other", "change", int(input("How changing or dynamic did this make me seem on a scale of 0 to 4? ")))
        set_other_value("the_other", "discomfort", int(input("How uncomfortable about me did this make you feel on a scale of 0 to 4? ")))
        set_other_value("social_group", "comfort", int(input("How comfortable did this make your social group feel on a scale of 0 to 4? ")))
        set_other_value("social_group", "change", int(input("How dynamic did this make your social group feel on a scale of 0 to 4? ")))
        set_other_value("social_group", "discomfort", int(input("How uncomfortable did this make your social group on a scale of 0 to 4? ")))

        # Ask user if they want to send feedback or try again
        ans = input("Would you like to update your values based on feedback? (y/n) ")
        if ans.lower() == 'y':
            my_other = feedback()
            return my_other
        elif ans.lower() == 'n':
            print("Values not updated.")
            return my_other
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            return update_my_other()