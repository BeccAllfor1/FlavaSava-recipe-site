
<h1 align="center">Flava Sava</h1>

<p align="center">
<img src="INSERT RESPONSIVE WEBSITE IMAGE HERE" width="600" height="100%">
</p>

This is a full-stack framework project built using Django, Python, HTML and CSS. Our goal is to create a functioning and responsive website, that allows users to post, comment and like or unlike cost-effective recipes. This project has been built for educational purposes.

# About
Flava Sava is a website where users can comment, like and view recipes and also share their own cost-effective and budget-friendly recipes with other users that are looking for fresh ingredients with impactful full-flavour recipes.
This page is intended for anyone and everyone who are looking for inspiration in preparing cheap but delicious meals during a period of economic austerity.

# Table of Contents 
1. [UX](#ux)
    - [User Stories](#user-stories)

2. [Scope](#scope)
    - [Features](#features)
    - [Future Features](#future-features)

3. [Structure](#structure)

4. [Wireframes](#wireframes)

5. [Database schema](#database-schema)

6. [Surface](#surface)

7. [Technologies Used](#technologies-used)

8. [Testing](#testing)

9. [Deployment](#deployment)

10. [Credits](#credits)

#
# UX
Using the core UX principles we first started with Strategy, thinking about the target audience & the features they would benefit from.

The target audience for 'Flava Sava' are:

- all age groups but mostly avid cooks/chefs, adults
- everyone who is looking for inspiration in preparing cost-effective yet flavourful meals
- people who like to share their delicious budget-meal creations with others
- people who are not financially able to spend lavishly on cooking ingredients but enjoy good flavour


These users will be looking for:
- An informative website, with information that is easy-to-find & concise
- A website that offers cost-effective and flavourful meals with simple ingredients
- Ability to make a user account in order to interact with the site content
- Ability to save liked recipes for later use
- Ability to post, comment and like recipes

This website will offer all of these things whilst also allowing for intuitive navigation and conformability of use.

## User Stories 

**Epic: User Registration and Authentication**
- As a new user I can register an account so that I can access and contribute to the recipe sharing site
- As a registered user I can log in to my account so that I can access personalised features of the site
- As a registered user I can reset my password if I forget it so that I can regain access to my account

**Epic: Viewing and Searching Recipes**
- As a logged-in User I can view a list of recipes so that I can browse through available recipes
- As a logged-in User I can view detailed information about a recipe so that I can see the full ingredients and cooking steps
- As a logged-in User I can search for recipes by keyword so that I can find specific recipes quickly

**Epic: Recipe Management**
- As a logged-in User I can edit my existing recipes so that I can update or amend them
- As a logged-in User I can delete my recipes so that I can remove any unwanted recipes that I have posted
- As a logged-in User I can comment on recipes so that I can share my thoughts or feedback

**Epic: User Profile Management**
- As a logged-in User I can view my profile so that I can see my personal information and contributed recipes
- As a logged-in User I can edit my profile information so that I can update my personal details
- As a logged-in User I can delete my account so that I can remove my presence from the site

**Epic: Administrative Features**
- As a site Admin I can access the dashboard so that I can manage users and content on the site
- As a site Admin I can moderate recipes and comments so that I can ensure the site content meets community guidelines


#
# Scope 

## **Features**

### **Home Page**
*Navigation bar:* 
- The navigation bar appears on every page so users can easily navigate through the site
- Navigation bar has links for 'Home', 'Recipes' and 'Login/Register' more links will be shown to logged in users
- If the user is logged in then the left side of the menu shows links for pages that only authorized users can visit and use, they are: 'Favorite Recipes', 'Your Recipes' and  'Logout'. Otherwise, the user will be given the option to 'Register' or 'Login'
- The user name will also appear on the bar, indicating which user is logged in
- A search bar is nested in the navbar to find recipes quickly
- The navbar is fully responsive, collapsing into a hamburger menu for medium and small screen size

<p align="center">
<img src="INSERT NAVIGATION BAR FEATURES IMAGE HERE" width="100%" height="100%">
</p>


*Hero Image:*
- The hero image welcomes the user with a short message advertising what the website is about
- The Login / Register button will take users to the login page, if users do not have an account there is a link to the registration page

<p align="center">
<img src="INSERT HERO IMAGE HERE" width="100%" height="100%">
</p>


*Recently added recipes:*
- Recently Added section shows the latest published recipes so users can quickly see recently published recipes
- The Recently Added section is fully responsive, showing 4 recipe cards
- Each recipe takes the user to the recipe details page
- Users can also see title, image, author, date posted, short description and number of likes

<p align="center">
<img src="INSERT IMAGE HERE" width="100%" height="100%">
</p>


*Most Loved Recipes:*
- The Most Loved Recipes section displays the top 5 recipes with the most likes
- Each recipe takes the user to the recipe details page
- At the bottom of the list there is a link to the Recipes page that takes users to the page with all the recipes
<p align="center">
<img src="INSERT IMAGE HERE" width="100%" height="100%">
</p>


*Footer:*
- Appears on every page snd contains social links
- Links are opened in a new tab to avoid dragging users from our site
<p align="center">
<img src="INSERT IMAGE HERE" width="100%" height="100%">
</p>

### **Recipes Page**
- The Recipes page shows all the published recipes, recipes are shown in order from newest to oldest
- The site will paginate all recipe cards to display 6 to a page
- Each recipe card will display an image, authors name, date posted, short description and number of likes
- Each recipe card takes users to the recipe details page 
<p align="center">
<img src="INSERT IMAGE HERE" width="100%" height="100%">
</p>

### **Login/Register**
- The Login / Register button takes users to the login page where they can also find a link to the Register page where they can create an account
<p align="center">
<img src="INSERT IMAGE HERE" width="100%" height="100%">
</p>

<p align="center">
<img src="INSERT IMAGE HERE" width="100%" height="100%">
</p>

### **Favorite Recipes Page**
- Only logged in users can see Favorite Recipes Page
- The Favorite Recipes page shows all the recipes that the user liked
<p align="center">
<img src="INSERT IMAGE HERE" width="100%" height="100%">
</p>

### **Your Recipes Page**
- The Your Recipes page displays all the recipes that user has created
- At the top there is an Add Recipe button which takes user to the add recipe page
- Each recipe has two buttons, Edit and Delete
- Edit button takes user to the edit page
- Clicking the Delete button will display the message asking the users if they are sure they want to delete that particular recipe
<p align="center">
<img src="INSERT IMAGE HERE" width="100%" height="100%">
</p>

### **Recipes Details Page**
- The Recipes Details Page displays all the information about the selected recipes
- At the top of the page, the recipe card will display Recipes name, author name, date posted and image
- The main body of the page contains short description of the recipe, ingredients and preparation steps
- Number of likes and comments are displayed after the preparation steps
- Commenting section is located at the end of the page, only logged in users can leave a comment
<p align="center">
<img src="INSERT IMAGE HERE" width="100%" height="100%">
</p>

<p align="center">
<img src="INSERT IMAGE HERE" width="100%" height="100%">
</p>

### **Add Recipe Page**
- On the Add Recipe page users can add their recipes to the website
- The user must fill in all the fields in order for the recipe to be published
- If the user doesn't fill in one of the fields the error message appears
- If the user doesn't provide their image, the default image is displayed
- The Add Recipe button is located at the end of the page
<p align="center">
<img src="INSERT IMAGE HERE" width="100%" height="100%">
</p>

### Future Features
- Categories
- Users settings
- Preparation time
- Notification for likes and comments

#
# Structure
 
Since our target audience is anyone and everyone who is looking for inspiration in preparing budget-friendly meals, the structure idea
for Flava Sava was to keep it simple. Simplicity helps users to quickly and easily access the app and navigate within the app.

The website is made from one app:
- recipes


# Wireframes
All wireframes were created used [Balsamiq](https://balsamiq.com/)

Wireframes for each device are linked here:
- [Desktop](assets/documents/Desktop-wireframes)
- [Tablet](assets/documents/Tablet-wireframes)
- [Mobile](assets/documents/Mobile-wireframes)


# Database schema

<p align="center">
<img src="INSERT DB SCHEME HERE" width="900" height="100%">
</p>

## Models
### **Post Model**

Please note that I am aware of this error. The Post model should be called the Recipe model. But when I wanted to change the name it was already too late because I had already written most of the code. The mentor mentioned to me that I should rename the model, but since the whole code was already written, I felt that changing the name was too much of a risk. I will avoid mistakes like this in the future

<p align="center">
<img src="INSERT IMAGE HERE" width="900" height="100%">
</p>

### **Comment Model**

<p align="center">
<img src="INSERT IMAGE HERE" width="900" height="100%">
</p>


# Surface

## Design 

## Chosen Color 
Color palette from [Coolors](https://coolors.co/9df57a-3c444c-fee73b-ff4f98-2daaf3-a9bedb)
<p align="center">
<img src="INSERT IMAGE HERE" width="800" height="300">
</p>

- **#BBBBBB** - navbar background color. It fits nicely with the hero image.
- **#FFC107** - buttons color. I choose this color because it matches nicely with the rest of the page and it elevates the look of the page
- **#F9F9F9** - body site color. Fits nicely with the rest of the page. I choose this color because normal white color is to bright
- **#F1E3CF**- background color for login/register forms. I choose this color because it fits nicely with side image
- **#484747** - footer background color



## Font 
- Mulish, sans-serif - main font
- Patric Hand- for navbar logo and welcome message


# Technologies Used

## Languages 
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Python](https://www.python.org/)


## Frameworks, Libraries & Programs Used
[GitHub](https://github.com/) - Holds the repository of my project, GitHub connects to GitPod and Heroku.

[GitPod](https://gitpod.io/workspaces) – Connected to GitHub, GitPod hosted the coding space, allowing the project to be built and then committed to the GitHub repository. 

[Heroku](https://www.heroku.com/) - Connected to the GitHub repository, Heroku is a cloud application platform used to deploy this project so the backend language can be utilised/tested. 

[Django](https://www.djangoproject.com/) - This framework was used to build the foundations of this project

[Gunicorn](https://gunicorn.org/) - Gunicorn is a pure-Python HTTP server for WSGI applications.

[Dj Database URL](https://pypi.org/project/dj-database-url/) - This allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.

[Bootstrap](https://getbootstrap.com/) - Used to quickly add design to my website, Bootstrap focuses on mobile first design meaning this website is responsive across multiple devices ans screen sizes. 

[Cloudinary](https://cloudinary.com/?utm_source=google&utm_medium=cpc&utm_campaign=Rbrand&utm_content=492438439811&utm_term=cloudinary&gclid=Cj0KCQiAt8WOBhDbARIsANQLp96hTerzfFJ_P9lX0tEYEdtM3tSsYB6fhw-x3wQxOO0oc4hXm-A2ZBUaAptIEALw_wcB) - Used to store images online for the recipe posts. 

[Summernote](https://summernote.org/) Used to add a text area field to the admin setup to enable a list of ingredients and method steps.

[Google Fonts](https://fonts.google.com/https://fonts.google.com/) - provide fonts for the website.

[Font Awesome](https://fontawesome.com/) -was used for icons.

[Balsamiq](https://balsamiq.com/) - was used to create site wireframes.

[Am I Responsive](http://ami.responsivedesign.is/) - to check if the site is responsive on different screen sizes.

[Pixabay](https://pixabay.com/) and [Unsplash](https://unsplash.com/) - were used for all the images

[W3C Markup Validator](https://validator.w3.org/#validate_by_input) - was used to validate HTML

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - was used to validate CSS

[Beautify](https://www.jpkc.com/tools/beautify/) - was used to correct indentation issues and get rid of too much whitespace - HTML, CSS

[Coolors](https://coolors.co/9df57a-3c444c-fee73b-ff4f98-2daaf3-a9bedb) - to make color palette


# Testing


## User Story Testing

### **Testing Users Stories form (UX) Section**

**EPIC: User Registration and Authentication**
1. As a new user I can register an account so that I can access and contribute to the recipe sharing site
<p align="center">
<img src="INSERT IMAGE HERE" width="500" height="300">
</p>

2. As a registered user I can log in to my account so that I can access personalised features of the site
<p align="center">
<img src="INSERT IMAGE HERE" width="500" height="300">
</p>

3. As a registered user I can reset my password if I forget it so that I can regain access to my account
<p align="center">
<img src="INSERT IMAGE HERE" width="500" height="300">
</p>

**EPIC: Viewing and Searching Recipes**
1. As a logged-in User I can view a list of recipes so that I can browse through available recipes
<p align="center">
<img src="INSERT IMAGE HERE" width="500" height="300">
</p>

2. As a logged-in User I can view detailed information about a recipe so that I can see the full ingredients and cooking steps
<p align="center">
<img src="INSERT IMAGE HERE" width="300" height="200">
</p>

3. As a logged-in User I can search for recipes by keyword so that I can find specific recipes quickly
<p align="center">
<img src="INSERT IMAGE HERE" width="300" height="200">
</p>

**EPIC: Recipe Management**
1. As a logged-in User I can edit my existing recipes so that I can update or amend them
<p align="center">
<img src="INSERT IMAGE HERE" width="600" height="100%">
</p>

2. As a logged-in User I can delete my recipes so that I can remove any unwanted recipes that I have posted
<p align="center">
<img src="INSERT IMAGE HERE" width="500" height="100%">
</p>

3. As a logged-in User I can comment on recipes so that I can share my thoughts or feedback
<p align="center">
<img src="INSERT IMAGE HERE" width="600" height="100%">
</p>

**EPIC: User Profile Management**
1. As a logged-in User I can view my profile so that I can see my personal information and contributed recipes
<p align="center">
<img src="INSERT IMAGE HERE" width="600" height="100%">
</p>

2. As a logged-in User I can edit my profile information so that I can update my personal details
<p align="center">
<img src="INSERT IMAGE HERE" width="600" height="100%">
</p>

3. As a logged-in User I can delete my account so that I can remove my presence from the site
<p align="center">
<img src="INSERT IMAGE HERE" width="1000" height="100%">
</p>

**EPIC: Administrative Features**
1. As a site Admin I can access the dashboard so that I can manage users and content on the site
<p align="center">
<img src="INSERT IMAGE HERE" width="1000" height="100%">
</p>

2. As a site Admin I can moderate recipes and comments so that I can ensure the site content meets community guidelines
<p align="center">
<img src="INSERT IMAGE HERE" width="600" height="100%">
</p>

This was tested by accessing the Django Admin Panel. By creating a Superuser we can access the Django Admin Panel where the administrator can perform all the CRUD functionalities


## Bugs and Issues
- I had a problem where summernote field for preparation_steps wasn't loading. 
The error was corrected by deleting the unnecessary space after the quotation marks indicating the summernote field

- Error - my search engine could not search recipes by title. The mistake was in writing _icontain where there should be two __ I listed one _. 
I fixed the error bu adding another _ to __icontain

- Your_recipes page 404 - I had a problem when I tried to get your_recipes page it displays page 404. After checking that everything is correctly related to the names entered and I still haven't found the bug, I contacted tutor support. The problem was in Chrome, your_recipe page is loading in every other browser. The mistake was in my chrome extensions.

- Pagination was not working. Upon checking the django documents I realised I hadn't coded pagination correctly for Class views. Using the documentation I corrected the mistake.

- User image uploads weren't uploading to Cloudinary. To fix this I added {% load cloudinary %} at the top of the file

# Deployment
This project was deployed using Github and Heroku.

## Github 
To create a new repository I took the following steps:

- Logged into Github.
- Clicked over to the ‘repositories’ section.
- Clicked the green ‘new’ button. This takes you to the create new repository page.
- Once there under ‘repository template’ I chose the code institute template from the dropdown menu.
- I input a repository name then clicked the green ‘create repository button’ at the bottom of the page.
- Once created I opened the new repository and clicked the green ‘Gitpod’ button to create a workspace in Gitpod for editing.

## Django and Heroku 
- To get the Django framework installed and set up I followed the Code institutes [Django Blog cheatsheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)

# Credits

- [Summernote](https://github.com/summernote/django-summernote) - I learn how to change summernote toolbar
- [Code Institute](https://codeinstitute.net/ie/) - 'I think therefore I blog' project helped me with recipe details page and pagination
- [Django documentation](https://docs.djangoproject.com/en/4.0/topics/pagination/) - also helped me with pagination and other problems
- [Search bar](https://www.teckiy.com/blog/implementation-of-search-bar-using-django-in-any-website-2936659075/) - this site is used to help me build Search bar
- [Taste](https://www.taste.com.au/) - all recipes were taken from Taste


## Media
- All images were taken from[Pixabay](https://pixabay.com/) and [Unsplash](https://unsplash.com/)


## Acknowledgements
- Thanks to Code Institute and our mentor
- The Budget Byte Coders Team - Rebecca Allford, Mohammad Usman Butt, Ernest Dapaah, Stuart Preston, Henry Egedegbe