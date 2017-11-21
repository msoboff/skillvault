from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home, sport_skills
from .models import Sport

# Create your tests here.

class HomeTests(TestCase):
    def setUp(self):
        self.sport = Sport.objects.create(name='Soccer')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        sport_skills_url = reverse('sport_skills', kwargs={'pk': self.sport.pk})
        print(sport_skills_url)
        print(self.response.content)
        self.assertContains(self.response, 'href="{0}"'.format(sport_skills_url))

class SportSkillsTests(TestCase):
    def setUp(self):
        Sport.objects.create(name='Soccer')

    def test_sport_skills_view_success_status_code(self):
        url = reverse('sport_skills', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_sport_skills_view_not_found_status_code(self):
        url = reverse('sport_skills', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_sport_skills_url_resolves_sport_skills_view(self):
        view = resolve('/sports/1/')
        self.assertEquals(view.func, sport_skills)
