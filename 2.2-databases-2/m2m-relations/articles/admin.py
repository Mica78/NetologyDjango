from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        lst = []
        for form in self.forms:
            lst.append(form.cleaned_data.get('is_main'))
        if True not in lst:
            raise ValidationError("Укажите основной раздел")
        if lst.count(True) > 1:
            raise ValidationError("Основным может быть только один раздел")
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 2
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ScopeInline, ]
