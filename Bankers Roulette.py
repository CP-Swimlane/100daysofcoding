import random
from collections import Counter
import sys
import time
# Split string method
names_string = input("Banker Roulette\n\nBest out of 21. \n\nGive me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

choice = []
a = 0
while a != 21:
  choosing = random.choice(names)
  print(choosing)
  choice.append(choosing)
  spinner = spinning_cursor()
  for _ in range(5):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')
  a += 1

payer = [word for word, word_count in Counter(choice).most_common(1)]
c = Counter(choice)
c.most_common(1)
print("\n")
spinner = spinning_cursor()
for _ in range(5):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')
print(str(payer[0]) + " is going to buy the meal today!\n")
print ("Most Common Name - ",c.most_common(1))
print(choice)