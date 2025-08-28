def count_vowels_consonants(text):
    text = text.replace(" "," ")
    text = text.lower()
    vowels = text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')
    number = text.count('1') - text.count('2') - text.count('3') - text.count('4') - text.count('5') - text.count('6') - text.count('7') - text.count('8') - text.count('9')
    consonants = len(text) + vowels - number
    return {
        'vowele':vowels,
        'consonants' : consonants
    }