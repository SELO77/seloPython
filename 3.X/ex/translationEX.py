from babel.support import Translations
import korean

# print(korean.morphology.Loanword('საქართველო', 'kat').read())

test_var = "한글"
# print(korean.hangul.get_vowel(test_var))
print(korean.hangul.split_char(test_var))
korean.morphology.Morphology