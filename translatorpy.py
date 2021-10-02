from translate import Translator
text=(input("enter the word to be translated: "))
toLanguage=(input("enter to what language to translate: "))
translator= Translator(from_lang="english",to_lang=toLanguage)
translation= translator.translate(text)
print(translation)
translator=Translator(from_lang="english",to_lang="spanish")
trans=translator.translate(text)