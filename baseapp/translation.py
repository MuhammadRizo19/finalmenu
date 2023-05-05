from .models import Section, Category, Meal
from modeltranslation.translator import TranslationOptions, register

@register(Section)
class SectionTranslationOptions(TranslationOptions):
    fields = ('section_name',)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(Meal)
class MealTranslationOptions(TranslationOptions):
    fields = ('meal_name', 'meal_description',)