from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()

    def __str__(self):
        return self.name


class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_completion = models.DateTimeField(blank=True, null=True)
    deadline_date = models.DateTimeField()
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title
