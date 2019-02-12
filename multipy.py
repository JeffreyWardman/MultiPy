"""
Runs a python script in multiple consoles with different inputs for arguments.

@author: Jeffrey Wardman
"""

import os
import pyautogui


def multipy(pyfile, input_file, virtual_env, PAUSE=0.15):
    """Runs a keygrabber script to set up the data collection for each input in a text file.
    
    Inputs to arguments are written in a text file on a line-by-line basis and separated by
    a space.
    
    :param pyfile:      string      python file
    :param virtual_env: string      virtual environment
    """
    arguments = open(input_file, 'r', newline='\n').read().splitlines()

    # open console
    os.system('gnome-terminal')

    pyautogui.PAUSE = PAUSE  # pause for PAUSE seconds between inputs

    for args in arguments:
        pyautogui.press('enter')

        # activate virtual environment
        pyautogui.typewrite('source activate ' + virtual_env)
        pyautogui.press('enter')

        # run python file
        pyautogui.typewrite('python ' + pyfile + ' ' + args)
        pyautogui.press('enter')

        # open new console tab
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('shift')
        pyautogui.keyDown('T')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('T')
