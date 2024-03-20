import random
import time

def MemoryGame(difficulty):
    def generate_sequence(difficulty):
        return [random.randint(1, 101) for _ in range(difficulty)]

    def get_list_from_user(difficulty, sequence):
        print("Remember the following numbers:")
        print(sequence)
        time.sleep(0.7)
        print("Now enter the numbers you remember:")
        user_list = []
        for _ in range(difficulty):
            while True:
                try:
                    num = int(input("Enter a number: "))
                    if 1 <= num <= 101:
                        user_list.append(num)
                        break
                    else:
                        print("Please enter a number between 1 and 101.")
                except ValueError:
                    print("Please enter a valid integer.")
        return user_list

    def is_list_equal(list1, list2):
        return list1 == list2

    difficulty = int(difficulty)
    sequence = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty, sequence)
    result = is_list_equal(sequence, user_list)
    if result:
        print("Congratulations! You remembered all the numbers!")
        return True
    else:
        print("Sorry, you did not remember all the numbers. You lost.")
        print("Correct sequence was:", sequence)
        return False


# Example usage:
if __name__ == "__main__":
    difficulty = input("Enter game difficulty (1-5): ")
    MemoryGame(difficulty)
