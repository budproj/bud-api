from django.db import models


class KeyResultCommentTypeChoices(models.TextChoices):
    SUGGESTION = 'suggestion'
    PRAISAL = 'praisal'
    QUESTION = 'question'
    ALIGNMENT = 'alignment'
    IMPROVEMENT = 'improvement'
    ISSUE = 'issue'
    COMMENT = 'comment'
