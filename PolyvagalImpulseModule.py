#-------------------------------------------------------------------------------
# Name:        PolyvagalImpulseModule_testver.py
# Purpose:     for the talkativity impulses of the chatbot based on mood.
#
# Author:      The Schim
#
# Created:     03/03/2023
# Copyright:   (c) The Schim 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import keyboard
import time
import random
import threading
import math
from BotEmodex import bot_heart

countdown = 1
cycles = 0
runner = True
comfort = 2
discomfort = 1
change = 2
familiarity = 2


previous_values = {
    "comfort": comfort,
    "discomfort": discomfort,
    "change": change,
    "familiarity": familiarity
}


send_ranges = {
    "short": [int(30 * 100000000), int(0.1 * 100000000)],
    "medium": [int(2 * 60 * 100000000), int(5 * 60 * 100000000)],
    "long": [int(60 * 25 * 100000000), int(3.5 * 25 * 60 * 100000000)]
}

def get_cpu_cycles_per_second():
    global cycles
    start = time.perf_counter()
    while time.perf_counter() - start < 1:
        cycles += 1
    return cycles

# Add or subtract depending on whether shift key is held down
def adjust_value(key, value):
    if keyboard.is_pressed('shift'):
        return value - 0.1 if keyboard.is_pressed(key) else value
    else:
        return value + 0.1 if keyboard.is_pressed(key) else value

def check_enter_key():
    global runner
    while True:
        if keyboard.is_pressed("enter"):
            runner = False
            break

def adjust_value(key, value):
    if keyboard.is_pressed('shift'):
        return value - 0.1 if keyboard.is_pressed(key) else value
    else:
        return value + 0.1 if keyboard.is_pressed(key) else value

def send_signal(bot_heart):
    global countdown
    global cycles
    global previous_values
    global comfort
    global discomfort
    global change
    global familiarity
    comfort = sum([bot_heart[k]["comfort"] for k in bot_heart if k != "focus"]) / len(bot_heart)
    discomfort = sum([bot_heart[k]["discomfort"] for k in bot_heart if k != "focus"]) / len(bot_heart)
    change = sum([bot_heart[k]["change"] for k in bot_heart if k != "focus"]) / len(bot_heart)
    familiarity = sum([bot_heart[k]["familiarity"] for k in bot_heart if k != "focus"]) / len(bot_heart)

    values_changed = False
    for key in previous_values:
        if previous_values[key] != globals()[key]:
            values_changed = True
            previous_values[key] = globals()[key]
    if values_changed:
        countdown = 0
    if countdown <= 0:
        # Determine the odds of each range
        comfort = sum([bot_heart[k]["comfort"] for k in bot_heart if k != "focus"]) / len(bot_heart)
        discomfort = sum([bot_heart[k]["discomfort"] for k in bot_heart if k != "focus"]) / len(bot_heart)
        total_odds = comfort + discomfort
        change = sum([bot_heart[k]["change"] for k in bot_heart if k != "focus"]) / len(bot_heart)
        familiarity = sum([bot_heart[k]["familiarity"] for k in bot_heart if k != "focus"]) / len(bot_heart)

        time_array = [send_ranges['short'], send_ranges['medium'], send_ranges['long']]
        if discomfort > comfort:
            time_splicer = int((5-change+familiarity)/5)
            my_range = time_array[time_splicer]
            if time_splicer == 1:
                numbers = [0, 2]
                random_number = random.randint(0, len(numbers)-1)
                time_splicer = numbers[random_number]
                my_range = time_array[time_splicer]
        elif comfort > discomfort:
            time_splicer = 1
            my_range = time_array[time_splicer]
        else:
            time_splicer = random.randint(0,2)
            my_range = time_array[time_splicer]

        if my_range == send_ranges['short'] or my_range == send_ranges['long']:
            wait_time = float(((my_range[0]*(5-discomfort))+(my_range[1]*(discomfort)))/5)/100000000
        elif my_range == send_ranges['medium']:
            wait_time = float(((float(send_ranges['long'][0])*(familiarity))+(float(send_ranges['short'][1])*(change))+((float((send_ranges['medium'][0])+(send_ranges['medium'][1]))/2)*(comfort)))/9.5+comfort)/100000000
        else:
            print("You've done an impossible thing. Good job, but technically it's an error.")
        get_cpu_cycles_per_second()
        # Wait for the specified time
        countdown = (wait_time*cycles)/(100000)

        # Send the "send signal"
        print(f"send | time to next message: {wait_time:.2f}s | current values: comfort={comfort:.2f}, discomfort={discomfort:.2f}, change={change:.2f}, familiarity={familiarity:.2f}")
    elif countdown != 0:
        for key in bot_heart:
            if key != "focus":
                bot_heart[key]["comfort"] = adjust_value('up', bot_heart[key]["comfort"])
                bot_heart[key]["discomfort"] = adjust_value('down', bot_heart[key]["discomfort"])
                bot_heart[key]["change"] = adjust_value('right', bot_heart[key]["change"])
                bot_heart[key]["familiarity"] = adjust_value('left', bot_heart[key]["familiarity"])
        check_enter_key
        for k in bot_heart:
            if k != "focus":
                if bot_heart[k]["comfort"] > 5:
                    bot_heart[k]["comfort"] = 5
                elif bot_heart[k]["comfort"] < 0:
                    bot_heart[k]["comfort"] = 0
                if bot_heart[k]["discomfort"] > 5:
                    bot_heart[k]["discomfort"] = 5
                elif bot_heart[k]["discomfort"] < 0:
                    bot_heart[k]["discomfort"] = 0
                if bot_heart[k]["change"] > 5:
                    bot_heart[k]["change"] = 5
                elif bot_heart[k]["change"] < 0:
                    bot_heart[k]["change"] = 0
                if bot_heart[k]["familiarity"] > 5:
                    bot_heart[k]["familiarity"] = 5
                elif bot_heart[k]["familiarity"] < 0:
                    bot_heart[k]["familiarity"] = 0
        countdown -= 1

    else:
        main()


