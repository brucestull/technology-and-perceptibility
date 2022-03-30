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


## Commands, keybindings, and dev server info
* Show markdown preview: `ctrl-shift-v`
* Run server: `python manage.py runserver`
* Server address: ``

## Project Setup
* [Custom User Model](https://learndjango.com/tutorials/django-custom-user-model)
* [How to start a Django project  (PDXCG Style)](https://github.com/PdxCodeGuild/class_otter/blob/main/3%20Django/docs/Django%20Project%20Setup.md)
### 1. Create and checkout 'setup' branch:
* Use [checkout](https://www.atlassian.com/git/tutorials/using-branches/git-checkout) to create new git branch.<br>
  * `git checkout -b setup`
### 2. Virtual environment setup:
* Create virtual environment
  * `pipenv install django==3.2 docutils==0.18.1 djangorestframework==3.13.1`
* Virtual Environment activation:
  * Powershell: `C:\Users\Bruce\.virtualenvs\technology-and-perceptibility-MoNxetid\Scripts\activate.ps1`
  * BASH: `source C:/Users/Bruce/.virtualenvs/technology-and-perceptibility-MoNxetid/Scripts/activate`
### 3. Django Project Creation:
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


- [ ] Set up Docutils.
- [ ] Create branch for next user story.
### 4. Start next user story: