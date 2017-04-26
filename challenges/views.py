from django.shortcuts import render
from datetime import datetime, timedelta
from django.views import generic
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from . import models

class IndexView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        try:
            obj = models.Challenge.objects.get(date=datetime.now())
            if obj.has_shown == False:
                obj.has_shown = True
                obj.save()
            context['challenge'] = obj     

        except ObjectDoesNotExist:
            context["error"] = 'There is no challenge today. Take a break!'

        return context


class OldChallengesView(generic.ListView):
    template_name = "old_challenges.html"
    queryset = models.Challenge.objects.exclude(date__exact=datetime.now()).filter(has_shown=True).values().order_by("-date")
    paginate_by = 10
    context_object_name = "challenges"


class ChallengeDetail(generic.DetailView):
    template_Name = "challenge_detail.html"
    