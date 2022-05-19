#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pw_straight = []
run_count = 0

while run_count != nr_letters:
  letter = random.choice(letters)
  pw_straight.append(letter)
  run_count += 1
run_count = 0

while run_count != nr_numbers:
  number = random.choice(numbers)
  pw_straight.append(number)
  run_count += 1
run_count = 0

while run_count != nr_symbols:
  symbol = random.choice(symbols)
  pw_straight.append(symbol)
  run_count += 1
run_count = 0

print("\n")
print("Eazy Level - Order not randomised:\n")
print("Your Easy Level Password is: " + ("".join(map(str,pw_straight))))
print("\n")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random.shuffle(pw_straight)
print("Hard Level - Order of characters randomised:\n")
print("Your Hard Level Password is: " + ("".join(map(str,pw_straight))))