from selenium import webdriver
from selenium.webdriver.common.by import By
import os


def test_scores_service(url):
    # Set up Chrome WebDriver
    driver = webdriver.Chrome()
    try:
        # Open the URL
        driver.get(url)

        # Find the score element
        score_element = driver.find_element(By.ID, 'score')

        # Get the text of the score element
        score_text = score_element.text

        # Check if the score text is convertible to an integer
        try:
            score = int(score_text)
        except ValueError:
            # Handle the case where the score text is not convertible to an integer
            print("Score text is not convertible to an integer:", score_text)
            return False

        # Check if the score is between 1 and 1000
        score_within_range = 1 <= score <= 1000

        return score_within_range

    finally:
        # Close the WebDriver
        driver.quit()

def main_function():
    # Get URL input from user
    url = input("Enter the URL of the application: ")

    if test_scores_service(url):
        print("Tests passed.")
        return 0
    else:
        print("Tests failed.")
        return -1


if __name__ == "__main__":
    exit_code = main_function()
    os._exit(exit_code)
