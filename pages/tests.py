import pytest
from django.urls import reverse


def test_home_page_status_code(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200


def test_home_uses_right_template(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200
    assert "home.html" in (t.name for t in response.templates)


def test_home_template_contains_correct_html(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200
    html = response.content.decode("utf-8")
    assert "<h1>Homepage</h1>" in html


def test_about_page_status_code(client):
    url = reverse("about")
    response = client.get(url)
    assert response.status_code == 200


def test_about_uses_right_template(client):
    url = reverse("about")
    response = client.get(url)
    assert response.status_code == 200
    assert "about.html" in (t.name for t in response.templates)


def test_about_template_contains_correct_html(client):
    url = reverse("about")
    response = client.get(url)
    assert response.status_code == 200
    html = response.content.decode("utf-8")
    assert "<h1>About page</h1>" in html
