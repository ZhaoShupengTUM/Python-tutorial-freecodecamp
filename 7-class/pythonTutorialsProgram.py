#calculators
"""
num1 = float(input("Enter the first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter the second number: "))

if op == "+":
    print(num1 + num2)
elif op == "/":
    print(num1 / num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operators")
"""

#guess secret word
"""
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, Yuo lose!")
else:
    print("You win!")
"""

#Exponent functions 2**3
"""
def raise_to_power(base_num, pow_number):
    result = 1
    for index in range(pow_number):
        result = result * base_num
    return result
print(raise_to_power(3,2))
"""

#translators
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))



