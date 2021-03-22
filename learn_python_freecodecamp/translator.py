# Macedonian to Bulgarian

def translate(phrase):
  translation = ""
  for letter in phrase:
    if letter.lower() in "e":
      if letter.isupper():
        translation = translation + "Ja"
      else:
        translation = translation + "ja" 
    else:
      translation = translation + letter
  return translation

print(translate(input("Enter a phrase: ")))