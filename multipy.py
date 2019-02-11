import os
import pyautogui


def run_data_processes(pyfile, arguments, input_file, virtual_env):
    """Runs a keygrabber script to set up the data collection for each input in a text file.
    :param pyfile:      string      python file
    :param arguments:   list        input arguments
    :param virtual_env: string      virtual environment
    """
    assert type(arguments) == list, "'arguments' must be a list of strings."

    inputs = open(input_file, 'r', newline='\n').read().splitlines()

    # open console
    os.system('gnome-terminal')

    pyautogui.PAUSE = 0.1  # pause for 0.1 seconds between inputs

    for input in inputs[:3]:
        args = ''
        for i in range(len(arguments)):
            args += ' --' + arguments[i] + ' ' + input.split()[i]

        pyautogui.press('enter')

        # activate virtual environment
        pyautogui.typewrite('source activate ' + virtual_env)
        pyautogui.press('enter')

        # run python file
        pyautogui.typewrite('python ' + pyfile + args)
        pyautogui.press('enter')

        # open new console tab
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('shift')
        pyautogui.keyDown('T')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('T')
