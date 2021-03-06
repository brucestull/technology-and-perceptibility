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

## Growth Areas
### Accessiblity
#### Accessiblity concepts I've learned:
* 'It’s most important for link text to make sense without the surrounding sentences or content.' - [Yale](https://usability.yale.edu/web-accessibility/articles/links)
- [X] Make TAPs model `url` so it isn't required to be provided when creating the TAP.[TAP Issue:18](https://github.com/brucestull/technology-and-perceptibility/issues/18)
  * `blank=True`
* To underline text within an anchor on focus, use `a:focus p {text-decoration: underline;}`

#### Accessibility questions I have:
- [ ] Which element is better for accessiblity, for calling a Vue method: 'button' or 'anchor'

#### ARIA concepts I've learned:
- [x] [WAI-ARIA Roles](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles)
- [x] [Are your Anchor Links Accessible? - amberwilson.co.uk](https://amberwilson.co.uk/blog/are-your-anchor-links-accessible/)
  - [x] [aria-label](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-label)
  - [x] [aria-describedby](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-describedby)

### Django
- [ ] [APITestCase](https://www.django-rest-framework.org/api-guide/testing/#example)

### Vue
- [x] 'textarea' binding:
  \<textarea v-model="editingCurrentTap.url_label" rows="6" cols="75">\</textarea>
- [x] 'name' attribute isn't needed on 'input's with Vue since we're not sending it as an HTTPRequest.

### JavaScript
- [ ] AXIOS - [Error handling](https://axios-http.com/docs/handling_errors)

### Python

### CSS

### HTML
- [x] Requirements to link label element to input element.
  * [label - Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)
  * [input - Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)
  * [label - w3schools](https://www.w3schools.com/tags/tag_label.asp)
  ```
  <label for="the-input"></label>
  <input id="the-input">
  ```

### Project Management:
#### GitHub:
* Learned how to use Projects.
* Learned how to use Issues.

## Commands, keybindings, and dev server info
* Show markdown preview: `ctrl-shift-v`
* Run server: `python manage.py runserver 8010`
* Production:
  * Admin address: [https://technology-and-perceptibility.herokuapp.com/admin/](https://technology-and-perceptibility.herokuapp.com/admin/)
  * API Update User: [https://technology-and-perceptibility.herokuapp.com/api/v1/user-update/](https://technology-and-perceptibility.herokuapp.com/api/v1/user-update/)
  * API Current User: [https://technology-and-perceptibility.herokuapp.com/api/v1/currentuser/](https://technology-and-perceptibility.herokuapp.com/api/v1/currentuser/)
* Dev:
  * App address: [http://localhost:8010/](http://localhost:8010/)
  * Admin address: [http://localhost:8010/admin/](http://localhost:8010/admin/)
  * API address: [http://localhost:8010/api/v1/](http://localhost:8010/api/v1/)
  * API Current User: [http://localhost:8010/api/v1/currentuser/](http://localhost:8010/api/v1/currentuser/)
  * API Update User: [http://localhost:8010/api/v1/user-update/](http://localhost:8010/api/v1/user-update/)
  * API - TAP: [http://localhost:8010/api/v1/taps/](http://localhost:8010/api/v1/taps/)
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
`http://localhost:8010/`
`http://localhost:8010/admin`

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

#### Create branch: `24-add-foreign-key-to-link-user-to-tap`
[TAP MVP Issue: 24](https://github.com/brucestull/technology-and-perceptibility/issues/24)

* Strange errors:
  * `taps.Tap.author: (fields.E300) Field defines a relation with model 'settings.AUTH_USER_MODEL', which is either not installed, or is abstract.`
  * `taps.Tap.author: (fields.E307) The field taps.Tap.author was declared with a lazy reference to 'settings.auth_user_model', but app 'settings' isn't installed.`
  * Needed non-literal form:
    * `AUTH_USER_MODEL` instead of string literal `'AUTH_USER_MODEL'` in `taps.models.Tap.author`.

- [ ] Make TAPs model `url` so it doesn't require input.[TAP Issue:18](https://github.com/brucestull/technology-and-perceptibility/issues/18)
  * `blank=True`

* Migrations:
  * `python manage.py makemigrations taps`
    * Needed to provide author id to allow migration since 'author' field did not exist previously.
  * `python .\manage.py sqlmigrate taps 0006`
  * `python manage.py migrate`

* Modify `api.serializers.py`:
  ```
  from rest_framework import serializers
  from django.contrib.auth import get_user_model

  from taps.models import Tap

  class NestedTapSerializer(serializers.ModelSerializer):
      class Meta:
          model = Tap
          fields = ('id', 'title', 'url', 'url_label', 'description')

  class NestedUserSerializer(serializers.ModelSerializer):
      class Meta: 
          model = get_user_model()
          fields = ('id', 'username')

  class TapSerializer(serializers.ModelSerializer):
      author_detail = NestedUserSerializer(read_only=True, source='author')
      class Meta:
          model = Tap
          fields = ('id', 'title', 'author', 'author_detail', 'url', 'url_label', 'description')

  class UserSerializer(serializers.ModelSerializer):
      taps_detail = NestedTapSerializer(many=True, read_only=True, source='taps')
      class Meta: 
          model = get_user_model()
          fields = ('id', 'username', 'taps_detail')
  ```

* Modify `api.views.py`:
  ```
  class UserViewSet(viewsets.ModelViewSet):
      queryset = get_user_model().objects.all()
      serializer_class = UserSerializer
  ```

* Modify `taps.models.Tap`:
  ```
  from tap_project.settings import AUTH_USER_MODEL

  class Tap(models.Model):
    ...
    author = models.ForeignKey(
      AUTH_USER_MODEL,
      # 'tap_project.settings.AUTH_USER_MODEL',   # This didn't work
      # 'users.CustomUser',                       # This didn't work
      related_name='taps',
      on_delete=models.CASCADE
      )
    ...
  ```

* Modify `api.urls.py`:
  ```
  from api.views import TapViewSet, UserViewSet

  ...
  router.register('users', UserViewSet, basename='users')
  ...
  ```

#### Create branch: `29-users-can-edit-their-taps`
[TAP MVP Issue: 29](https://github.com/brucestull/technology-and-perceptibility/issues/29)

#### Create branch: `20-practice-django-rest-testing`
[TAP MVP Issue: 20](https://github.com/brucestull/technology-and-perceptibility/issues/20)
* A test sample:
  ```
  user_list_url = '/api/v1/users/'

  a_test_user = {
      "username": 'Dezzi',
      "email": 'dezzi@thekitten.edu',
      "password": '1234fuzzy',
  }

  class TestUsersAPI(APITestCase):
      def test_retrieve_user(self):
          self.assertEqual(CustomUser.objects.count(), 0)
          response = self.client.post(user_list_url, a_test_user, format='json')
          self.assertEqual(response.status_code, status.HTTP_201_CREATED)
          self.assertEqual(CustomUser.objects.count(), 1)
          self.assertEqual(CustomUser.objects.get().username, 'Dezzi')
          self.assertEqual(CustomUser.objects.get().email, 'dezzi@thekitten.edu')
  ```

* Django run tests:
  * `python .\manage.py test`
  * `python .\manage.py test api`
  * `python .\manage.py test <the app name>`

#### Create branch: `33-add-rest-framework-tests`
[TAP MVP Issue: 33](https://github.com/brucestull/technology-and-perceptibility/issues/33)

#### Create branch: `35-user-can-add-tap-via-gui`
[TAP MVP Issue: 35](https://github.com/brucestull/technology-and-perceptibility/issues/35)

#### Create branch: `37-user-can-delete-a-tap`
[TAP MVP Issue: 37](https://github.com/brucestull/technology-and-perceptibility/tree/37-user-can-delete-a-tap)

#### Create branch: `30-add-input-labels-for-edit-tap-page`
[TAP MVP Issue: 30](https://github.com/brucestull/technology-and-perceptibility/tree/30-add-input-labels-for-edit-tap-page)

#### Create branch: `42-add-input-labels-for-user-login-signup-etc`
[TAP MVP Issue: 42](https://github.com/brucestull/technology-and-perceptibility/issues/42)
* Django forms already impliments this. Not further action needed.
  * [Django Login and Logout Tutorial - learndjango.com](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
  * [django.contrib.auth - GitHub](https://github.com/django/django/tree/main/django/contrib/auth)
  * [django.contrib.auth - djangoproject](https://docs.djangoproject.com/en/4.0/ref/contrib/auth/)

#### Create branch: `40-all-input-boxes-have-labels`
[TAP MVP Issue: 40](https://github.com/brucestull/technology-and-perceptibility/issues/40)


#### Create branch: `45-add-permissions-to-tap-model-api`
[TAP MVP Issue: 45](https://github.com/brucestull/technology-and-perceptibility/issues/45)
* Example:
  * `api.permissions.py`:
    ```
    class IsAuthorOrReadOnly(permissions.BasePermission):
        def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS:
                return True
            return obj.author == request.user
    ```
  * `api.views.py`:
    ```
    class PostViewSet(viewsets.ModelViewSet):
        queryset = Post.objects.all()
        serializer_class = PostSerializer
        permission_classes = [IsAuthorOrReadOnly]
    ```

#### Create branch: `61-learn-proper-accessible-aria-and-html-tags`
[TAP MVP Issue: 61](https://github.com/brucestull/technology-and-perceptibility/issues/61)

##### Notes:
* Links:
  * http://www.caitlingeier.com/work/
  * https://www.deque.com/blog/author/caitlin-geier/
  * [ARIA: switch role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/switch_role)
  * [ally-101.com](https://a11y-101.com/)
    * [Link texts](https://a11y-101.com/design/links-text)
    * [Link visual](https://a11y-101.com/design/link-visual)
* [Accessibility - Yale](https://usability.yale.edu/web-accessibility/articles/links#image-links)
  * Underline link text when it is focussed, icons also can help.
* focus:
  ```
  a:focus {
    outline: 3px solid orange;
  }
  ```

* Remove underlines:
  ```
  a:active {
    text-decoration: none;
  }
  ```

* Apple iPhone switches:
  * 'tap' the screen or 'press and hold':
    * [iPhone switches](https://support.apple.com/en-us/HT201370)

* It's probably not a good idea for me to use the "Edit" toggles I currently have implemented. These cause abrupt changes to the screen. The buttons and content can move when used like this.

* Focus Styles
  * [Having a Little Fun With Custom Focus Styles - css-tricks.com](https://css-tricks.com/having-a-little-fun-with-custom-focus-styles/)
  * Button style:
    ```
    button:focus {
      outline: 3px dashed orange;
    }
    ```
    ```
    button:focus {
      outline: 3px dashed orange;
      outline-offset: 10px;
    }
    ```
* [User Facing State - css-tricks.com](https://css-tricks.com/user-facing-state/)
* [Focusing on Focus Styles - css-tricks.com](https://css-tricks.com/focusing-on-focus-styles/)
* [Toggle Buttons](https://inclusive-components.design/toggle-button/)
* [2. Using WAI-ARIA](https://www.w3.org/TR/wai-aria-1.1/#usage)



