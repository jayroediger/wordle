from random import  choice

words_list =["apple", "hello", "enter", "found", "trail",]

word = choice(words_list)

wrong_tries = 1

while True:
  guessed_word = input("Enter a 5 letter word: ")
  for i in range(5):
    if word[i] == guessed_word[i]:
      print("\033[92m {}\033[00m" .format(guessed_word[i]), end = " ")
    elif guessed_word[i] in word:
      print("\033[93m {}\033[00m" .format(guessed_word[i]), end = " ")
    else:
      print("\033[91m {}\033[00m" .format(guessed_word[i]), end = " " )
  print("\n","-" * 40)
  if guessed_word == word:
    print("Your guessed the word correctly in", wrong_tries, "tries.")
    break
  else:
    wrong_tries = wrong_tries + 1