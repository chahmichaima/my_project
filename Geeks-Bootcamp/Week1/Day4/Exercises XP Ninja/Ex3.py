MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', ' ': '/'
}
ENGLISH_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}
def english_to_morse(text):
    morse_translation = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_translation.append(MORSE_CODE_DICT[char])
    return " ".join(morse_translation)
def morse_to_english(morse_text):
    words = morse_text.split(' / ')
    english_words = []
    for word in words:
        letters = word.split(' ')
        decoded_word = "".join([ENGLISH_CODE_DICT.get(letter, '') for letter in letters])
        english_words.append(decoded_word)
    return " ".join(english_words)
message_morse = english_to_morse("SOS")
print(f"En Morse : {message_morse}")
message_english = morse_to_english("... --- ...")
print(f"En Anglais : {message_english}")