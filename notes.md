# Capstone
* [Capstone Assignment](https://github.com/PdxCodeGuild/class_otter/blob/main/5%20Capstone/Capstone%20Proposal.md)<br>
* [Capstone Respository](https://github.com/brucestull/technology-and-perceptibility)<br>

## Resources
* [Markdown syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)<br>
* [Django Project Setup](https://github.com/PdxCodeGuild/class_otter/blob/main/3%20Django/docs/Django%20Project%20Setup.md)<br>
* [Django Admin Documentation Generator](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/admindocs/#module-django.contrib.admindocs)<br>
* [Docutils](https://docutils.sourceforge.io/)<br>
* [Django Tutorial](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)<br>
* [Django Customizing](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/)<br>
* [Django Custom User Model](https://learndjango.com/tutorials/django-custom-user-model)<br>
* [Example CSS Project](https://github.com/PdxCodeGuild/class_otter/tree/main/code/bruce/Module_03/lab03_chirp)
* [Example Django and Jinja base.html](https://github.com/PdxCodeGuild/class_otter/blob/main/code/bruce/Module_03/lab03_chirp/templates/base.html)
* [Example Django and Jinja templates](https://github.com/PdxCodeGuild/class_otter/tree/main/code/bruce/Module_03/lab03_chirp/templates)


## Commands, keybindings, and dev server info
* Show markdown preview: `ctrl-shift-v`
* Run server: `python manage.py runserver`
* App address: [http://localhost:8000/](http://localhost:8000/)
* Admin address: [http://localhost:8000/admin/](http://localhost:8000/admin/)
* API address: [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/)
* API - TAPs Address: [http://localhost:8000/api/v1/taps/](http://localhost:8000/api/v1/taps/)
* Virtual Environment activation:
  * Powershell: `C:\Users\Bruce\.virtualenvs\technology-and-perceptibility-MoNxetid\Scripts\activate.ps1`
  * BASH: `source C:/Users/Bruce/.virtualenvs/technology-and-perceptibility-MoNxetid/Scripts/activate`

## Project Setup
* [Custom User Model](https://learndjango.com/tutorials/django-custom-user-model)
* [How to start a Django project  (PDXCG Style)](https://github.com/PdxCodeGuild/class_otter/blob/main/3%20Django/docs/Django%20Project%20Setup.md)

### Create and checkout 'setup' branch:
* Use [checkout](https://www.atlassian.com/git/tutorials/using-branches/git-checkout) to create new git branch.<br>
  * `git checkout -b setup`

### Virtual environment setup:
* Create virtual environment
  * `pipenv install django==3.2 docutils==0.18.1 djangorestframework==3.13.1`

### Django Project Creation:
* Create Django Project:
  * `django-admin startproject tap_project .`
* Test server for green rocket:
  * `python manage.py runserver`
* Create Django apps:
  * `python manage.py startapp taps`
  * `python manage.py startapp users`
* Add to `taps_project.settings.py`:
  ```
    INSTALLED_APPS = [
      ...
      'rest_framework',

      'users.apps.UsersConfig',
      ...
    ]
    ...
    AUTH_USER_MODEL = 'users.CustomUser'
  ```
* Add CustomUser to `users.models.py`:
  ```
  from django.contrib.auth.models import AbstractUser

  class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
  ```
* Add form classes to `users.forms.py`:
  ```
  from django.contrib.auth.forms import UserCreationForm, UserChangeForm

  from .models import CustomUser

  class CustomUserCreationForm(UserCreationForm):
    class Meta:
      model = CustomUser
      fields = ('username', 'email')

  class CustomUserChangeForm(UserChangeForm):
    class Meta:
      model = CustomUser
      fields = ('username', 'email')
  ```
* Add class to `users.admin.py`:
  ```
  from django.contrib import admin

  from django.contrib.auth.admin import UserAdmin

  from .forms import CustomUserCreationForm, CustomUserChangeForm
  from .models import CustomUser


  class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'username')

  admin.site.register(CustomUser, CustomUserAdmin)
  ```
* Migrations:
  * `python manage.py makemigrations users`
  * `python manage.py migrate`

* Create superuser:
  * `python manage.py createsuperuser`

* Create `tap_project.secrets.py` and move `SECRET_KEY` to it:
* Add to `tap_project.settings.py`:
  ```
  TEMPLATES = [
      {
          ...
          'DIRS': [BASE_DIR / 'templates'],
          ...
      },
  ]
  ```
  ```
  LOGIN_REDIRECT_URL = 'home'
  LOGOUT_REDIRECT_URL = 'home'
  ```

* Create `templates.registration.login.html`:
  ```
  {% extends "base.html" %}

  {% block title %}Log In{% endblock %}

  {% block content %}
  <h2>Log In</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Log In</button>
  </form>
  {% endblock %}
  ```
* Create `templates.registration.signup.html`:
  ```
  {% extends "base.html" %}

  {% block title %}Sign Up{% endblock %}

  {% block content %}
  <h2>Sign Up</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sign Up</button>
  </form>
  {% endblock %}
  ```
* Create `templates.base.html`:
  ```
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>{% block title %}Technology and Perceptibility{% endblock %}</title>
  </head>
  <body>
      <main>
          {% block content %}
          {% endblock %}
      </main>    
  </body>
  </html>
  ```
* Create `templates.home.html`:
  ```
  {% extends "base.html" %}

  {% block title %}Home{% endblock %}

  {% block content %}
  {% if user.is_authenticated %}
    Hi {{ user.username }}!
    <p><a href="{% url 'logout' %}">Log Out</a></p>
  {% else %}
    <p>You are not logged in</p>
    <a href="{% url 'login' %}">Log In</a> |
    <a href="{% url 'signup' %}">Sign Up</a>
  {% endif %}
  {% endblock %}
  ```
* Modify `tap_project.urls.py`:
  ```
  from django.contrib import admin
  from django.urls import path, include
  from django.views.generic.base import TemplateView

  urlpatterns = [
      path('', TemplateView.as_view(template_name='home.html'), name='home'),
      path('admin/', admin.site.urls),
      path('users/', include('users.urls')),
      path('users/', include('django.contrib.auth.urls')),
  ]
  ```

* Add following to a new `users.urls.py`:
  ```
  from django.urls import path

  from .views import SignUpView

  urlpatterns = [
      path("signup/", SignUpView.as_view(), name="signup"),
  ]
  ```
* Add to `users.views.py`:
  ```
  from django.urls import reverse_lazy
  from django.views.generic.edit import CreateView

  from .forms import CustomUserCreationForm


  class SignUpView(CreateView):
      form_class = CustomUserCreationForm
      success_url = reverse_lazy('login')
      template_name = 'registration/signup.html'
  ```
* Test login and admin page:
`python manage.py runserver`
`http://localhost:8000/`
`http://localhost:8000/admin`

* Add to `tap_project.settings.py`:
  ```
  INSTALLED_APPS = [
    ...
    'taps.apps.TapsConfig',
    ...
  ]

  TIME_ZONE = 'America/New_York'

  STATICFILES_DIRS = [BASE_DIR / 'static']

  LOGIN_URL = 'login'
  ```


- [X] Set up Docutils.
    * [docutils](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/admindocs/#module-django.contrib.admindocs)
- [X] Create branch for next user story.
    * `add-bootstrap-to-templates`

### Start next user story:

#### NOTE: Encountered CSS issues
* Encountered issues with form field labels having font too small while using Materialize. Decided to try my own CSS.
- [X] Create branch for CSS practice and adding to project.
  * `my-css-branch`
* CSS practice directory:
  * `practice_and_learning_directory\practice_css`
* Remember to have patience:
  * It takes time to learn, we will do stuff poorly until we learn how to do it non-poorly.

#### CSS Concepts explored:
  * [box-sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing)
  * [display](https://developer.mozilla.org/en-US/docs/Web/CSS/display)
  * [CSS Selectors](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors)
  * [margin](https://developer.mozilla.org/en-US/docs/Web/CSS/margin)
  * [padding](https://developer.mozilla.org/en-US/docs/Web/CSS/padding)
  * [card](https://developer.mozilla.org/en-US/docs/Web/CSS/Layout_cookbook/Card)
  * [max-width](https://developer.mozilla.org/en-US/docs/Web/CSS/max-width)
  * [em, px](https://www.w3.org/Style/Examples/007/units.en.html)
  * [Flexible Box](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout)
  * [flex-wrap](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-wrap)
  * [justify-content](https://developer.mozilla.org/en-US/docs/Web/CSS/justify-content)
  * [Sticky Footer](https://developer.mozilla.org/en-US/docs/Web/CSS/Layout_cookbook/Sticky_footers)
  * [@media](https://developer.mozilla.org/en-US/docs/Web/CSS/@media)

#### Create branch [git checkout](https://www.atlassian.com/git/tutorials/using-branches/git-checkout): `add-css-header-footer`
* Remember to use [git fetch](https://www.atlassian.com/git/tutorials/syncing/git-fetch):
  * `git fetch --dry-run` a super safe way to see what fetch will do.
  * It downloads current versions of remote branchs.
  * It doesn't automatically `merge` any of these versions.
  * `git pull` will merge remote changes into current branch.
- [X] `git checkout -b add-css-header-footer main`
- [X] Add the css to branch `add-css-header-footer`.
- [X] Only change `README.md`, `notes.md`, and project css on this branch.
* Create `static/css/style.css`.
  * [Django static files](https://docs.djangoproject.com/en/4.0/howto/static-files/)
* Commit the existing CSS version.

#### Create branch [git checkout](https://www.atlassian.com/git/tutorials/using-branches/git-checkout): `???????`
* What is branch name?
* We are going to be writing Django REST tests.
* How about we take a short segue and work on TAP model and API?
* Current branches:
  * `main`
  * `add-css-header-footer` - Functionality mostly complete. Will create new branch for styling the Vue elements on `home.html`.
  * `my-css-branch` - Used to practice CSS. Not necessary to keep.
  * `setup` - Used to set up project. Not necessary to keep.
* Git branch experiment:
  * I've made some changes to `README.md` and `notes.md` and want to see what happens if I create new branch and add those changes to that branch rather than current branch.
  * `git checkout -b edit-readme-and-notes main`
  * `git add -A`
  * `git commit -m "Edited README.md and notes.md"`
  * `git push origin edit-readme-and-notes main`
  * Pulled [changes](https://github.com/brucestull/technology-and-perceptibility/commit/ebf322a06a09a016685d636b0de8a4ecc5e09b57) and [more changes](https://github.com/brucestull/technology-and-perceptibility/commit/bf23fd362a261b5c384dc3e8b45951946486f336) into main.
  * Learned that weird things happen when trying to take notes while on the branch being committed.
  * There is no need to `git pull origin main` (while on `edit-readme-and-notes`) since we don't need to `pull` all the changes to `main` into our feature branch.
    * `git fetch` is probably a better way to get the remote changes onto our local repo.

#### Create branch [git checkout](https://www.atlassian.com/git/tutorials/using-branches/git-checkout): `create-tap-model-and-api`
* `git checkout -b create-tap-model-and-api main`
* Create simple TAP model. This model will be expanded later.
* Register the model `Tap` in `taps.admin.py`.
* Migrations:
  * `python manage.py makemigrations taps`
  * `python .\manage.py sqlmigrate taps 0001`
    * View what migrations will occur.
  * `python manage.py migrate`
* Check admin panel for new TAPs model.
  * `python manage.py runserver`
- [X] Add some TAPs to the db in admin panel.
- [X] Create `api` app:
  * `python manage.py startapp api`
* Look at Pokedex to see what stuff I need to do with `api` app.
  * It seems we don't need to add `api` to `tap_project.settings.py.INSTALLED_APPS`.
##### File Creation/Modifications:

* Modify `tap_project.urls.py`:
  ```
  urlpatterns = [
    ...
    path('api/v1/', include('api.urls')),
    ...
  ]
  ```
* Create `api.urls.py`:
  ```
  from rest_framework.routers import DefaultRouter

  from api.views import TapViewSet

  router = DefaultRouter()
  router.register('taps', TapViewSet, basename='taps')

  urlpatterns = router.urls + [

  ]
  ```

* Modify `api.views.py`:
  ```
  from rest_framework import viewsets

  from taps.models import Tap
  from api.serializers import TapSerializer

  class TapViewSet(viewsets.ModelViewSet):
      queryset = Tap.objects.all()
      serializer_class = TapSerializer
  ```

* Create `api.serializers.py`:
  ```
  from rest_framework import serializers

  from taps.models import Tap

  class TapSerializer(serializers.ModelSerializer):
      class Meta:
          model = Tap
          fields = ('id', 'title', 'description')
  ```

#### Git things I've learned:
* Git update local repo to reflect current remote branches:
`git remote update origin --prune`
* Create and checkout branch from existing branch:
`git checkout -b <my new branch> <existing branch>`
* `git checkout`: [git checkout](https://www.atlassian.com/git/tutorials/using-branches/git-checkout)
* `git pull`: [git pull](https://www.atlassian.com/git/tutorials/syncing/git-pull)
* `git fetch`: [git fetch](https://www.atlassian.com/git/tutorials/syncing/git-fetch)
* `git merge`: [git merge](https://www.atlassian.com/git/tutorials/using-branches/git-merge)

#### Create branch for Vue to list TAPs: `list-taps-on-home`
`git checkout -b list-taps-on-home main`

#### Accessiblity concepts I've learned:
* 'It’s most important for link text to make sense without the surrounding sentences or content.' - [Yale](https://usability.yale.edu/web-accessibility/articles/links)

#### ARIA concepts I've learned: