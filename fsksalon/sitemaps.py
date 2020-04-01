from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Hair, Course, Beauty


class BeautySitemap(Sitemap):
    def item(self):
        return Beauty.objects.all()


class CourseSitemap(Sitemap):
    def item(self):
        return Course.objects.all()



class HairSitemap(Sitemap):
    def item(self):
        return Hair.objects.all()

