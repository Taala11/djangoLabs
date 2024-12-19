from django import forms
from .models import Book
from .models import Address, Student, Gallery


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'addresses']
        addresses = forms.ModelMultipleChoiceField(queryset= Address.objects.all(), widget=forms.CheckboxSelectMultiple)

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'image']