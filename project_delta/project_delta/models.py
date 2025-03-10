from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(maxlength = None)
    id = models.BigAutoField(primary_key=True)
    userrname = models.CharField(max_length= None)
    date_published = models.DateTimeField.auto_now_add()
    date_last_edit = models.DateTimeField.auto_now()
    is_edited = models.BooleanField()
    MAIN_FILTER_CHOICES = {
        "Analysis": "Analysis",
        "Coaching": "Coaching",
        "Discussion": "Discussion",
    }

    SUBFILTER_CHOICES = {
        "Training": "Training",
        "Matchday": "Matchday",
        "Mentality": "Mentality",
        "UCL": "UCL",
        "EPL": "EPL",
        "La Ligo": "La Ligo",
        "Serie A": "Serie A",
        "Bundesliga": "Bundesliga",
        "MLS": "MLS",
        "Team": "Team",
        "Player": "Player",
    }
    FILTER_MAPPING = {
        "Analysis": ["Team", "Player"],
        "Coaching": ["Training", "Matchday", "Mentality"],
        "Discussion": ["UCL", "EPL", "La Ligo", "Serie A", "Bundesliga", "MLS"],
    }

    main_filter = models.CharField(
        max_length=20,
        choices=MAIN_FILTER_CHOICES,
    )
    sub_filter = models.CharField(
        max_length=20,
        choices=SUBFILTER_CHOICES,
    )
    upVotes = models.IntegerField(default=0)
    body = models.TextField()
    is_senior_citzen = models.BooleanField(default = False)
    upvoted_by = models.ManyToManyField(User, related_name="upvoted_posts", blank=True)


class Comment(models.Model):
    pass