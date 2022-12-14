# product form from code institute Boutique Ado

'''
Imports relevant django packages
'''
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):
    '''
    Product form information
    '''

    class Meta:
        '''
        Product form fields generator
        '''
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded input-boxes'


class ReviewForm(forms.ModelForm):
    '''
    Review form for the product.
    '''
    class Meta:
        '''
        Fields that are displayed on the form.
        '''
        model = Review
        fields = ('review', 'rating', 'review_writer')

        widgets = {

            'review': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write review here.....'}),
            'review_writer': forms.HiddenInput()
        }