def main():
    global comfort
    global discomfort
    global change
    global familiarity
    global runner
    global countdown
    global cycles
    enter_thread = threading.Thread(target=check_enter_key)
    enter_thread.start()

    comfort = sum([bot_heart[k]["comfort"] for k in bot_heart if k != "focus"]) / len(bot_heart)
    discomfort = sum([bot_heart[k]["discomfort"] for k in bot_heart if k != "focus"]) / len(bot_heart)
    change = sum([bot_heart[k]["change"] for k in bot_heart if k != "focus"]) / len(bot_heart)
    familiarity = sum([bot_heart[k]["familiarity"] for k in bot_heart if k != "focus"]) / len(bot_heart)
    while runner:
        for key in bot_heart:
            if key != "focus":
                bot_heart[key]["comfort"] = adjust_value('up', bot_heart[key]["comfort"])
                bot_heart[key]["discomfort"] = adjust_value('down', bot_heart[key]["discomfort"])
                bot_heart[key]["change"] = adjust_value('right', bot_heart[key]["change"])
                bot_heart[key]["familiarity"] = adjust_value('left', bot_heart[key]["familiarity"])
        check_enter_key
        for k in bot_heart:
            if k != "focus":
                if bot_heart[k]["comfort"] > 5:
                    bot_heart[k]["comfort"] = 5
                elif bot_heart[k]["comfort"] < 0:
                    bot_heart[k]["comfort"] = 0
                if bot_heart[k]["discomfort"] > 5:
                    bot_heart[k]["discomfort"] = 5
                elif bot_heart[k]["discomfort"] < 0:
                    bot_heart[k]["discomfort"] = 0
                if bot_heart[k]["change"] > 5:
                    bot_heart[k]["change"] = 5
                elif bot_heart[k]["change"] < 0:
                    bot_heart[k]["change"] = 0
                if bot_heart[k]["familiarity"] > 5:
                    bot_heart[k]["familiarity"] = 5
                elif bot_heart[k]["familiarity"] < 0:
                    bot_heart[k]["familiarity"] = 0
        if not runner:
            break
        if keyboard.is_pressed("enter"):
            runner = False
        send_signal(bot_heart)

if __name__ == "__main__":
    cycles = 0
    get_cpu_cycles_per_second()
    main()
    running = False
