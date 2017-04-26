from datetime import datetime, timedelta

from django.db import models
from django.utils import timezone

# from challenges.tasks import set_challenge_finished


class Challenge(models.Model):
    title = models.CharField(max_length=120)
    suggested_by = models.CharField(max_length=120, blank=True)
    image = models.URLField(max_length=500, blank=True)
    has_shown = models.BooleanField(default=False)
    date = models.DateField(default=datetime.now())

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     same_date_obj = Challenge.objects.filter(date=self.date)
    #     if same_date_obj.exists():
    #         while True:
    #             if Challenge.objects.filter(date=self.date).exists():
    #                 self.date += timedelta(days=1)
    #             else:
    #                 break
    #     super().save(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            date_gte_count = Challenge.objects.filter(date__gte=self.date).count()

            if date_gte_count:
               self.date += timedelta(days=date_gte_count)

            if self.date != datetime.now():
                self.date = datetime.now()

        super(Challenge, self).save(*args, **kwargs)