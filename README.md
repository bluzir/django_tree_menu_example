# django_tree_menu

![Django Support](https://img.shields.io/badge/django%20versions-1.11%20%7C%202.0%20%7C%202.1%20%7C%202.0%20%7C%202.2-blue.svg)

### Features
* Compatible with Django 1.10 and Django >=2.0
* Any number of nesting levels
* Easy to add to template
* Bootstrap 4 example with 3-level menu
* Doesn't use third-party libraries

### Usage

0. Migrations at first

`python manage.py makemigrations menu`

`python manage.py migrate`

1. Create Menu in admin

![Menu admin screenshot](https://pp.userapi.com/c850236/v850236047/142510/FRRsd79bAAU.jpg)

2. Create child Menu Items for this Menu in admin

![Menu items admin screenschot](https://pp.userapi.com/c850236/v850236047/142523/jkYhQXDmZ8A.jpg)

3. Optionally add subitems to this Menu Item. In this case menu field must be blank

![Menu subitem admin screenshot](https://pp.userapi.com/c850236/v850236047/142523/jkYhQXDmZ8A.jpg)

4. In begining of your template add `{% load draw_menu %}`. 

5. Add this where your Menu should be in template `{% draw_menu 'main' %}`
Where `main` is your Menu slug.

### Examples

1. Create Menu with slug `main` and some Menu Items for it
2. Go to `/templates/home.html`
3. Delete comments at lines 5 and 8
4. `python manage.py runserver` and go to `127.0.0.1:8000`