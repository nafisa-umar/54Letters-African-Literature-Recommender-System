from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField

User = get_user_model()

# Create your models here.


class Book(models.Model):
    rec_id = models.IntegerField(primary_key=True)
    goodreads_url = models.URLField(max_length=300)
    title = models.CharField(max_length=255)
    titleComplete = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    imgUrl = models.URLField(max_length=300, blank=True,
                             null=True, default="/media/cover.jpg")
    author = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=15, blank=True, null=True)
    isbn13 = models.CharField(max_length=255, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    numPages = models.SmallIntegerField(blank=True, null=True)
    publishYear = models.SmallIntegerField(blank=True, null=True)
    avgRating = models.DecimalField(
        max_digits=3, decimal_places=2, blank=True, null=True)
    soup = models.TextField(blank=True, null=True)
    stemmedSoup = models.TextField(blank=True, null=True)
    ratings_count = models.SmallIntegerField(blank=True, null=True, default=0)

    class Meta:
        ordering = ('title', )

    def __str__(self):
        return self.title


class Genre(models.Model):
    genre_id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=100)
    book = models.ManyToManyField(Book, verbose_name="books in genre")

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

# class Similarity(models.Model):
#     book1 = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='similar_books')
#     book2 = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='similar_books_as_second')
#     similarity_value = models.FloatField()

#     def __str__(self):
#         return f"{self.book1.title} - {self.book2.title}"


class UserProfile(models.Model):
    # foreign key linking to model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    # genres = models.ManyToManyField(Genre, related_name='userprofiles')

    def __str__(self):
        return self.user.username

# class ExcelFileUpload(models.Model):
#     excelfileupload = models.FileField(upload_to="excel")
