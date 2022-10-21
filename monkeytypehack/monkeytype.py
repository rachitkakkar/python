import pytesseract
from pyautogui import screenshot
from pynput.keyboard import Key, Controller
from time import sleep

sleep(1)

# Screenshot the region of the screen with the text and use the tesseract optical character recognition engine (OCR) to detect the text from the image
keyboard = Controller()
screen = screenshot(region=(500, 825, 1920, 300))
message = pytesseract.image_to_string(screen).replace('\n', ' ')

if (message[0] == 'l'): message = message[1:] # If the OCR detects the cursor as a letter, remove it

# Use pyautogui to type each character in the message with a delay to get a WPM with a number (shows Infinite WPM without it)
# WPM -> words per minute
for c in message:
    sleep(0.011)
    keyboard.press(c)
