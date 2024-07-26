import random
from collections import Counter

def roll_dice(num_rolls):
    results = [random.randint(1, 6) for _ in range(num_rolls)]
    return results

def count_results(results):
    count = Counter(results)
    return count

def display_results(count):
    print("\nResults:")
    for i in range(1, 7):
        print(f"{i}: {count.get(i, 0)} times")

def main():
    try:
        num_rolls = int(input("Enter the number of times you want to roll the dice: "))
        if num_rolls <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    results = roll_dice(num_rolls)
    count = count_results(results)
    display_results(count)

if __name__ == "__main__":
    main()