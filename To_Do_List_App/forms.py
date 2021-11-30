from django.forms import ModelForm
from .models import Todo
from django import forms
from django.utils.translation import gettext_lazy as _


# class edit_order_detail(ModelForm):
#     class Meta:
#         model = Todo
#         fields = ['completed']
#
#         labels = {
#             'completed': _(''),
#
#         }

class edit_order_detail(forms.ModelForm):

    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {

            'task_name': forms.TextInput(attrs={
                         'class': 'form-control',
                         'placeholder': "Add tasks"
                         }),

            'completed': forms.CheckboxInput(attrs={
                         'class': 'form-check-input',
                         'role': "switch"
                         })
        }
        # labels = {
        #     'completed': _('Completed'),
        # }