import sys
import traceback

import korean

sys.path.append('./')
import module.korea_language_token as ko


inputVal = input("한글입력 : ")
print("inputVal: %s" %inputVal)

inputVal = inputVal.replace(' ', '')

def split_kor(inputVal):
  splitVal = ''
  splitValEng = ''
  for char in inputVal:
    try:
      values = korean.hangul.split_char(char)
      # print("korean.hangul.split_char(char):%s"%values)
      print(values)
      for val in values:
        if val != "":
          splitVal += val
          splitValEng += ko.token[val]
    except:
      print(traceback.format_exc())
  return [splitVal, splitValEng]

def read_kor_eng(input_val):
  result = korean.morphology.Morpheme('newYork').read()

# split_kor(inputVal)

print(korean.hangul.is_hangul("o"))

# print(korean.morphology.Noun('레벨42').read())
# print(korean.morphology.Morpheme('new York').read())
# print(korean.morphology.Loanword('newyork', 'eng').read())
#
# translations = Translations.load('i18n', 'ko_KR')
# korean.l10n.patch_gettext(translations)
# _ = translations.ugettext
#
# print(_(u'{I like a {0}').format(_(u'banana')))

# translations = Translations.load('i18n', 'ko_KR')
# korean.l10n.patch_gettext(translations)
# _ = translations.ugettext
# _(u'I like a {0}.').format(_(u'banana'))