word = str(input("Enter a word: "))

def english_to_pig_latin(word):
  if word[0] in "aeiou":
    return word + "ay"
  else:
    return word[1:] + word[0] + "ay"

print(english_to_pig_latin(word))