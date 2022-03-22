from logging import getLogger

from django.views.generic import TemplateView

LOG = getLogger()


class HomeView(TemplateView):
    template_name = 'home.html'
