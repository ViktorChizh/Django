from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
#  admin.site.register(Author)
admin.site.register(Genre)
#  admin.site.register(BookInstance)
admin.site.register(Language)

#  Define the admin class
class BookInLine(admin.TabularInline):  # добавил как выполнение домашнего задания
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInLine]  # добавил как выполнение домашнего задания

#  Register the admin class with the associated model

admin.site.register(Author, AuthorAdmin)

#  В этот раз для создания и регистрации новых моделей используем декоратор @register (он делает то же самое, что и admin.site.register())
#  Register the Admin classes for Book using decorator

class BookInstanceInLine(admin.TabularInline):
    model = BookInstance
    extra = 0 # убирает пустые строки снизу при вводе информации о копиях (по умолчантю 3 пустых строки)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInLine]

#  Register the Admin classes for BookInstance using decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')  # добавил как выполнение домашнего задания
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availabiliti', {
            'fields': ('status', 'due_back', 'borrower')
        })
    )
