# instant_message_bot.py - this program will automatically send out messages to a group of friends


import pyautogui, time, pyperclip
import logging

# Set up the logging parameters.
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
file_handler = logging.FileHandler('instant_message_bot.log')
formatter = logging.Formatter('%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)



# Get basic parameters out of the way.

new_convo_box = (2169, 190)                 # position of starting our gui automation
email_list = []         # Set  a a list of emails to send. 
message = ''            # Create a message to send over. 


# Image Verification coordinates
add_pic_logo = (3808, 1059)
pic_logo_colors = (255, 255, 255)                       # This may need to be modified depending on how reliable it is.

logger.debug('Initilized the regular parameters to start automation')


# Loop through our email list and Enter the person's email address
for email in email_list:
    print(f'Sending a message  to {email}')
    x, y = new_convo_box
    pyautogui.click(x, y, duration=0.4)
    pyautogui.typewrite(email)
    time.sleep(2)           # Give the program enough time to register the email.
    pyautogui.press('enter')
    logger.debug(f'Searched up {email}')

    # Verify that the message box has been created.
    if pyautogui.pixelMatchesColor(3640, 1063, pic_logo_colors):
        # Send out th message.
        pyautogui.typewrite(message, interval=0.05)
        time.sleep(2)
        pyautogui.hotkey('shiftleft', 'pageup')
        time.sleep(1)
        pyautogui.keyDown('ctrlleft')
        pyautogui.press('c')
        pyautogui.keyUp('ctrlleft')
        text = pyperclip.paste()
        if text == message:
            pyautogui.typewrite(['enter'])
        else:
            print(f'There was problem verifying that the text box opened up for {email}')
            logger.warning(f"The text box couldn't be opened up for {email}")
            continue
    else:
        print(f'There was an error sending a message to {email} ')
        logger.warning(f"Couldn't validate that the message box was actually opened up.")
        continue

