from django.test import TestCase
from django.core.urlresolvers import reverse


class IndexViewTest(TestCase):

    def setUp(self):

        self.url = reverse('core:index')

    def test_response_200(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)

        self.assertTemplateUsed(response, 'core/index.html')
