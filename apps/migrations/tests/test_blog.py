from uuid import UUID

import pytest
from model_bakery import baker
from django_faker import faker
from rest_framework.reverse import reverse_lazy, reverse
from apps.models import Blog


@pytest.mark.django_db
class TestBlogAPIView:
    @pytest.fixture
    def blogs(self):
        fake = faker
        blog = baker.make(
            Blog,
            name=fake.name(),
        )

    @pytest.fixture
    def url(self):
        return reverse_lazy('blogsP:blog-blog')

    def test_blog_list(self, client, url):
        response = client.get(url)
        assert response.status_code == 200

    def test_blog_create_api(self, client, url):
        url = ''
        response = client.post(url)
        assert response.status_code == 200
