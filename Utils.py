import os
SCORES_FILE_NAME = "scores.json"
BAD_RETURN_CODE = 0
def screen_cleaner():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


