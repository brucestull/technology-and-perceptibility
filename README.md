## Name
### TAP - Technology and Perceptibility
#### Project Management Pages:
* [Milestones](https://github.com/brucestull/technology-and-perceptibility/milestones)
* [TAP - Minimum Viable Product](https://github.com/brucestull/technology-and-perceptibility/projects/2)
* [TAP - Technology and Perceptibility](https://github.com/brucestull/technology-and-perceptibility/projects/1)


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
<!-- * CSS - [Materialize](https://materializecss.com/) -->
<!-- * CSS - [Bootstrap](https://getbootstrap.com/) -->
<!-- * Full-Stack - [Django](https://docs.djangoproject.com/en/4.0/) -->
<!-- * Templating - Engine [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) -->
* Back-end - [Django REST Framework](https://www.django-rest-framework.org/)
* Front-end - [Vue.js](https://v2.vuejs.org/)
* Graphical Charts - [D3](https://d3js.org/)
<!-- * Graphical Charts - [Chart.js](https://www.chartjs.org/docs/latest/) -->


## Features

### User Stories
1. As an Alternative Navigation user, I want to navigate the application using keyboard only, because this is how I access internet content.
    - [ ] Learn how to make important content waypoints navigable.
2. As an Alternative Navigation user, I want to navigate the application using screen-reader and keyboard only, because this is how I access internet content.
    - [ ] Learn how to make important content waypoints navigable.
3. As a Color Blind user, I want to the application to have adequate contrast, because adequate contrast is important for reading and understanding application content.
    - [ ] Use Color Contrast Analyser as project is built.
4. As a User, I want to be able to create a login account, because I want to use the app in the future to view and edit TAPs.
    - [X] Create User Model.
      - [X] Create CustomUser model in case additional User model fields might be needed in future.
    - [ ] Create API for User Model.
      - [X] Create or use existing `api` app:
        - [X] Create Django REST API `urls.py` for Users.
        - [X] Create Django REST API `serializers.py` for Users.
        - [ ] Create Django REST API `permissions.py` for Users.
        - [ ] Create Django REST API `views.py` for Users.
5. As a User, I want to be able to save a set of three fields (url, url title, url description), because I want to refer to them in the future.
    - [X] Create TAP (data) Model.
      - [X] Create basic TAP Model:
      - [ ] Modify TAP Model to include (or verify it includes) all required fields:
        - [X] URL
        - [X] URL Title
        - [X] URL Label
        - [X] URL Description
        - [ ] Other fields:
          - [ ] Code Snippet
    - [X] Add foreign key to link multiple TAPs to a single user. Will this be in both 'Tap' and 'CustomUser'? [posts.models.py](https://github.com/PdxCodeGuild/class_otter/blob/main/code/merritt/22-jan/drf-blog-22jan/posts/models.py) - It seems there is no need to add to a `users.models.py`.
    - [ ] Create API for TAP Model.
      - [X] Create or use existing `api` app:
        - [X] Create Django REST API `views.py` for TAPs.
        - [X] Create Django REST API `urls.py` for TAPs.
        - [X] Create Django REST API `serializers.py` for TAPs.
        - [ ] Modify (or verify) TAP API to include all required fields:
          - [ ] ???
        - [X] Create Django REST API `permissions.py` for TAPs.
        - [ ] Create permission in `permissions.py` to allow editing of TAPs by User who owns the TAP.
        - [ ] Incorporate permissions in `views.py`.
    - [X] Create input fields (using Vue) for TAP creation component.
      - [X] Bind the input fields to the Vue model.
    - [X] Create button to submit TAP creation action.
      - [X] Use 'v-on:click' or '@click'
6. As a User, I want to access my previously saved field sets, because I want to review and have access to the saved links' url and information.
    NOTE: These features may be completed in User story above.
7. As A mobile phone user, I need to be able to view the field sets.
    - [ ] Ensure site displays appropriately on small screens.

### Miscellaneous Tasks:
- [X] Apply CSS:
  - [X] Apply sticky footer to `base.html`.
  - [X] Apply `flex` and [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media) to a top nav/header. As screen width grows, move from stacked title/nav to side-by-side with one on right and one on left.
  - [X] Compare my own 'cards' in Stuff project to [Card](https://developer.mozilla.org/en-US/docs/Web/CSS/Layout_cookbook/Card) - [Download the code](https://github.com/mdn/css-examples/blob/main/css-cookbook/card--download.html).[^cards-and-accessibility]

[^cards-and-accessibility]:[Cards Accessibility Issues](https://inclusive-components.design/cards/)

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
- [X] 0.5 Days - Learn FireFox Accessibility Tester[^firefox-accessibility-tester]
### Mar 30 - Mar 30:
- [X] 0.5 Days - Learn Materialize - Decided to try my own CSS due to font-size issues
### Mar 31 - Mar 31:
- [X] 0.5 Days - Practice my own custom CSS - [We Got Stuff!](https://github.com/PdxCodeGuild/class_otter/tree/main/code/bruce/Module_02/lab02_Company_Home)
### Mar 31 - Mar 31:
- [X] 0.5 Days - Learn proper accessible ARIA and HTML tags - [HTML Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element#content_sectioning)
### Apr 01 - Apr 04:
- [X] 1.5 Days - Learn Django REST Framework testing
  - [X] [Example Test](https://www.django-rest-framework.org/api-guide/testing/#example)
  - [X] [Another Example Test](https://www.django-rest-framework.org/api-guide/testing/#example_1)
  - [X] [Rendering Responses](https://www.django-rest-framework.org/api-guide/testing/#rendering-responses)
### Apr 04 - Apr 05:
- [X] 1.5 Days - Write Django (REST) tests
### Apr 06 - Apr 07:
- [X] 1.5 Days - TAP Model - API and Front End
### Apr 07 - Apr 10:
- [ ] 1.5 Days - Finish [1. Minimum Viable Product](https://github.com/brucestull/technology-and-perceptibility/milestone/1)
<!-- Not needed, Django provides all the user fuctionality we need. -->
<!-- - [ ] 1.5 Days - User Model - API and Front End -->
### Apr 11 - Apr 12:
- [ ] 2 Days - Finish [2. Accessibility Enhancements](https://github.com/brucestull/technology-and-perceptibility/milestone/2)
### Apr 13 - Apr 14:
- [ ] 1.0 Days - Learn Chart.js or 3D[^stretch-goal]

[^firefox-accessibility-tester]: [FireFox Accessiblity Tester](https://firefox-source-docs.mozilla.org/devtools-user/accessibility_inspector/index.html)


## Project Setup
- [X] Create GitHub repository for [TAP project](https://github.com/brucestull/technology-and-perceptibility)
- [X] Create pipenv
  - [X] Use django==3.2
  - [X] Use docutils==0.18.1 
    [docutils at Django](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/admindocs/#module-django.contrib.admindocs) 
    [docutils at PyPI](https://pypi.org/project/docutils/) 
  - [X] Use djangorestframework==3.13.1 
- [X] Create Django project


## Extras and Reminders
- [ ] Favicon.
- [ ] Normalize the css.
  * [index.html with normalize](https://github.com/PdxCodeGuild/class_otter/blob/main/code/bruce/Module_02/lab03_Blog/templates/index.html)
  * \<link rel="stylesheet" type="text/css" href="https://necolas.github.io/normalize.css/8.0.1/normalize.css" />
- [ ] Check order of \<script\> tags to ensure proper script execution.
- [ ] Check some of the links in Vue console when there are errors/warnings. Sometimes the link will show the actual location of bug even though line numbers may be different than in IDE.
- [ ] CSS is almost done. Add card for CSS finishing touches to the backlog. Finish it some other day.

## License

This project is licensed under the [GNU General Public License v3.0] License - see the [LICENSE.md](https://github.com/brucestull/technology-and-perceptibility/blob/main/LICENSE) file for details


## Resources

Inspiration, examples, code snippets, etc.
* [a11y](https://www.a11yproject.com/)
* [MDN ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)
* [WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)
* [Cards and Accessibility](https://inclusive-components.design/cards/)
* [Anchor links and accessibility](https://amberwilson.co.uk/blog/are-your-anchor-links-accessible/)
* [Yale University - Usability and Web Accessibility](https://usability.yale.edu/web-accessibility/articles/links)
* [htmldog](https://htmldog.com/guides/html/advanced/links/)
* [WabAIM - Skip Navigation Links](https://webaim.org/techniques/skipnav/)
* [Windows 11 - Screen Reader](https://support.microsoft.com/en-us/windows/complete-guide-to-narrator-e4397a0d-ef4f-b386-d8ae-c172f109bdb1#WindowsVersion=Windows_11)
  * WindowsKey+Ctrl+Enter
* Frameworks and Libraries
  * [Vue.js 3](https://vuejs.org/guide/introduction.html)
  * [Vue.js 2](https://v2.vuejs.org/v2/guide/)
  * [Django REST Framework](https://www.django-rest-framework.org/)
  * [Django 3.2](https://docs.djangoproject.com/en/3.2/)
  * [Bootstrap](https://getbootstrap.com/)
  * [Materialize](https://materializecss.com/)
  * [D3 - SVG compatible](https://d3js.org/)
  * [Chart.js - Accessiblity](https://www.chartjs.org/docs/latest/general/accessibility.html)
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
  * [Django REST Testing - APIRequestFactory](https://www.django-rest-framework.org/api-guide/testing/)
  * [Django and Django REST testing - rootstrap.com](https://www.rootstrap.com/blog/testing-in-django-django-rest-basics-useful-tools-good-practices/)
* [a11y - Pronunciation](https://www.a11yproject.com/posts/a11y-and-other-numeronyms/)
* [a11y - Bookmarklets](https://www.a11yproject.com/resources/#bookmarklets)
* [a11y - Development Tools](https://www.a11yproject.com/resources/#development-tools)
* [Inclusive Components](https://inclusive-components.design/)
* [Tooltips & Toggletips](https://inclusive-components.design/tooltips-toggletips/)
* [The Bootcampers Guide to Web Accessibility](https://a11y-with-lindsey.ck.page/products/pre-order-the-bootcampers-guide-to-web)
* [.md syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
* [Accessibility APIs: A Key To Web Accessibility](https://www.smashingmagazine.com/2015/03/web-accessibility-with-accessibility-api/)
* [Create GitHub Wiki](https://docs.github.com/en/communities/documenting-your-project-with-wikis)
