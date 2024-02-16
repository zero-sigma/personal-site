# Readme

This is the public repo for my personal site, created using the [Django Web Framework](https://www.djangoproject.com/) and progressively enhanced using [Unpoly](https://unpoly.com/). I realize that Django + Unpoly is rather heavy-handed for something as simple as a personal site and I plan on deprecating Unpoly in the future. The motivation for using Django for this project is to have a publically available resource for people to reference or copy over into their own projects, as many Django projects available on the web are rather large and sprawling.

## Directory Structure

I'm somewhat opinionated when it comes to how small to medium-sized Django projects should be structured. For example: I much prefer to place my apps inside of an `apps/` directory rather than having them located in the `BASE_DIR` (see `settings.py`, line 10). I also place all templates inside of a parent file, rather than having each of them distributed across each of their respective app folders. I have always found this to be a much more maintainable approach (the exception being larger projects, which I have found some success in structuring as [service layers](https://forum.djangoproject.com/t/structuring-large-complex-django-projects-and-using-a-services-layer-in-django-projects/1487/2))

```
src/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── blog/
│   ├── core/
│   │   └── management/
│   │       ├── delete_migrations.py
│   │       └── delete_pycache.py
│   ├── projects/
│   └── snippets/
├── seo/
│   ├── robots.txt
│   └── sitemap.xml
├── static/
│   ├── css
│   └── js
├── templates/
│   ├── pages
│   ├── blog
│   ├── projects
│   ├── snippets
│   ├── partials
│   │   ├── _navbar.html
│   │   └── _footer.html
│   └── _base.html
├── .gitignore
├── manage.py
└── sample.env
```

## Helpful Commands

### Delete Pycache 

```
$ python manage.py delete_migrations
```

### Delete Migrations

```
$ python manage.py delete_migrations
```

### Livereload (using [django-livereload-server](https://github.com/tjwalch/django-livereload-server))

Start the livereload server:
```python
$ python manage.py livereload
```

```python
$ python manage.py runserver
```

In the browser's address bar access your web app by doing:

```
127.0.0.1:8000 or localhost:8000
```

