## Name
### TAP - Technology and Perceptibility


## Project Overview

### Important Concepts

#### Ultimate Goals of The Project
 * Research and/or literature reviews need to be done to understand how best to provide effective access to technology, both physical individual-use devices and a means of high-speed internet access.
 * Research and/or literature reviews need to be done to understand how other people perceive the world in order to make sure technology is accessible and technology training is effective.
 * This application can be used in the future to store in-house data models, which would be produced by in-house researchers. This information would be used to make decisions on how best to spend resources to provide three things to underserved individuals:
   * Physical technology devices.
   * Some form of high speed internet access.
   * Training in digital literacy.
 * This application can be used to store reference code-snippets of accessible features of web applications, this information would be useful for website developers.

#### Accessibility with Alternative Navigation.
  * Application must be accessible to users of alternative navigation.
  * Application can be tested manually[^firefox-accessibility-tester] or use automated testing.

### Libraries and Frameworks
<!-- CSS - [Materialize](https://materializecss.com/)<br> -->
CSS - [Bootstrap](https://getbootstrap.com/)<br>
Back-end - [Django REST Framework](https://www.django-rest-framework.org/)<br>
Front-end - [Vue.js](https://v2.vuejs.org/)<br>
Graphical Charts - [D3](https://d3js.org/)<br>
<!-- Graphical Charts - [Chart.js](https://www.chartjs.org/docs/latest/)<br> -->


## Features

### User Stories
1. As an Alternative Navigation user, I want to navigate the application using keyboard only, because this is how I access internet content.
    - [ ] Learn how to make important content waypoints navigable.
2. As an Alternative Navigation user, I want to navigate the application using screen-reader and keyboard only, because this is how I access internet content.
    - [ ] Learn how to make important content waypoints navigable.
3. As a Color Blind user, I want to the application to have adequate contrast, because adequate contrast is important for reading and understanding application content.
    - [ ] Use Color Contrast Analyser as project is built.
4. As a User, I want to be able to create a login account, because I want to use the app in the future to view and edit TAPs.
    - [ ] Create User Model.
      - [ ] Create CustomUser model in case additional User model fields might be needed in future.
    - [ ] Create API for User Model.
      - [ ] Create Django REST API views.py for Users.
      - [ ] Create Django REST API urls.py for Users.
      - [ ] Create Django REST API serializers.py for Users.
      - [ ] Create Django REST API permissions.py for Users.
    - [ ] Create input fields (using Vue) for User creation component.
      - [ ] Bind the input fields to the Vue model.
    - [ ] Create button to submit User creation action.
      - [ ] Use 'v-on:click' or '@click'
    - [ ] Have page display name of signed-in User.
      - [ ] Create an HTML block with 'v-if' to control when User's username is displayed and tie that to a 'checkedIn' flag.
5. As a User, I want to be able to save a set of three fields (url, url title, url description), because I want to refer to them in the future.
    - [ ] Create TAP (data) Model.
    - [ ] Create API for TAP Model.
      - [ ] Create Django REST API views.py for TAPs.
      - [ ] Create Django REST API urls.py for TAPs.
      - [ ] Create Django REST API serializers.py for TAPs.
      - [ ] Create Django REST API permissions.py for TAPs.
      - [ ] Create permission in permissions.py to allow editing of TAPs by User who owns the TAP.
      - [ ] Incorporate permissions in views.py.
    - [ ] Create input fields (using Vue) for TAP creation component.
      - [ ] Bind the input fields to the Vue model.
    - [ ] Create button to submit TAP creation action.
      - [ ] Use 'v-on:click' or '@click'
6. As a User, I want to access my previously saved field sets, because I want to review and have access to the saved links' url and information.
    NOTE: These features may be completed in User story above.
7. As A mobile phone user, I need to be able to view the field sets.
    - [ ] Ensure site displays appropriately on small screens.

### Stretch Goals
1. As a User, I want to be able to view the data of an external site's API provided for consumption in a format I can read, because I want to be able to review data from outside organizations.[^external-site-api][^stretch-goal]
2. As a User, I want to be able to view the data of the external site in both graphical-chart and table forms, because I want to be able to know the value trends in the data presented.[^external-site-api][^stretch-goal]
3. As a User, I want to be able to save a fourth element of the above field sets in the form of a code snippet, because I want to be able to include a snippet of code in addition to the existing three fields. This field can be useful to developers who want to share notes.[^stretch-goal]
4. As a User, I want to share my field sets with other users in the form of common access field sets or shared via email or message system, because I want to share my knowledge and interests with other users.[^stretch-goal]

[^stretch-goal]:
    Stretch Goals

## Data Models
* User
  * First Name
  * Last Name
  * Email
* Three/Four Element Field Set
  * URL
  * URL Title
  * URL Description
  * Code Snippet[^stretch-goal]
* Data model for external sites' API[^external-site-api][^stretch-goal]    

[^external-site-api]:
    External API to be determined.


## Schedule
### Mar 30 - Mar 30:
- [ ] 0.5 Days - Learn FireFox Accessibility Tester[^firefox-accessibility-tester]<br>
### Mar 30 - Mar 30:
- [ ] 0.5 Days - Learn Bootstrap
### Apr 31 - Apr 31:
- [ ] 0.5 Days - Learn proper accessible ARIA and HTML tags
### Apr 31 - Apr 04:
- [ ] 1.5 Days - Learn Django REST Framework testing
### Apr 04 - Apr 05:
- [ ] 1.5 Days - Write Django (REST) tests
### Apr 05 - Apr 06:
- [ ] 1.5 Days - User Model - API and Front End
### Apr 07 - Apr 08:
- [ ] 1.5 Days - TAP Model - API and Front End
### Apr 11 - Apr 12:
- [ ] 1.0 Days - Learn Chart.js or 3D[^stretch-goal]

[^firefox-accessibility-tester]: [FireFox Accessiblity Tester](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector/index.html)


## Project Setup
- [X] Create GitHub repository for [TAP project](https://github.com/brucestull/technology-and-perceptibility)
- [ ] Create pipenv
  - [ ] Use django==3.2<br>
  - [ ] Use docutils==0.18.1<br>
    [docutils at Django](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/admindocs/#module-django.contrib.admindocs)<br>
    [docutils at PyPI](https://pypi.org/project/docutils/)<br>
  - [ ] Use djangorestframework==V.v<br>
- [ ] Create Django project


## License

This project is licensed under the [GNU General Public License v3.0] License - see the [LICENSE.md](https://github.com/brucestull/technology-and-perceptibility/blob/main/LICENSE) file for details


## Resources

Inspiration, examples, code snippets, etc.
* [a11y](https://www.a11yproject.com/)
* [MDN ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)
* [WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)
* Frameworks and Libraries
  * [Vue.js 3](https://vuejs.org/guide/introduction.html)
  * [Vue.js 2](https://v2.vuejs.org/v2/guide/)
  * [Django REST Framework](https://www.django-rest-framework.org/)
  * [Django 3.2](https://docs.djangoproject.com/en/3.2/)
  * [Bootstrap](https://getbootstrap.com/)
  * [D3 - SVG compatible](https://d3js.org/)
  * [Chart.js - Accessiblity](https://www.chartjs.org/docs/latest/general/accessibility.html)
  * [Materialize](https://materializecss.com/)
* [Mozilla - On Accessiblity](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
* [FireFox - Accessibility Inspector](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector/index.html)
* [Keyboard-navigable JavaScript widgets](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Keyboard-navigable_JavaScript_widgets)
* [National Digital Inclusion Alliance](https://www.digitalinclusion.org/definitions/)
* [\<canvas\> - Accessibility](https://pauljadam.com/demos/canvas.html)
* [Paul J. Adam - Demos](https://pauljadam.com/demos/)
* [SVG: Scalable Vector Graphics](https://developer.mozilla.org/en-US/docs/Web/SVG)
* [SVG In HTML Introduction](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/SVG_In_HTML_Introduction)
* [SVG animation with SMIL](https://developer.mozilla.org/en-US/docs/Web/SVG/SVG_animation_with_SMIL)
* [SVG Tutorial](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial)
* [PennState - Charts & Accessibility](https://accessibility.psu.edu/images/charts/)
* Glossary - a11y
  * [Nonvisual Desktop Access](https://makeitfable.com/glossary-term/nvda-nonvisual-desktop-access/)
  * [Screenreader](https://makeitfable.com/glossary-term/screen-reader/)
  * [Semantic Markup](https://makeitfable.com/glossary-term/semantic-markup/)
* Testing:
  * [SSA - ANDI](https://www.ssa.gov/accessibility/andi/help/howtouse.html)
  * [Colour Contrast Analyser (CCA)](https://www.tpgi.com/color-contrast-checker/)
  * [Django Test Framework](https://docs.djangoproject.com/en/4.0/topics/testing/)
  * [Django Test Framework @ Mozilla](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)
  * [Django APIRequestFactory](https://www.django-rest-framework.org/api-guide/testing/)
* [a11y - Pronunciation](https://www.a11yproject.com/posts/a11y-and-other-numeronyms/)
* [a11y - Bookmarklets](https://www.a11yproject.com/resources/#bookmarklets)
* [a11y - Development Tools](https://www.a11yproject.com/resources/#development-tools)
* [The Bootcampers Guide to Web Accessibility](https://a11y-with-lindsey.ck.page/products/pre-order-the-bootcampers-guide-to-web)
* [.md syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
* [Accessibility APIs: A Key To Web Accessibility](https://www.smashingmagazine.com/2015/03/web-accessibility-with-accessibility-api/)
