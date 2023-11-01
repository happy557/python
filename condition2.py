digits = input("Enter the numbers: ")

if not digits:
    result = []
else:
    digit_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    combinations = [""]
    for digit in digits:
        new_combinations = []
        for letter in digit_to_letters.get(digit, ''):
            for combination in combinations:
                new_combinations.append(combination + letter)
        combinations = new_combinations

    result = combinations

print(result)