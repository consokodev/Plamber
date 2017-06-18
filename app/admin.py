# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Category, Author, Book, BookRating, BookComment, AddedBook, TheUser, Language, Post


# ----------------------------------------------------------------------------------------------------------------------
class CustomUserAdmin(UserAdmin):
    """
    Class for specifying extra fields for admin panel.
    """
    list_display = ('id',) + UserAdmin.list_display
    ordering = ('-id',)


# ----------------------------------------------------------------------------------------------------------------------
class TheUserAdmin(admin.ModelAdmin):
    """
    Class for pretty representation data of users in admin panel.
    """
    list_display = ('id', 'username', 'email')

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def username(obj):
        return obj.id_user.username

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def email(obj):
        return obj.id_user.email


# ----------------------------------------------------------------------------------------------------------------------
class CategoryAdmin(admin.ModelAdmin):
    """
    Class for pretty representation data of categories in admin panel.
    """
    list_display = ('category_name',)


# ----------------------------------------------------------------------------------------------------------------------
class AuthorAdmin(admin.ModelAdmin):
    """
    Class for pretty representation data of authors in admin panel.
    """
    list_display = ('id', 'author_name')


# ----------------------------------------------------------------------------------------------------------------------
class LanguageAdmin(admin.ModelAdmin):
    """
    Class for pretty representation data of languages in admin panel.
    """
    list_display = ('language',)


# ----------------------------------------------------------------------------------------------------------------------
class BookAdmin(admin.ModelAdmin):
    """
    Class for pretty representation data of books in admin panel.
    """
    list_display = ('id', 'book_name', 'author', 'category', 'language', 'who_added', 'upload_date')

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def author(obj):
        return obj.id_author.author_name

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def category(obj):
        return obj.id_category.category_name

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def language(obj):
        return obj.language.language


# ----------------------------------------------------------------------------------------------------------------------
class BookGeneral(admin.ModelAdmin):
    """
    General class for Ratings, Comments and Added books.
    """
    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def user(obj):
        return obj.id_user

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def book(obj):
        return '({}) {}'.format(obj.id_book.id, obj.id_book)


# ----------------------------------------------------------------------------------------------------------------------
class BookRatingAdmin(BookGeneral):
    """
    Class for pretty representation data of book rating in admin panel.
    """
    list_display = ('user', 'book', 'rating')


# ----------------------------------------------------------------------------------------------------------------------
class BookCommentAdmin(BookGeneral):
    """
    Class for pretty representation data of book comments in admin panel.
    """
    list_display = ('user', 'book', 'text', 'posted_date')


# ----------------------------------------------------------------------------------------------------------------------
class AddedBookAdmin(BookGeneral):
    """
    Class for pretty representation data of added books in admin panel.
    """
    list_display = ('user', 'book', 'last_page', 'last_read')


# ----------------------------------------------------------------------------------------------------------------------
class PostAdmin(admin.ModelAdmin):
    """
    Class for pretty representation data of project blog posts in admin panel.
    """
    list_display = ('heading', 'user', 'posted_date')


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(TheUser, TheUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookRating, BookRatingAdmin)
admin.site.register(BookComment, BookCommentAdmin)
admin.site.register(AddedBook, AddedBookAdmin)
admin.site.register(Post, PostAdmin)
