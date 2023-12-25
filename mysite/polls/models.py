from django.db import models


class Question(models.Model):
    """Model for a single poll Question. A question will have multiple choices."""

    question_text: models.CharField = models.CharField(max_length=200)
    pub_date: models.DateTimeField = models.DateTimeField("date published")


class Choice(models.Model):
    """Model for single choice associated with a single question"""

    question: models.ForeignKey = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text: models.CharField = models.CharField(max_length=200)
    votes: models.IntegerField = models.IntegerField(default=0)
