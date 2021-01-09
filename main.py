import random


def get_winners():
    """Randomly gets winning numbers"""

    numbers = []

    # Randomly get 5 winning numbers
    for i in range(0, 5):
        if not numbers:
            number = random.randrange(1, 71)
            while number > 25:
                number = random.randrange(1, 71)
            else:
                numbers.append(number)
        else:
            numbers.append(random.randrange(numbers[i - 1], 71))

    # Randomly get multiplying ball
    numbers.append(random.randrange(1, 25))

    return numbers


def get_numbers(winning_numbers):
    """Randomly get players numbers"""

    numbers = []
    jackpot = []
    count = 1

    # Keep loop going while list is empty (not a winner)
    while not jackpot:
        # Randomly get 5 numbers. Use enumeration to index numbers list, create conditions
        for i, h in enumerate(range(0, 5)):

            # If numbers list is empty (1st number) dont get a number over 40
            if not numbers:
                number = random.randrange(1, 71)
                while number > 25:
                    number = random.randrange(1, 71)
                else:
                    numbers.append(number)
            else:
                # While currently generated number is less than last/index number, get new number. Current index minus 1 (Using enumeration here)
                numbers.append(random.randrange(numbers[i - 1], 71))

        # Randomly get multiplying ball
        numbers.append(random.randrange(1, 25))

        print(f'Drawn Numbers: {"-".join([str(i) for i in numbers]):<20} |    Winning Numbers: {"-".join([str(i) for i in winning_numbers])}    |    Play: {count}    |    Money Spent ($2 Each): {count * 2}')
        # Check players if players numbers match jackpot numbers. Break loop if winner
        if numbers == winning_numbers:
            jackpot.append(f'Matched All 6 - {"-".join([str(i) for i in numbers])}')
            break

        # If loop is not broken, redelcare numbers list, add one to games played
        numbers = []
        count += 1

    # Print jackpot
    print(f'Winner - {"-".join([str(i) for i in jackpot])}')
    input("Press enter to close")


if __name__ == '__main__':

    generate_winning_numbers = get_winners()
    print(generate_winning_numbers)
    get_numbers(generate_winning_numbers)
