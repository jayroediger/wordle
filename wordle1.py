from random import  choice

words_list =["apple", "hello", "enter", "found", "trail",]

word = choice(words_list)

wrong_tries = 1

while True:
  guessed_word = input("Enter a 5 letter word: ")
  for i in range(5):
    if word[i] == guessed_word[i]:
      print(guessed_word[i], "\U0001F7E9")
    elif guessed_word[i] in word:
      print(guessed_word[i], "\U0001F7E8")
    else:
      print(guessed_word[i], "\U0001F7E5" )
  print("-" * 40)
  if guessed_word == word:
    print("Your guessed the word correctly in", wrong_tries, "tries.")
    break
  else:
    wrong_tries = wrong_tries + 1 