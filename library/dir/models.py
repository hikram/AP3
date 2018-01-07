from django.db import models

# Create your models here.
class Category(models.Model):
	#Model for a book category
    name = models.CharField(max_length=200, help_text="Enter book category:")
    
    def __str__(self):
        return self.name

from django.urls import reverse

class Book(models.Model):
    #Model for books
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    plot = models.TextField(max_length=1000, help_text="Enter a brief description of the plot")
    category = models.ManyToManyField(Category, help_text="Choose a category for this book")
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_category(self):
        return ', '.join([ category.name for category in self.category.all()[:3] ])
    display_category.short_description = 'Category'

import uuid # Required for unique book instances

class BookInstance(models.Model):
	#Model for book instances
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('b', 'Borrowed'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    def __str__(self):
        return '{0} ({1})'.format(self.id,self.book.title)

class Author(models.Model):
	#Model for authors
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    

    def __str__(self):
        return '{0}, {1}'.format(self.first_name,self.last_name)










