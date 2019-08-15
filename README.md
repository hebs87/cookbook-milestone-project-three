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

## Features

### Functionality

The app uses Python logic to allow users to login, or register for a free account. The app offers **CRUD** operations to allow users to create, read, update and delete food recipes. Users can search for a recipe by name, or they can filter recipes based on various categories. Additionally, users can like recipes and add them to their list for easy access.

I added some additional features that weren't within the scope of the project, as I felt that they offered better interactivity for users.

### Existing Features

- **Flash Messages** - Displayed at the top of the page below the navbar. These messages differ based on user interaction and provides helper messages for users. Each message is displayed for 3000 milliseconds.
- **Login** - Allows existing users to login to their account. The form's username field only accepts alphanumeric values. I've included authorization checks to verify the username and password (hashed password) against the details stored in the database before users can be logged in.
- **Register** - Allows new users to register for a free account. The form's username field only accepts alphanumeric values. I've included checks to ensure that the username doesn't already exist in the database before users are successfully registered. The passwords stored in the database are hashed for security purposes.
- **Logout** - Allows users to logout of their account by clicking the 'Logout' link in the navbar/sidenav. Upon clicking the button, the user session ends.
- **Profile Page** - When logged in, users can visit their profile page to view a list of their added or liked recipes, change their password or delete their account.
- **Added Recipes List** - In the user's profile page, the 'Added Recipes' section displays a list of the user's added recipes. The user can click the image or recipe name to view the full details of that particular recipe. If the user hasn't added any recipes, a generic message is displayed which the user can click to add a recipe (redirects the user to the 'Add Recipe' page).
- **Liked Recipes List** - In the user's profile page, the 'Liked Recipes' section displays a list of the user's liked recipes. The user can click the image or recipe name to view the full details of that particular recipe. Alternatively, the user can click the 'Liked' button to unlike the recipe and remove it from their list. If the user hasn't liked any recipes, a generic message is displayed which the user can click to browse all recipes (redirects the user to the 'Browse' page).
- **Change Password** - In the user's profile page, the 'Change Password' button triggers a modal with a form. The form asks for the user's existing password and new password. I've included authorization checks to verify the existing password (hashed password) against the details stored in the database before the user's password is successfully changed. If the check is successful, the password in the database is updated with the new hashed password.
- **Delete Account** - In the user's profile page, the 'Delete Account' button triggers a modal with a form. The form asks the user to confirm their existing password before deleting their account.I've included authorization checks to verify the existing password (hashed password) against the details stored in the database before the user's account is successfully deleted and their record is removed from the database. When a user's account is deleted, all their added recipes are removed from the site and from other users' liked lists too.
- **Browse** - All recipes are initially displayed when the Browse page first loads. The recipes are displayed in cards with some of the recipe's quick stats.
- **Search** - The user can search for a particular recipe by a keyword in the recipe name, and the results are subsequently diplayed when the user clicks the Search button. For example, if the user searches for 'chicken', the results show all recipes with 'chicken' in their name. The form field is required and the user can't submit the form without entering a value. Additionally, when the Search accordion is expanded, the Filter accordion is hidden and its form fields are reset. The Filter accordion is shown again when the Search accordion is collapsed.
- **Filter** - The user can filter recipes based on up to 4 categories, and the results are subsequently diplayed when the user clicks the Filter button. At least one options is required and the user can't submit the form without selecting any options. Additionally, when the Filter accordion is expanded, the Search accordion is hidden and its form fields are reset. The Search accordion is shown again when the Search accordion is collapsed.
- **Reset Button** - 
- **Recipe Preview Cards** - 
- **Recipe Count Helper Text** - 
- **Pagination** - The Browse page uses pagination for the unfiltered results to display 8 recipes per page. The previous page button is only available if there is a previous page. The next page button is only available if there is a next page. *_Pagination isn't currently available for search results, and a bug currently prevents the pagination from working for filtered results_*
- **Add Recipe** - 
- **Add New Ingredient/Instruction Row** - 
- **Remove New Ingredient/Instruction Row** - 
- **Cancel Button (Add Recipe Page)** - 
- **View Recipes** - Added date/edited date
- **Edit Recipes** - 
- **Remove Current Ingredient/Instruction Row** - 
- **Cancel Button (Add Recipe Page)** - 
- **Delete Recipe** - 
- **Rate Recipe** - 
- **Like Recipe** - 
- **** - 
- **** - 
- **** - 

### Features Left to Implement



## Technologies Used

- [**Balsamiq**](https://balsamiq.com/)
    - I've used **Balsamiq** to create wireframes of my website/app before building it.
- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - The project uses **HTML** to create the basic elements and content of my game.
- [**SCSS**](https://sass-lang.com/documentation/syntax)
    - The project uses **SCSS** to add custom styles to the elements and content of my game. I used **SCSS** instead of **CSS**, as it is more powerful and I used the logic to write some variables and mixins, which I called for my fonts and button styles.
- [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
    - The project uses **CSS** to apply the custom styles created with **SCSS** to my game. The index.html file is linked directly to the main.css stylesheet.
- [**Bootstrap**](https://getbootstrap.com/)
    - The project uses the **Bootstrap** framework to add a responsive grid system, prebuilt components, plugins built on jQuery, and Bootstrap styles to my game, before adding my custom styles.
- [**JavaScript**](https://www.javascript.com/)
    - The project uses **JavaScript** from my custom script.js file to add functionality and interactivity to my game. This is the core focus of this project. The project also uses **JavaScript** from Bootstrap which is required to add functionality to the Bootstrap modal.
- [**jQuery**](https://jquery.com)
    - The project uses **jQuery** to simplify DOM manipulation. This is both the standard jQuery that is built with Bootstrap components, and my custom jQuery used in my script.js file.
- [**Google Fonts**](https://fonts.google.com/)
    - The project uses **Google Fonts** to style the text and suit my chosen theme.
- [**Font Awesome**](https://fontawesome.com/)
    - The project uses **Font Awesome** for the instructions and sound icons in the header of my game website/app.
- [**Cloud9**](https://c9.io/login)
    - I've used **Cloud9** as the development environment to write the code for my website.
- [**Jasmine**](https://jasmine.github.io/)
    - The project uses Test Driven Development (TDD) using the **Jasmine** framework to automate some testing of my **JavaScript** code.

### Version Control

- [**Git**](https://git-scm.com/)
    - I've used **Git** as a version control system to regularly add and commit changes made to project in Cloud9, before pushing them to GitHub.
- [**GitHub**](https://github.com/)
    - I've used **GitHub** as a remote repository to push and store the committed changes to my project from Git. I've also used GitHub pages to deploy my website/app in a live environment.

## Testing



### Testing User Stories

I used my user stories and documented each of the steps that each user would need to complete to accomplish what they have stated. Below is the link to the document that contains this information:

- [Testing User Stories]()

### Responsive Testing

I used Google Chrome's Development tools to constantly test each change that I made to my project and to ensure that it appeared in the desired way on different screen sizes. I also tested my game on different screen sizes (mobile, tablet and desktop) to ensure it appeared in the desired way on different devices.

To test my whole app, I went through each feature and documented the results on a spreadsheet. The spreadsheet also documents any responsive features and confirms that they work and appear as intended on different screen sizes. The link to the spreadsheet it below:

- [Testing Checklist]()

### Additional Testing

In addition to my own testing, I also asked family members, friends and the Slack community to test my game and provide any feedback.

### HTML and CSS Validation



### Interesting Bugs Or Problems



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