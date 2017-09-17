# django_tree_menu

### Features
* Any number of nesting levels
* Easy to add to template
* Optimized SQL
* Bootstrap 3
* Does not use third-party libraries

### How to use

1. Create Menu in admin

![Menu admin screenshot](https://i.imgur.com/zYdJhR6.png)

2. Create Items for this menu in admin

![Menu items admin screenschot](https://i.imgur.com/gRu5ZAk.png)

3. In begining of template add `{% load draw_menu %}`. 

4. Add this where your menu should be in template `{% draw_menu 'main' %}`

5. You are awesome ^)
