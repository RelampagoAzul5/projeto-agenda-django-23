# from django.db.models import Q
from typing import Any, Dict
from django.shortcuts import render  # , get_object_or_404, redirect
from contact.models import Contact
from django.core.exceptions import ValidationError
# from django.core.paginator import Paginator
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone'
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        self.add_error(
            'first_name', ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        return super().clean()


def create(request):
    if request.method == 'POST':

        context = {
            'form': ContactForm(request.POST)
        }
        return render(
            request,
            'contact/create.html',
            context
        )
    context = {
        'form': ContactForm()
    }
    return render(
        request,
        'contact/create.html',
        context
    )
