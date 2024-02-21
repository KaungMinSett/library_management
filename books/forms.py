from django import forms
from library.models import Book


INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'



    # title = models.CharField(max_length=200)
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # publication_date = models.DateField()
    # genre = models.ManyToManyField(Genre)
    # isbn = models.CharField(max_length=13, unique=True)
    # count = models.IntegerField(default=1)
class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title','author','publication_date','genre','isbn','count')

        widgets = {
            # 'category':forms.Select(attrs={
            #     'class': INPUT_CLASSES
            # }),
            # 'name':forms.TextInput(attrs={
            #     'class': INPUT_CLASSES
            # }),
            # 'description':forms.Textarea(attrs={
            #     "class":INPUT_CLASSES
            # }),
            # 'price':forms.TextInput(attrs={
            #     "class":INPUT_CLASSES,
            #     "type":"number"
            # }),
            # 'image':forms.FileInput(attrs={
            #     "class":INPUT_CLASSES
            # })
            'title':forms.TextInput(attrs={'class':INPUT_CLASSES}),
            'author':forms.Select(attrs={'class':INPUT_CLASSES}),
            'publication_date':forms.DateInput(attrs={'type':'date','class':INPUT_CLASSES}),
            'genre':forms.SelectMultiple(attrs={'class':INPUT_CLASSES}),
            'isbn':forms.TextInput(attrs={'class':INPUT_CLASSES}),
            'count':forms.NumberInput(attrs={'class':INPUT_CLASSES}),
        }

# class EditBookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ('name','category','description','price','image','is_sold')

#         widgets = {
#             'category':forms.Select(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'name':forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'description':forms.Textarea(attrs={
#                 "class":INPUT_CLASSES
#             }),
#             'price':forms.TextInput(attrs={
#                 "class":INPUT_CLASSES,
#                 "type":"number"
#             }),
#             'image':forms.FileInput(attrs={
#                 "class":INPUT_CLASSES
#             }),
           
#         }