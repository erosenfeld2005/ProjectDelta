from django.db import models

class Report(models.Model):
    #can set to null so report is not delted if the user who made the report 
    #deleted their account
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True) 
    id = models.BigAutoField(primary_key=True)
    body = models.TextField()
    is_seen = models.BooleanField()
    is_processed = models.BooleanField()
    is_upheld = models.BooleanField()
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    body = models.TextField()
    upVotes = models.IntegerField(default=0)
    upvoted_by = models.ManyToManyField(User, related_name="upvoted_posts", blank=True)
    reports = models.ForeignKey(Report, on_delete=models.CASCADE)

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
        "La Liga": "La Liga",
        "Serie A": "Serie A",
        "Bundesliga": "Bundesliga",
        "MLS": "MLS",
        "Team": "Team",
        "Player": "Player",
    }
    FILTER_MAPPING = {
        "Analysis": ["Team", "Player"],
        "Coaching": ["Training", "Matchday", "Mentality"],
        "Discussion": ["UCL", "EPL", "La Liga", "Serie A", "Bundesliga", "MLS"],
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
    is_senior_citizen = models.BooleanField(default = False)
    upvoted_by = models.ManyToManyField(User, related_name="upvoted_posts", blank=True)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reports = models.ForeignKey(Report, on_delete=models.CASCADE)
