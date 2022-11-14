import re
from random import randint, choice

def count_words(sentence, unique=False):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&;*_~'''
    
    for mark in punctuations: # Remove Punctuations
        sentence = sentence.replace(mark, '')

    words = sentence.split(' ') # Split the sentence by space
    
    if unique: # If counting unique words remove duplicates
        unique_words = []

        for i in words: 
            if i not in unique_words: 
                unique_words.append(i)

        words = unique_words

    length = len(words) # Return the length of the list
    return length

def random_password(length):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aieou'
    special_characters = '''!()-[]{};:'"\,<>./?@#$%^&;*_~'''
    numbers = '0123456789'

    password = ''

    for i in range(length):
        if i % 2 == 0: password += choice(consonants) # If index is even, add consonant
        else: password += choice(vowels) # Otherwise, add vowel
    
    # Choose a random position for the special character and number
    special_character_pos = randint(0, length)
    number_pos = randint(0, length)
    while number_pos == special_character_pos: number_pos = randint(0, length) # Make sure the two aren't the same

    # Write a randome character and random number in those positions
    password = password[0:special_character_pos] + choice(special_characters) + password[special_character_pos:]
    password = password[0:number_pos] + choice(numbers) + password[number_pos:]

    return password

def caesar_cipher(text, key, decrypt=False):
    if decrypt: key *= -1 # We can decrypt simply by turning the key negative

    alaphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    encrypted_text = ''

    for char in text: # Loop over every character in the text
        if char.isupper(): upper = True # If the character is upper, set a boolean to true
        else: upper = False
            
        char = char.lower() # Lower the character because our alphabet is all lowercase

        if char in alaphabet: # Find where the character is present in the alphabet list if it is
            pos = alaphabet.index(char)
            
            encrypted_char = alaphabet[(pos + key) % 26] # Loop over if out of range
            if upper: encrypted_char = encrypted_char.upper() # If the boolean we set from earlier is true, make the encrypted character uppercasing

            encrypted_text +=  encrypted_char # Adding the new encrypted character to the string

        else: # The character is not a letter, and we keep it the same
            encrypted_text += char

    return encrypted_text

def pig_latin(sentence): # Update to use regex
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&;*_~'''
    pig_sentence = ''

    for text in sentence.split(' '): # Split sentence into list of seperate words, and loop over words
        punctuations_pos = []

        for i in range(len(text)): # Remove punctation and store positions, so we can add them later
            if text[i] in punctuations:
                punctuations_pos.append((text[i], i))
                text = text[0 : i : ] + text[i + 1 : :]

        vowel_pos = re.search('[aeiouAEIOU]', text).span()[0] # Find the first vowel in the list

        if vowel_pos == 0: 
            text += 'yay ' # If the word starts with a vowel, add a yay to the end
            shift_pos = 3 # We would need to move any punctuation 3 values over to get to the end of the "yay"

        else: 
            text = text[vowel_pos:] + text[0:vowel_pos] + 'ay ' # If not, move the part before the vowel to the end and add ay
            shift_pos = 2 # We would need to move any punctuation 2 values over to get to the end of the "ay"

        for pos in punctuations_pos: # Loop over the punctuation
            text = text[0:(pos[1]+shift_pos)] + pos[0] + text[(pos[1]+shift_pos):] # Add the punctuation, but shift it over so it reaches the end of the word

        pig_sentence += text # Add the new text to the sentence

    return pig_sentence

# def one_time_pad(sentence, key):
#     encrypted_text = ''
#     alaphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#     for i in range(len(sentence)):
#         if sentence[i] in alaphabet:
#             encrypted_i = alaphabet.index(sentence[i]) + alaphabet.index(key[i])
#             encrypted_text += alaphabet[encrypted_i % 26]

#         else: encrypted_text += sentence[i]

#     return encrypted_text

print(random_password(10)) # Output: A random english sounding string with a random character and number
print(count_words('How many words are in this sentence?')) # Output: 7
print(count_words('How How How many many many unique unique words words words are are are in in in this this this sentence sentence sentence?', unique=True)) # Output: 8
print(caesar_cipher('No one can break this cipher MUHAHHAHAHAHH!!!!!!!', 1))  # Output: Op pof dbo csfbl uijt djqifs NVIBIIBIBIBII!!!!!!
print(caesar_cipher('Op pof dbo csfbl uijt djqifs NVIBIIBIBIBII!!!!!!', 1, decrypt=True)) # Output: No one can break this cipher MUHAHHAHAHAHH!!!!!!
print(pig_latin('Hello, I am awesome and this is a string.')) # Output: ellohay Iyay amyay awesomeyay andyay isthay isyay ayay ingstray.
# print(one_time_pad('no one can break this cipher MUHAHHAHAHAHH!!!!!!!', 'gfhethgtuhwehtrightrhgirtwsnsiurfhrq'))