# -*- coding: utf-8 -*-

import imghdr
import io

import PyPDF2

from django.core.exceptions import ValidationError


# ----------------------------------------------------------------------------------------------------------------------
def validate_image(value):
    """
    Validates if the image which is uploading is exactly image, because file can be renamed.
    Raises an error if validation not passed.

    :param str value: The file object.
    """
    if not imghdr.what(value):
        raise ValidationError('Tried to upload not an image!')


# ----------------------------------------------------------------------------------------------------------------------
def validate_pdf(value):
    """
    Validates the uploading file if it is a PDF.
    Raises an error if validation not passed.

    :param value: The file object.
    """
    try:
        PyPDF2.PdfFileReader(io.BytesIO(value.read()))
    except PyPDF2.utils.PdfReadError:
        raise ValidationError('Tried to upload not PDF as a book!')
