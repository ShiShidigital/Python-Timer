# Timer Program for 1 Week Challange
# Version 1
import time # import time module for time.sleep() function
import winsound # import winsound module for the beep

print('\n', '-' * 5, 'The Timer', '-' * 5)

print('''
This Timer will count down the time and alert you when the time is up.
First you need to give the Minutes you want the Timer to last.
Then you can start the Timer.
You can change the Timer or repeat the current Timer.
''')

def countdown(timer):     #countdown() function, needs seconds as input for now

    while timer > 0:      # while seconds are more than 0
        minutes, seconds = divmod(timer, 60) # return (minutes, seconds) touple (before, after) the comma after division
        print('{:>5}{:02d}:{:02d}'.format(' ', minutes, seconds), end='\r')   # print number in time format in same line
        time.sleep(1)       # make the program wait 1 second
        timer -= 1        # substract 1 from seconds

    print('{:>5}{:02d}:{:02d}'.format(' ', 0, 0), end='\r')
    print('\n *** Time is up! *** \n')    # print something when while-loop reaches 0
    winsound.Beep(540, 1000)    #   makes a beep sound (frecuency, duration)


def get_time():     #function to get time from user
    while True: # start while loop
        user_input = input("How many minutes shall the Timer run? > ")    # get minutes from user

        try:    #start try-except block
            user_minutes = int(user_input)   # turn string into integer

            if user_minutes < 0:
                print('Please choose a positive value.\n')
                continue    # stay in while loop

            return user_minutes

        except:
            print('Please give a positive whole number for the minutes!\n')
            continue    # stay in while loop


def runtime(user_minutes):  # Inform user what will happen with the input
    if user_minutes == 1:   # Choose minute or minutes for the print statement.
        str_min = 'minute'
    else:
        str_min = 'minutes'

    print('\n --- The Timer will run for {} {}. ---\n'.format(user_minutes, str_min)) # print out what happens next



user_minutes = get_time()   # get minutes after start of program
runtime(user_minutes)       # show what will happen with the user input

while True:
    try:
        user_input = int(input('Start this Timer now(1), choose other time(2) or end the program(3)? > ')) #simple menu

        if user_input == 1:
            print('Starting Timer...\n')

            timer = user_minutes * 60   # turn minutes into seconds
            countdown(timer)  # call function countdown with seconds

        elif user_input == 2:
            print('Choose a new time...\n')

            user_minutes = get_time()
            runtime(user_minutes)

        elif user_input == 3:   # Break out of while loop and end program
            print('Exit program')
            break

        else:
            print('Please choose another number\n')

    except:     #error handling
        print('Please choose from 1, 2 or 3. All other inputs are invalid.\n')
        continue


input() # so i can see the result, stops program from closing
