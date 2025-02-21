# -*- coding: utf-8 -*-


# ----------------------------------------------------------------------------------------------------------------------
class Utils:
    """
    Class with util functions which helps to generate some data.
    """

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def generate_sort_dict(book):
        return {'id': book.id,
                'name': book.book_name,
                'author': book.id_author.author_name,
                'url': book.photo.url if book.photo else ''}
