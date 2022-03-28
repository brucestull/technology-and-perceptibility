## Name
### TAP
* Technology and Perceptibility


## Project Overview
* User can register (create account).
* User can save NAMEs (link to accessibility resource with description).
* User can access thier previously saved NAMEs.
* User can share their link to a friend's email (or NAME account).
* User can control full features of application using keyboard or other alternative navigation.
* User can save examples of accessibility-related code snippets.
* User can view data and data trends in graphic-chart and table forms.

### Important Concepts
* Accessibility with Alternative Navigation.
  * Application must be accessible to users of alternative navigation.
  * Application can be tested manually or use automated testing.
* Research needs to be done to understand how best to provide effective access to technology, both physical individual-use devices and a means of high-speed internet access.
* Research needs to be done to understand how other people perceive the world in order to make sure technology is accessible and technology training is effective.
* This application can be used to store reference code-snippets of accessible features of web applications, this information would be useful for website developers.
* This application can be used in the future to store in-house data models, which would be produced by in-house researchers. This information would be used to make decisions on how best to spend resources to provide three things to underserved individuals:
  * Physical technology devices.
  * Some form of high speed internet access.
  * Training in digital literacy.

### Libraries and Frameworks
CSS - [Materialize](https://materializecss.com/)<br>
Back-end - [Django REST Framework](https://www.django-rest-framework.org/)<br>
Front-end - [Vue.js](https://v2.vuejs.org/)<br>
Graphical Charts - [D3](https://d3js.org/)
Graphical Charts - [Chart.js](https://www.chartjs.org/docs/latest/) 


## Features
### User Stories
1. As an Alternative Navigation user, I want to navigate the application using keyboard only, because this is how I access internet content.
2. As an Alternative Navigation user, I want to navigate the application using screen-reader and keyboard only, because this is how I access internet content.
3. As a User, I want to be able to create a login account, because I want to use the app in the future and have access to previous actions.
4. As a User, I want to be able to save a set of three fields (url, url title, url description), because I want to refer to them in the future.
5. As a User, I want to access my previously saved field sets, because I want to review and have access to the saved links' url and information.
6. As a User, I want to share my field sets with other users in the form of common access field sets or shared via email or message system, because I want to share my knowledge and interests with other users.
7. As a User, I want to be able to save a fourth element of the above field sets in the form of a code snippet, because I want to be able to include a snippet of code in addition to the existing three fields.
8. As A mobile phone user, I need to be able to view the field sets.

### Stretch Goals
1. As a User, I want to be able to view the data of an external site's API provided for consumption in a format I can read, because I want to be able to review data from outside organizations.[^external-site-api]
2. As a User, I want to be able to view the data of the external site in both graphical-chart and table forms, because I want to be able to know the value trends in the data presented.[^external-site-api]


## Data Models
* User
  * First Name
  * Last Name
  * Email
* Three/Four Element Field Set
  * URL
  * URL Title
  * URL Description
  * Code Snippet
* Data model for external sites' API[^external-site-api]    

[^external-site-api]:
    These are items in the stretch goal.

## Schedule






## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Resources

Inspiration, examples, code snippets, etc.
* [a11y](https://www.a11yproject.com/)
* [MDN ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)
* [WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)
* [Keyboard-navigable JavaScript widgets](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Keyboard-navigable_JavaScript_widgets)
* [National Digital Inclusion Alliance](https://www.digitalinclusion.org/definitions/)
* [Chart.js - Accessiblity](https://www.chartjs.org/docs/latest/general/accessibility.html)
* [\<canvas\> - Accessibility](https://pauljadam.com/demos/canvas.html)
* [Paul J. Adam - Demos](https://pauljadam.com/demos/)
* [SVG: Scalable Vector Graphics](https://developer.mozilla.org/en-US/docs/Web/SVG)
* [D3 - SVG compatible](https://d3js.org/)
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
* [a11y - Pronunciation](https://www.a11yproject.com/posts/a11y-and-other-numeronyms/)
* [a11y - Bookmarklets](https://www.a11yproject.com/resources/#bookmarklets)
* [a11y - Development Tools](https://www.a11yproject.com/resources/#development-tools)
* [.md syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
* [Accessibility APIs: A Key To Web Accessibility](https://www.smashingmagazine.com/2015/03/web-accessibility-with-accessibility-api/)
