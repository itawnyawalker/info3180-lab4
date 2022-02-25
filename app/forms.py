from wsgiref.validate import validator
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed


class UploadForm(FlaskForm):
    """Photo upload form"""
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg','png', 'Images only'])])