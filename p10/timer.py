# import the time module
import time


# def the countdown function
def countdown(t):
    while t:
        mins, secs = divmod(t,60)
        # mins = t// 60
        # secs = t% 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # time = f''
        print(timer)
        time.sleep(1)
        t -= 1

    print('Time over!')

t = int(input('Enter the time in seconds: '))

# function call
countdown(t)



