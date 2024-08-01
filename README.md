# The Sesh Recipes app

The Seesh Recipes App is a web application built using the Django web framework. This app is designed to help users easily sign up, create and view alcoholic and non-alcoholic recipes. It allows users to add, edit, and delete cocktails (which they created).

![Screenshot of how the app looks on different screen sizes](docs/images/multi_screen.PNG)

The live version of this app is located [here](https://sesh-recipes-d4bfd3561a5d.herokuapp.com/)

## Table Of Contents:
1. [Design](#design)
    * [User Stories](#user-stories)
    * [Agile Methodology](#agile-methodology)
    * [Database Diagram](#database-diagram)
    * [Features](#features)
    * [Future Features](#future-features)
    * [Technologies Used](#technologies-used)
    * [Testing](#testing)
    * [Deployment](#deployment)

# User Stories
User stories are a way to define the functionality and features of the cocktail recipe app from the perspective of the end users. Here are some user stories for a cocktail recipe app:
As a user, I want to be able to view and create cocktail recipes so I can make cocktails and share my recipes with other users.

- As a user, I can create an account in the app.
- As a user, I can login or logout from the app, so that can view the list of cocktails created by me and others.
- As a user, I want to be able to add cocktail recipes to the list to be viewed by other users.
- As a user, I should be able to click on the cocktail recipe in the list and see the instructions and ingredients about that cocktail recipe.
- As a user, I can edit an cocktail recipe on the list that I created so that I can update or make changes to that cocktail recipe.
- As a user, I should be able to delete cocktail recipes added by me.
- As a user, I want to be able to easily search for cocktail recipes in list to sperate different cocktail recipes by ingredients.
- As a user, I want to be able to view and edit my cocktail recipes on multiple devices (e.g., smartphone, tablet, web browser) for convenience and accessibility.    


# Agile methodology

GitHub is a powerful platform for version control. In addition it can be effectively used to support agile methodologies. Github Projects was used to track the development of this app using the agile approach. The project can be found [here](https://github.com/users/Paulmayock/projects/1).

# Features

- **User-friendly design:** The app has a container desing which is accessible and user-friendly on various devices, including mobile phones and tablets.
![Accessible and user-friendly design](docs/images/Home_screen.PNG) 

- **User Sign up:** Users can sign up to create a account to add cocktail recipes.
![Registration](docs/images/Sign_up.PNG) 

- **User Sign in:** Users can sign in to their account.
![Sign in](docs/images/Sign_In.PNG)

- **Recipe List:** Users can view the list of cocktail recipes added.
![Recipe List](docs/images/recipes.PNG) 

- **Recipe Details:** Users can click on recipes to view ingredients and steps to making the cocktail selected.
![Recipe Details](docs/images/recipe_details.PNG) 

- **Recipe Search:** User can search cocktail recipes from the list in the search bar. 
![Recipe Search](docs/images/recipe_search.PNG) 

- **Add Recipe:** User who is signed up and logged in can add a cocktail recipe.
![Add Recipe top part](docs/images/add_recipe_top.PNG)
![Add Recipe bottom part](docs/images/add_recipe_bottom.PNG)

- **Edit Recipe:** Users who created recipes can edit their recipes in case a mistake is made when first adding the cocktail recipe. 
![Edit Recipe top part](docs/images/edit_recipe_top.PNG) 
![Edit Recipe bottom part](docs/images/edit_recipe_bottom.PNG)

- **Delete Recipe:** Users who created a recipe can delete it.
![Delete Recipe](docs/images/delete_recipe.PNG) 

- **Forgotten Password** Users who forget their password can email the app admin to has this reset.
![Forgotten Password](docs/images/forgotten_password.png)

# Future Features

Some features I would like to implement in future releases are as follows.
- Add a map so users can search locations of cocktail bars in their area and off-licenses.
- Add a rating system so users can rate cocktails.
- Add a option to add shot/shooter recipes.
- Add a more fixed search engine to search cocktails for time of year(sumemer, winter)