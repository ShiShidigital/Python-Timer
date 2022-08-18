# Timer Program for 1 Week Challange
# Version 1.1
import time # import time module for time.sleep() function
import winsound # import winsound module for the beep
import re   # import regex module to find patterns in text

print('\n', '-' * 5, 'The Timer', '-' * 5)

print('''
This Timer will count down the time and alert you when the time is up.
First you need to give the Minutes you want the Timer to last.
Then you can start the Timer.
You can change the Timer or repeat the current Timer.
''')


def countdown(timer):     #countdown() function, needs seconds as input for now

    while timer > 0:      # while seconds are more than 0
        hours, minutes = divmod(timer, 3600)
        mins, seconds = divmod(minutes, 60) # return (minutes, seconds) touple (before, after) the comma after division

        print('{:>5}{:002d}:{:02d}:{:02d}'.format(' ', hours, mins, seconds), end='\r')   # print number in time format in same line with indent
        time.sleep(1)       # make the program wait 1 second
        timer -= 1        # substract 1 from seconds

    print('{:>5}{:002d}:{:02d}:{:02d}'.format(' ', 0, 0, 0), end='\r')
    print('\n *** Time is up! *** \n')    # print something when while-loop reaches 0
    winsound.Beep(540, 1000)    #   makes a beep sound (frecuency, duration)


def get_time():     #function to get time from user
    while True: # start while loop
        pattern = r"(\d+:\d+:\d+)"  # regex, \d+ = one or more numbers, : = literal colone

        try:
            user_input = input("Set up Timer (hh:mm:ss) > ")    # let user put in timer
            m = re.match(pattern, user_input)   # find pattern in user_input

            if m is not None:   # if m is not None, so it found the pattern
                user_timer = user_input.split(':')  # split on colone, make list
                return user_timer   # return user_timer, end function

            else:   # Tell the user what went wrong.
                print('''
The input needs to be in exactly this format ==> hh:mm:ss
Only whole positive numbers are allowed. \n''')

        except:
            print('Except: The input needs to be in this format: hh:mm:ss ')
            continue


def runtime(user_timer):  # Inform user what will happen with the input
    user_hrs = user_timer[0]    # get first object in user_timer list
    user_min = user_timer[1]
    user_sec = user_timer[2]

    print('\n --- The Timer will run for {} hours {} minutes and {} seconds. ---\n'.format(user_hrs, user_min, user_sec)) # print out what happens next


user_timer = get_time()   # get minutes after start of program
runtime(user_timer)       # show what will happen with the user input

while True:
    try:
        user_input = int(input('Start this Timer now(1), choose other time(2) or end the program(3)? > ')) #simple menu

        if user_input == 1:
            print('Starting Timer...\n')

            timer = int(user_timer[0]) * 3600 + int(user_timer[1]) * 60 + int(user_timer[2])   # turn hours and minutes into seconds
            countdown(timer)  # call function countdown with seconds

        elif user_input == 2:
            print('Choose a new time...\n')

            user_timer = get_time()
            runtime(user_timer)

        elif user_input == 3:   # Break out of while loop and end program
            print('Exit program')
            break

        else:
            print('Please choose another number\n')

    except:     #error handling
        print('Please choose from 1, 2 or 3. All other inputs are invalid.\n')
        continue


input() # so i can see the result, stops program from closing
