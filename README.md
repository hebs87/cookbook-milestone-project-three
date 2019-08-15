# [Fine Dining Online Cookbook](https://online-cookbook-ms3-hebs87.herokuapp.com/) - Milestone Project Three

## Table of Contents

- [**About**](#About)
  - [Why This Project?](#Why-This-Project)
- [**UX**](#UX)
  - [User Stories](#User-Stories)
  - [Research](#Research)
  - [Style Rationale](#Style-Rationale)
  - [Wireframes](#Wireframes)
- [**Features**](#Features)
  - [Functionality](#Functionality)
  - [Existing Features](#Existing-Features)
    - [Game Controls](#Game-Controls)
    - [Modes](#Modes)
  - [Features Left To Implement](#Features-Left-To-Implement)
- [**Technologies Used**](#Technologies-Used)
  - [Version Control](#Version-Control) 
- [**Testing**](#Testing)
  - [Testing User Stories](#Testing-User-Stories)
  - [Automated Testing](#Automated-Testing)
    - [Run Jasmine Tests](#Run-Jasmine-Tests)
    - [Create Jasmine Tests](#Create-Jasmine-Tests)
  - [Responsive Testing](#Responsive-Testing)
  - [Additional Testing](#Additional-Testing)
  - [HTML And CSS Validation](#HTML-And-CSS-Validation)
  - [Interesting Bugs Or Problems](#Interesting-Bugs-Or-Problems)
- [**Deployment**](#Deployment)
  - [Repository Link](#Repository-Link)
  - [Running Code Locally](#Running-Code-Locally)
- [**Credits**](#Credits)
  - [Content](#Content)
  - [Media](#Media)
    - [Sounds](#Sounds)
  - [Acknowledgements](#Acknowledgements)
  - [Disclaimer](#Disclaimer)

## About

This application (app) is an online cookbook - a place where users can find recipes for any occasion. Users can also create their own free account and add an unlimited number of recipes that they can share with other users and visitors.

Users can rate recipes, and like recipes to add them to their 'Liked' list for easy access from their own profile page. Users can also print recipes directly from the site.

### Why This Project?

I created this app for the Data Centric Development project of [**_Code Institute's_**](https://codeinstitute.net/) Full Stack Software Development course. The project scope was to create a web app using Python and a no-SQL database (MongoDB), which uses **CRUD** operations to allow users to easily create, read, update and delete food recipes.

The front-end display and functionality used HTML, CSS and JavaScript.

## UX

### User Stories

- As a consumer, I want to browse a catalogue of recipes so that I can decide on a suitable meal for a particular occasion
- As a chef, I want to store my own recipes on a website so that I can share them with others
- As a chef, I want to be able to update any recipes that I can see any mistakes with, so that the consumers see the correct details for a particular recipe
- As a blogger, I want to be able to rate recipes that I try out so that I can let others know how good/bad they are
- As a consumer, I want to be able to search for a particular recipe by its name, so that I can access that particular recipe easily and quickly
- As a consumer, I want to be able to filter recipes based on various categories and see a quick summary of them before I decide on which one to choose, so that I don't have to waste time going through the ingredients list for each one
- As a consumer, I want to see a summary list of recipes based on the most liked, so that I can quickly see the most popular ones

### Style Rationale

I received inspiration for the style of my app following my visit to a dessert restaurant called [**_Heavenly Desserts_**](https://heavenlydesserts.co.uk/). I thought the colour scheme of both the resetaurant and their website looked really modern and professional, and I wanted this to be mirrored in my web app too.

### Wireframes

I drew my wireframes using Balsamiq. I have done separate wireframes to show my consideration of how to make my website/app responsive. The links to the files are below:

- [Home - no user logged in (xs, sm and md)](https://github.com/hebs87/cookbook-milestone-project-three/blob/master/cookbook/wireframes/home-md-sm-no-login.png)
- [Home - no user logged in (lg and xl)](https://github.com/hebs87/cookbook-milestone-project-three/blob/master/cookbook/wireframes/home-xl-lg-no-login.png)
- [Home - user logged in (xs, sm and md)](https://github.com/hebs87/cookbook-milestone-project-three/blob/master/cookbook/wireframes/home-md-sm-logged-in.png)
- [Home - user logged in (lg and xl)](https://github.com/hebs87/cookbook-milestone-project-three/blob/master/cookbook/wireframes/home-xl-lg-logged-in.png)
- [Browse (xs, sm and md)](https://github.com/hebs87/cookbook-milestone-project-three/blob/master/cookbook/wireframes/browse-md-sm.png)
- [Browse (lg and xl)](https://github.com/hebs87/cookbook-milestone-project-three/blob/master/cookbook/wireframes/browse-xl-lg.png)
- [Recipe (xs, sm and md)](https://github.com/hebs87/cookbook-milestone-project-three/blob/master/cookbook/wireframes/recipe-md-sm.png)
- [Recipe (lg and xl)](https://github.com/hebs87/cookbook-milestone-project-three/blob/master/cookbook/wireframes/recipe-xl-lg.png)
- [Add Recipe (xs, sm and md)](https://github.com/hebs87/cookbook-milestone-project-three/blob/master/cookbook/wireframes/add-recipe-md-sm.png)
- [Add Recipe (lg and xl)](https://github.com/hebs87/cookbook-milestone-project-three/blob/master/cookbook/wireframes/add-recipe-xl-lg.png)

There are some differences between my wireframes and my final website. This was due to visual preferences and feedback received from my mentor, and also other users who tested my website.

### Database Schema

Before building my project, I designed the database schema for the various collections that I would use. The links to the files are below:

- []()
- []()
- []()

## Features

### Functionality

The app uses Python logic to allow users to login, or register for a free account. The app offers **CRUD** operations to allow users to create, read, update and delete food recipes. Users can search for a recipe by name, or they can filter recipes based on various categories. Additionally, users can like recipes and add them to their list for easy access.

I added some additional features that weren't within the scope of the project, as I felt that they offered better interactivity for users.

### Existing Features

- **Navbar/Sidenav Links** - The navbar and sidnav links vary depending on whether the user is logged in or not. If the user isn't logged in, the Home, Browse and Login links are shown. When the user is logged in, the Home, Browse, Profile, Add Recipe and Logout links are shown.
- **Index Buttons** - The buttons on the index page vary depending on whether the user is logged in or not. If the user isn't logged in, the Browse and Login buttons are shown. When the user is logged in, the Browse, Profile and Add Recipe buttons are shown.
- **Flash Messages** - Displayed at the top of the page below the navbar. These messages differ based on user interaction and provides helper messages for users. Each message is displayed for 3000 milliseconds.
- **Login** - Allows existing users to login to their account. The form's username field only accepts alphanumeric values. I've included authorization checks to verify the username and password (hashed password) against the details stored in the database before users can be logged in.
- **Register** - Allows new users to register for a free account. The form's username field only accepts alphanumeric values. I've included checks to ensure that the username doesn't already exist in the database before users are successfully registered. The passwords stored in the database are hashed for security purposes.
- **Logout** - Allows users to logout of their account by clicking the 'Logout' link in the navbar/sidenav. Upon clicking the button, the user session ends.
- **Profile Page** - When logged in, users can visit their profile page to view a list of their added or liked recipes, change their password or delete their account.
- **Added Recipes List** - In the user's profile page, the 'Added Recipes' section displays a list of the user's added recipes. The user can click the image or recipe name to view the full details of that particular recipe. If the user hasn't added any recipes, a generic message is displayed which the user can click to add a recipe (redirects the user to the 'Add Recipe' page).
- **Liked Recipes List** - In the user's profile page, the 'Liked Recipes' section displays a list of the user's liked recipes. The user can click the image or recipe name to view the full details of that particular recipe. Alternatively, the user can click the 'Liked' button to unlike the recipe and remove it from their list. If the user hasn't liked any recipes, a generic message is displayed which the user can click to browse all recipes (redirects the user to the 'Browse' page).
- **Change Password** - In the user's profile page, the 'Change Password' button triggers a modal with a form. The form asks for the user's existing password and new password. I've included authorization checks to verify the existing password (hashed password) against the details stored in the database before the user's password is successfully changed. If the check is successful, the password in the database is updated with the new hashed password.
- **Delete Account** - In the user's profile page, the 'Delete Account' button triggers a modal with a form. The form asks the user to confirm their existing password before deleting their account.I've included authorization checks to verify the existing password (hashed password) against the details stored in the database before the user's account is successfully deleted and their record is removed from the database. When a user's account is deleted, all their added recipes are removed from the site and from other users' liked lists too.
- **Browse** - All recipes are initially displayed when the Browse page first loads, only if their 'deleted' field value in the database is 'False'. The recipes are displayed in cards with some of the recipe's quick stats.
- **Search** - The user can search for a particular recipe by a keyword in the recipe name, and the results are subsequently diplayed when the user clicks the Search button. For example, if the user searches for 'chicken', the results show all recipes with 'chicken' in their name. The form field is required and the user can't submit the form without entering a value. Additionally, when the Search accordion is expanded, the Filter accordion is hidden and its form fields are reset. The Filter accordion is shown again when the Search accordion is collapsed.
- **Filter** - The user can filter recipes based on up to 4 categories, and the results are subsequently diplayed when the user clicks the Filter button. At least one options is required and the user can't submit the form without selecting any options. Additionally, when the Filter accordion is expanded, the Search accordion is hidden and its form fields are reset. The Search accordion is shown again when the Search accordion is collapsed.
- **Reset Button** - The reset button is available in both the Search and Filter accordions. Clicking the Reset button refreshes the 'Browse' page and restores its default values.
- **Recipe Count Helper Text** - The helper text displays the recipe count for the default, filtered and search results. If no recipes are found, the text confirms this. If 1 recipe is found, the text confirms this. If more than 1 recipe is found, the text confirms the count and states they are sorted by most liked. *_Recipes are sorted by most liked first, then A-Z on the recipe name_*
- **Recipe Preview Cards** - Each preview card shows the relevant recipe's picture, recipe name and some quick stats (number of views, number of likes and average rating). Clicking either the recipe image or name takes the user to that recipe's page with its full details.
- **Pagination** - The Browse page uses pagination for the unfiltered results to display 8 recipes per page. The previous page button is only available if there is a previous page. The next page button is only available if there is a next page. *_Pagination isn't currently available for search results, and a bug currently prevents the pagination from working for filtered results_*
- **Add Recipe** - Create operation. Allows the user to add a new recipe to the site and database. All form fields, except the file input field, are required. If an image isn't submitted, the relative filepath for a stock image is added to the new record in the database. If an image is added, it is uploaded to the 'img' directory in the local workspace and the image's relative filepath is added to the database. Additionally, the new recipe's ObjectID is added to the user's added list in the database, which is subsequently pulled through on their profile page.
- **Add New Ingredient/Instruction Row** - This button is shown on the Add Recipe and Edit Recipe pages. Allows the user to add a new ingredient or instruction row. Each new row is required and the user cannot submit the form without entering a value in it, or removing the empty row.
- **Remove New Ingredient/Instruction Row** - This button is shown on the Add Recipe and Edit Recipe pages. Allows the user to remove the last ingredient or instruction row. The button will only function if the row count is greater than one.
- **Cancel Button (Add Recipe Page)** - Cancels the form submission when clicked and redirects the user to the Home page.
- **View Recipes** - Read operation. Displays the recipe's full details on a page. If the recipe hasn't been edited, the added date is displayed. If it has been edited, the last edited date is displayed instead.
- **Print Recipe Button** - On the View Recipes page, the user can print the details for that particular recipe by clicking the Print button. The Print button is available at all times, even when the user isn't logged in.
- **Edit Recipe Button** - The Edit button is available only when the user is logged in. Clicking it takes the user to the Edit Recipe page.
- **Edit Recipe** - Update operation. All exisiting recipe values are pre-populated in the relevant form fields, which the user is able to edit if required. Upon form submission, the recipe database record is updated with the new values. Additionally, the last edited date field in the recipe record is updated with the current date.
- **Remove Current Ingredient/Instruction Row** - This button is shown to the right of each ingredient and instruction row in the Edit Recipe form. This button allows the user to remove that particular ingredient or recipe row when clicked. The button will only function if the row count is greater than 1.
- **Cancel Button (Edit Recipe Page)** - Cancels the form submission when clicked and redirects the user back to the relevant Recipe Page.
- **Delete Recipe** - The Delete button is only available if the user is logged in and they have added that recipe. Clicking the button triggers the Delete modal, which asks the user to confirm the deletion request. If the user presses 'YES', the 'deleted' field in the recipe's database record is updated to 'True', which ensures that the recipe is no longer displayed on the app, although the record isn't removed from the database. Additionally, the recipe is removed from the user's list of added recipes, and also from all other users' list of liked recipes.
- **Rate Recipe** - The Rate It button is only available if the user is logged in. Clicking the Rate it button triggers the Rate It modal. The modal has a dropdown menu from which the user can select their rating. The user can't submit the form without selecting an option. Upon form submission, the rating value is converted to an integer and is added to the recipe record's 'rating_values' list in the database, and the new average rating value and rating count are calculated and displayed on the webpage.
- **Like Recipe** - The Like button is only available if the user is logged in. Clicking the Like button adds the recipe's ObjectID to the user's liked recipes list in the database, the button icon is filled in and the text changes to 'Liked'.
- **Unlike Recipe** - The Liked button is only available if the user is logged in and has already liked the recipe. Clicking the button removes the recipe's ObjectID from the user's liked recipes list in the database, the button icon is no longer filled in and the text changes back to 'Like'.

### Features Left to Implement

With more time and knowledge, I would like to implement some additional features to the app.

- **Search Results Pagination** - I would like to add pagination for the search results. At present, the database doesn't have many entries, so the page doesn't get too crowded with the search results. However, as the site grows and more users add recipes, pagination would be required to improve UX.
- **Working Pagination for Filter Results** - At present, the pagination for the filter results doesn't work as intended due to a bug (explained in the [Interesting Bugs Or Problems](#Interesting-Bugs-Or-Problems) section). This doesn't currently cause any problems with there only being a small number of recipes, but this will need to be resolved as the site grows and the filter results return more than 8 recipes.
- **Pagination Page Numbers and Truncation ** - I would like to add a feature where users can select a page number to navigate to, rather than having to use the previous and next page buttons. Additionally, I would like to truncate this if the pagination gets too long so that it doesn't take too much space on the page. This will improve UX as the site grows and there are more recipes and pages to navigate through.
- **Select Sort By Value** - I would like to add a feature which allows users to sort recipes or search on filter results by different categories. At present, the recipes are sorted by the most liked first, followed by the recipe name. Giving users the ability to select how the results are sorted will allow them greater flexibility to find recipes based on their needs.
- **Change Forgotten Password** - At present, the user can only change their password when they are logged in. If a user forgets their password, they won't be able to login or reset their password. With this in mind, I would like to implement the feature to allow the user to reset their password if they have forgotten it.

## Technologies Used

- [**Balsamiq**](https://balsamiq.com/)
    - I've used **Balsamiq** to create wireframes of my website/app before building it.
- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - The project uses **HTML** to create the basic elements and content of my app.
- [**SCSS**](https://sass-lang.com/documentation/syntax)
    - The project uses **SCSS** to add custom styles to the elements and content of my app. I used **SCSS** instead of **CSS**, as it is more powerful and I used the logic to write some variables, mixins and media queries, which I called for various features.
- [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
    - The project uses **CSS** to apply the custom styles created with **SCSS** to my app. The base.html file is linked directly to the main.min.css stylesheet.
- [**Materialize**](https://materializecss.com/)
    - The project uses the **Materialize** framework to add a responsive grid system, prebuilt components, plugins built on jQuery, and Materialize styles to my app, before adding my custom styles.
- [**jQuery**](https://jquery.com)
    - The project uses **jQuery** as the primary JavaScript functionality. This is both the standard jQuery that is built with Materialize components, and my custom jQuery used in my script.js file.
- [**Python**](https://www.python.org/)
    - The project uses **Python** as the back-end programming language for my app.
- [**PyMongo**](https://api.mongodb.com/python/current/)
    - The project uses **PyMongo** as the Python API for MongoDB. This API enables linking the data from the back-end database to the front-end app.
- [**Flask**](https://flask.palletsprojects.com/en/1.0.x/)
    - The project uses **Flask**, which is a Python microframework.
- [**Jinja**](https://jinja.palletsprojects.com/en/2.10.x/)
    - The project uses **Jinja** for templating with Flask in the HTML code. I used **Jinja** to simplify my HTML code, avoid repetition, and allow simpler linking of the back-end to the front-end.
- [**MongoDB**](https://cloud.mongodb.com/)
    - The project uses **MongoDB** to store the database in the cloud. The information displayed in the front-end app is pulled from the database store.
- [**Google Fonts**](https://fonts.google.com/)
    - The project uses **Google Fonts** to style the text and suit my chosen theme. The brand logo uses the *_Dancing Script_* font and the rest of the site uses the *Roboto_* font.
- [**Font Awesome**](https://fontawesome.com/)
    - The project uses **Font Awesome** for the various icons in my app.
- [**AWS Educate Cloud9**](https://aws.amazon.com/education/awseducate/)
    - I've used **AWS Educat Cloud9** as the development environment to write the code for my website.

### Version Control

- [**Git**](https://git-scm.com/)
    - I've used **Git** as a version control system to regularly add and commit changes made to project in Cloud9, before pushing them to GitHub.
- [**GitHub**](https://github.com/)
    - I've used **GitHub** as a remote repository to push and store the committed changes to my project from Git. I've also used GitHub pages to deploy my website/app in a live environment.

### Hosting
- [**Heroku**](https://www.heroku.com/)
    - I've used **Heroku** as the hosting platform to deploy my app.

## Testing

### Testing User Stories

I used my user stories and documented each of the steps that each user would need to complete to accomplish what they have stated. Below is the link to the document that contains this information:

- [Testing User Stories](https://github.com/hebs87/cookbook-milestone-project-three/blob/master/cookbook/testing/testing-user-stories.pdf)

### Responsive and Functional Testing

I used Google Chrome's Development tools to constantly test each change that I made to my project and to ensure that it appeared in the desired way on different screen sizes. I also tested my app on different screen sizes (mobile, tablet and desktop) to ensure it appeared in the desired way on different devices.

I created my own account and several fake user accounts to test the functionality and validation worked as expected.

To test my whole app, I went through each feature and documented the results on a spreadsheet. The spreadsheet also documents any responsive features and confirms that they work and appear as intended on different screen sizes. The link to the spreadsheet it below:

- [Testing Checklist](https://github.com/hebs87/cookbook-milestone-project-three/blob/master/cookbook/testing/testing-checklist.pdfs)

### Additional Testing

In addition to my own testing, I also asked family members, friends and the Slack community to test my game and provide any feedback.

### HTML, CSS, jQuery and Python Validation

- I used the [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) to validate my HTML code.
    - The W3C Validator tool doesn't recognise the Jinja templating, which has resulted in it showing a lot of errors in relation to the Jinja code. However, all other code is validating fine.
- I used the [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate my CSS code.
- I used the [Esprima Syntax Validator tool](http://esprima.org/demo/validate.html) to validate my JavaScript syntax.
- I used the [Pep8 Online tool](http://pep8online.com/) to validate my Python syntax.

### Interesting Bugs Or Problems

- **Accessing Nested list in Database** - The categories field in my recipes collection is a dictionary with a nested 
- **** -
- **** -
- **** -
- **** -
- **** -
- **** -
- **** -
- **** -
- **** -
- **** -
- **** -

## Deployment

The hosting platform that I've used for my project is Heroku. To deploy my website to Heroku, I used the following steps:

### Repository Link

Click the link below to run my project in the live environment:

[]()

### Running Code Locally

To run my code locally, users can download a local copy of my code to their desktop by completing the following steps:

## Credits



### Content



### Media



#### Sounds



### Acknowledgements



### Disclaimer

This project is for educational purposes only.