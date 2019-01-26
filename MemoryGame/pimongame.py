#importing necessary library
import RPi.GPIO as GPIO
import threading
import time
import random
import os
from time import sleep

# green, White, Yellow, RED
LIGHTS = [13, 26, 19, 6]    #in BCM mode
#GPIO Pin for button Press
#Corresponding button FOr Led As Above
BUTTONS = [17, 22, 27, 4]   #in BCM mode

# values you can change that affect game play
speed = 0.25
# Various flags used to signal game status
is_displaying_pattern = False
is_won_current_level = False
is_game_over = False
play = 0
# game state
current_level = 1
current_step_of_level = 0
#list for storing LED's pattern
pattern = []
flag = 0

#Function to initialize Gpio Pin and setting mode
def initialize_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LIGHTS, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(BUTTONS, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(5, GPIO.IN)
    GPIO.setup(9, GPIO.OUT)
    
#Function to check Whether sequence of button pressed is same as sequence of LED's glown
def verify_player_selection(channel):
    #print (channel)
    global current_step_of_level, current_level, is_won_current_level, is_game_over
    if not is_displaying_pattern and not is_won_current_level and not is_game_over:
        #Function to glow led For corresponding Switch
        flash_led_for_button(channel)
        if channel == BUTTONS[pattern[current_step_of_level]]:
            current_step_of_level += 1
            if current_step_of_level >= current_level:
                current_level += 1
                is_won_current_level = True
                current_score = current_level-1
                print("Your Current Score:------- %d"%current_score)
        else:
            is_game_over = True
            
def verify_player_auto():
    if(play):
        if GPIO.input(4) == False :
            GPIO.output(6,True)  ## Turn on Led
            time.sleep(.2)
            GPIO.output(6,False)
            verify_player_selection(4)
        if GPIO.input(27) == False :
            GPIO.output(19,True)  ## Turn on Led
            time.sleep(.2)
            GPIO.output(19,False)
            verify_player_selection(27)
        if GPIO.input(22) == False :
            GPIO.output(26,True)  ## Turn on Led
            time.sleep(.2)
            GPIO.output(26,False)
            verify_player_selection(22)
        if GPIO.input(17) == False :
            GPIO.output(13,True)  ## Turn on Led
            time.sleep(.2)
            GPIO.output(13,False)
            verify_player_selection(17)

            
#Function to glow LED For corresponding Button Press
def flash_led_for_button(button_channel):
    led = LIGHTS[BUTTONS.index(button_channel)]
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(led, GPIO.LOW)
#Function to define new Pattern for Led Where one more LED will Glow in comparision to previous state
def add_new_color_to_pattern():
    global is_won_current_level, current_step_of_level
    is_won_current_level = False
    current_step_of_level = 0
    #Emptying the pattern of LED's First
    pattern[:]=[]
    #Appending new Pattern
    for i in range(current_level):
        next_color = random.randint(0, 3)
        pattern.append(next_color)
#Function To display the pattern Of LED's Glown
def display_pattern_to_player():
    global is_displaying_pattern
    is_displaying_pattern = True
    #setting all LED to Off if they are previously Glown
    GPIO.output(LIGHTS, GPIO.LOW)
    for i in range(current_level):
        GPIO.output(LIGHTS[pattern[i]], GPIO.HIGH)
        time.sleep(speed)
        GPIO.output(LIGHTS[pattern[i]], GPIO.LOW)
        time.sleep(speed)
    is_displaying_pattern = False
#Function Which wait for Player to enter the same pattern as pattern of LED's
def wait_for_player_to_repeat_pattern():
    #Until game is not won
    while not is_won_current_level and not is_game_over:
        verify_player_auto()
        time.sleep(0.1)
#Start new game after loosing initializing every variable
def reset_board_for_new_game():
    global is_displaying_pattern, is_won_current_level, is_game_over
    global current_level, current_step_of_level, pattern,flag
    is_displaying_pattern = False
    is_won_current_level = False
    is_game_over = False
    current_level = 1
    current_step_of_level = 0
    pattern = []
    flag = 0
    GPIO.output(LIGHTS, GPIO.LOW)
# Function to start the game
def start_game():
    while True:
        add_new_color_to_pattern()
        display_pattern_to_player()
        wait_for_player_to_repeat_pattern()
        if is_game_over:
            print("Game Over! Your max score was {} colors!\n".format(current_level-1))
            play_again = raw_input("Enter 'Y' to play again, or just press [ENTER] to exit.\n")
            if play_again == "Y" or play_again == "y":
                reset_board_for_new_game()
                print("Begin new round!\n")
            else:
                print("Thanks for playing!\n")
                break
        time.sleep(2)
#We have done Threading for Performing multiple task to make this responsive
def start_game_monitor():
    t = threading.Thread(target=start_game)
    t.daemon = True
    t.start()
    t.join()
#DRiver Function
def main():
    global play,flag
    try:
        initialize_gpio()
        GPIO.output(9,0)
        #Condition for detecting motion for first time using motion sensor to start game
        while True:
            if flag == 0 :
                if(GPIO.input(5) == 1):
                    GPIO.output(9,True)
                    flag = 1
                    #time.sleep(2)
                    
            else:
                break
        print("Begin new round!\n")
        play=1
        start_game_monitor()
    finally:
        GPIO.cleanup()
        
if __name__ == '__main__':
    main()
