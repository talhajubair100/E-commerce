from modeltranslation.translator import translator, TranslationOptions
from .models import Setting

class SettingTranslationOptions(TranslationOptions):
    fields = ('title', 'contact',)

translator.register(Setting, SettingTranslationOptions)