"""Dummy forms for the tests of the forms_ajaxified app."""
from django import forms

from . import models


class DummyForm(forms.ModelForm):
    """Dummy form for the tests of the forms_ajaxified app."""
    model = models.DummyModel
