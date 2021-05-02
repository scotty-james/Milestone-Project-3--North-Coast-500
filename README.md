Welcome to the North Coast 500 - a Review Site for travellers embarking on Scotland's WORLD FAMOUS Road Trip! 

I built this travel information and review site for my third milestone project for the Code Institutes Full Stack Software Development Course.

![Responsive Designs](static/images/readme_images/readme_image1.png)

### <p align="center">The image above is a visual of the site displayed on different devices using [I Am Responsive](http://ami.responsivedesign.is/#)

### <p align="center">You can view the live site here: [www.northcoast500.com](https://north-coast-500.herokuapp.com/)

---


## Contents

- [**User Experience (UX)**](#ux)
  - [User Stories](#user-stories)
  - [Strategy](#strategy)
    - [_External user’s goal_](#external-user’s-goal)
    - [_Site owner's goal_](#external-user’s-goal)
  - [Scope](#scope)
    - [_Scope In_](#scope-in)
    - [_Scope Out_](#scope-out)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
    - [_Wireframes_](#mobile-wireframes)
  - [Surface](#surface)
    - [_Design_](#design)
    - [_Colour_](#colour)
    - [_Typography_](#typography)
- [**Features**](#features)
  - [_Existing Features_](#existing-features)
  - [_Features Left to Implement_](#features-left-to-implement)
- [**Technologies Used**](#technologies-used)
  - [_Languages_](#languages)
  - [_Frameworks & Libraries_](#frameworks-and-libraries)
- [**Testing**](#testing)
- [**Version Control Management**](#version-control-management)
- [**Deployment**](#deployment)
  - [_Deployment Steps_](#deployment-steps)
  - [_How To run this Project Locally_](#how-to-run-this-project-locally)
- [**Credits**](#credits)
  - [_Content_](#content)
  - [_Media_](#media)
  - [_Code_](#code)
- [**Resources**](#resources)
- [**Acknowledgements**](#acknowledgements)

---

## <p align="center"> UX

### User Stories

> - As a new website user, I want to understand the website purpose easily so that I remain interested in exploring the site further. 
> - s a new website user, I want to understand the reasons why I need to create an account so that I can make a decision on the value of doing so. 
> - As an existing user I want to be able to create and update my own personal reviews so that I have full control on the content I submit. 
> - As an existing user I want to be able to delete any review I have submitted so that I have full control on the content I submit. 
> - As an existing user, I want to be able to log out at any point when I am finished so that I know my account is secure. 

### Strategy

#### External user’s goal

- Read the reviews of others who have experienced the route in order to gain real life reviews that can help me make a decision. 
- Creating an account should be simple and quick, requiring as little personal information as possible.  -
-  Share my own experience with others by submitting reviews and rating my trip. 
- Access additional information outside the website to explore further and gain more insight (links to external sources, dedicated websites etc)


#### Site owner's goal

- Built a site that provides specific information to a targeted audience. 
- Create a site that allows users to submit reviews in order to share their experience with others. 
- Create a site that allows users to manipulate their review input by being able to update or delete their previous posts. 
- Create a site that is user friendly and provides the targeted user with inspiration and links to further information.


### Scope

#### Scope In

- A homepage that provides information about Scotland's north coast 500 road trip route, including the key stopping points along the route. 
- A visual image of the route above the fold on the website to draw the user’s initial attention to the route map and key stops along the way. 
- External links to all information outlines on the home page to allow the user to gain deeper information should they want to. 
- Provide information on places to stay, food and drink, beaches and coastal regions of the route, and scotland’s wildlife likely to be encountered along the route. 
- A review page containing all reviews submitted by other users. 
- Ability for new users to create an account on the site. 
- Ability for existing users to log into their account.
- A review form that allows users to create and submit a review. 
- An edit review form that allows users to update previously posted reviews. 
- A delete review form that allows users to remove previously posted reviews. 
- Ability to log out of the site. 

#### Scope Out

- Customer profile page
- Ability to like or add comments to other users' reviews. 
- Search functionality to allow users to search reviews. 


### Structure

The structure of information on the site will follow a very simple design and navigation flow. As an information based website, the goal is to make the siete as easy as possible for the user to navigate.  
#### Home Page
- Main page with key relevant information on the website's purpose - the North Coast 500 road trip route. A map of the route is displayed above the fold to instantly allow the user to visualize the route as soon as they enter the website. 
- A link directing the user to the dedicated review page is also above the fold to allow customers to instantly navigate to this page if they wish to do so. 
#### Sign Up Page
- Contains the form that allows a new user to create an account. 
#### Sign In Page
- Contains the form that allows existing users to sign into their account.
#### Reviews Page
- A dedicated page containing the reviews posted by users of the site. This page is populated using the data submitted by users filling in a review form and submitting the review to the site.
#### Add Review Form
- An ‘ADD Review’ Tab is placed in the nav bar which allows the user to submit a review directly on the website. 
-- The Add Review Tab displays in the nav bar whether or not the customer is logged in, however, in the event the user is not logged in, when clicked a model will appear prompting the user to either sign in or create an account. If the user is logged in, they are directed straight to the review form. 
#### Edit Review & Delete Form
- Both of these forms are located within the reviews page and display only when the user is logged in and has previously submitted at least one review. 
Sign Out Tab
- This nav bar link allows the user to sign out of their account and will only display on the navbar if a user has signed into their account.
#### Footer 
- A fixed footer that contains additional information and navigational options for both new and existing users of the site. 


### Skeleton

- The website has been designed to allow the user to navigate through the journey effortlessly. 
- The nav bar links are designed to display relevant to whether the user is logged into the site or not. 
- The user will be immediately navigated to the main reviews page upon submitting a review. 
- When attempting to delete a review, the user will be navigated to a dedicated page that will provide additional protection in case the user clicked delete by mistake. 
- The user will flow to the login page after clicking the logout button, enabling them to log back in quickly if this was done in error. 


#### Wireframes

All wireframes were created using [Balsamic](https://balsamiq.com/).

### Surface

#### Design

The website’s sole purpose is to display information and reviews on Scotland’s north coast 500 road trip. This is an extremely scenic route through the Scottish mountains and around 500 miles of coastline. Therefore, the page is designed for lots of images. The main page has many images of the route to engage with the user as they are most likely on the page to help plan and visualise their dream road trip. 

#### Colour

The color scheme is very simple, white and blue, using the blue from the Scotish Flag as my inspiration for the site.

- #0065BF

![Colour Palette](static/images/readme_images/colour-palette.png)


#### Typography

Typography
In line with websites simplicity I have only used one font throughout - Righteous! 

![Google Fonts](static/images/readme_images/readme-googlefonts.png)

I really liked the simplicity of Open Sans and therfore didn't feel the need from a design perspective to add any additional fonts. 

---

## <p align="center">Database Set Up

This project relies on having a Database Schema designed in order to operate as intended. The database schema was designed and created using MongoDB. After creating the database, I created three collections - categories, posts, and users, which formed the structure of my database schema.  

### Collections

> The 'USERS' collection is designed to simply accept and store the required user details which are captured when the user creates an account, it contains the following structure:

Document Labels 

| _ID                                                                                              | ObjectId    |
| ------------------------------------------------------------------------------------------------ | ----------- |
| username                                                                                         | String      |
| password                                                                                         | String      |

Capturing the user data is the first step in the database design as a user must first create an account in order to interact with the website and create, edite, delete posts.


> The 'CATEGORIES' collection was designed to take in a specific road trip. For now, the website is based on the North Coast 500 road trip, however, future plans for the website involve building out a community review site where users can share experiences on other popular road trips, like Ireland’s Wild Atlantic Way. The categories collection will allow me to add further road trips which will then allow users choose which Road Trip they would like to review. Adding a new road trip category will be an Admin privilege. 

Document Labels 

| _ID                                                                                              | ObjectId    |
| ------------------------------------------------------------------------------------------------ | ----------- |
| category_name                                                                                    | String      | 



> The 'POSTS' collection was designed to handle the data from the actual review that the user will post to the website. It contains the following: 

Document Labels 

| _ID                                                                                              | ObjectId    |
| ------------------------------------------------------------------------------------------------ | ----------- |
| category_name                                                                                    | String      |
| star_rating                                                                                      | String      |
| post_title                                                                                       | String      |
| post_description                                                                                 | String      |
| image_url                                                                                        | String      |
| created_by                                                                                       | String      |
| review_date                                                                                      | String      |

All of these data points are required on the add review form, a form cannot be submitted without contend added to each of these fields. 

---

## <p align="center">Features

### Existing Features
- A tab that allows users to ‘Add Review’ which is displayed whether the user is logged in or not.
- A model that appears after clicking the ‘Add Review’ Tab if the user is not logged in, the model containing information on how to add a review by either signing in or creating an account. 
- A sign up page that allows new users to create an account, which will allow the user to interact with the site. 
- A sign in page that will allow existing members to sign into their account in order to interact with the site. 
- Flash messaging to warn the user of specific actions - for example, advising the customer that a user name already exists if they try to create an account using a username that has already been taken. 
- Flash messaging to advise the customer that they have successfully created an account. 
- Flash messaging to warn the customer when they enter the wrong username and/or password when signing in. 
- All forms have validation to ensure the user enters the required parameters in each form throughout the site. 
- Password hashing to ensure security is enabled within the site. 
- Flash messaging to welcome the user upon signing in successful, displaying the users name on screen. 
- Add Review tab that displays a form that allows the user to create and submit a review directly onto the dedicated review page. 
- An ‘Update’ tab that appears only on the reviews submitted by the logged in user. The update tab when clicked will allow the user to edit their review. 
- Updated reviews when submitted are reloaded on the main review page within the site. 
- A ‘Delete’ Tab that allows appears only on the reviews submitted by the logged in user. 
- A ‘Cancel’ button on the delete review page that allows the customer to be able to change their mind after clicking the first delete button. 
- Ability to add an image url in the review form that allows users to add and submit an image with their review. 
- A sign out tab that allows the user to sign out of their session, with a flashed message to confirm to the user that sign out has been successful. 
- User ratings select drop down which converts into Star Ratings when the review is submitted. 
- Nav bar that displays certain links only when the user is signed into their account. 


### Features Left to Implement

- A user profile page which will display the users previously submitted reviews. 
- An add comments section which will allow users to ask questions within the community of existing members. 
- A like / helpful button which will allow users to like other users' reviews. 
- Expansion of the website to include other route trip routes around the globe. 
- Ability for users to sign up to email newsletters. 
- Admin functionality that will allow admin to moderate reviews and comments as the community grows. 

---

## <p align="center">Technologies Used

### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Python](https://www.python.org/)
- [JQuery](https://jquery.com/)


### Frameworks and Libraries
- [Pip3](https://pip.pypa.io/) - was used to install the required packages to run python.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Was used as the main micro framework for the web app.
- [WTForms](https://flask-wtf.readthedocs.io/en/stable/quickstart.html) - Was used to create all forms within the app.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - Was used for all templating within python.
- [PyMongo](https://pypi.org/project/pymongo/) - Was used as the Python driver for MongoDB. 
- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) - used for password hashing within the user authentication process. 
- [Datetime](https://docs.python.org/3/library/datetime.html) - used to pull in date automatically when user post submitted to the site.
- [MongoDB](https://www.mongodb.com) - Was used as the primary database for the webapp.
-[Heroku](https://www.heroku.com/) - was used to deploy the webapp. 
[RandomKeygen](https://randomkeygen.com/) - Used to generate a random number which was used as the web app's SECRET_KEY.
- [Materialize](https://materializecss.com/) - was used for the navbar, the footer and the model structure.
- [Google Fonts](https://fonts.google.com/) - used to select the text font to be used throughout the site.
- [Gitpod](https://gitpod.io/) - used as my IDE.
- [Git](https://git-scm.com/) - used for version control via VS code by providing regular commits to Git, and pushing to GitHub.
- [GitHub](https://github.com/) - for my Git repository.
- [Balsamic](https://balsamiq.com/) - used to create the website wireframes.
- [Tinyjpg](https://tinyjpg.com/) - used for image resizing.
- [Favicon Generator](https://favicon.io/favicon-converter/) - used for generating the site favicon.
- [PEP8](http://pep8online.com/) - used to validate the code for the website. 
- [JS Hint](https://jshint.com/) - used to validate the javascript code within the website. 
- [Jigsaw](https://jigsaw.w3.org/css-validator/) - used to vaidate all CSS code. 
- [W3C Markup Validation](https://validator.w3.org/#validate_by_input) - used to validate the HTML within the code base. 

---


## <p align="center">Testing

### W3C Validation

The following pages were passed through the official W3C validation site with no errors returning:

- index.html: No errors or warnings to show.
- posts.html: No errors or warnings to show.
- register.html: No errors or warnings to show.
- login.html: No errors or warnings to show.
- add_post.html: No errors or warnings to show.
- edit_post.html: No errors or warnings to show.
- delete_post.html: No errors or warnings to show.

![HTML Validator Results](static/images/readme_images/html_validator.png)

- style.css: Congratulations! No Error Found.

![CSS Validator Results](static/images/readme_images/css_validator.png)

### JSHint

The following files were passed through JSHint with no warnings detected.

- script.js

### PEP8 Python Validator

The following pages were validated using PEP8 without error. 

- app.py
- forms.py

![PEP8 Validator Results](static/images/readme_images/PEP8_image1.png)


### User Story Testing Validation

> #### <p align="center">_As a new website user, I want to understand the website purpose easily so that I remain interested in exploring the site further. 

I’ve designed the site in a way that as son as the user enters the site they immediately see what the page is about by displaying 3 key images above the fold:
- The large image  on the right displays a road with a car driving along it, instantly articulating a road journey. On this is a clear message to the customer - discovery and share. 
- A button has been added to the image to allow the customer to quickly navigate to the review site in order to read reviews posted by other users. A link to the review page is aslo contained within the nav bar.
- The top image on the right hand side displays a map of the road trip route. 
- The bottom right hand image displays the North 500 route sign. The route is commonly referred to as Scotland's route 66.

#### Home Page

![User Story Image](static/images/readme_images/user_story_image1.png)

#### Review Page
![User Story Image](static/images/readme_images/user_story_image3.png)

> #### <p align="center">_As a new website user, I want to understand the reasons why I need to create an account so that I can make a decision on the value of doing so. 

- To draw attention to the sign in functionality I have emphasised this within the nav bar - boxing it for additional focus. 
- The Sign in page is simple and clear and has been built to allow the customer to sign up at speed. The form is simple and requires the user to provide a username and password only in order to create an account. 

#### Sign In Page
![User Story Image](static/images/readme_images/user_story_image2.png)


> #### <p align="center">_As an existing user I want to be able to create and update my own personal reviews so that I have full control on the content I submit. 

- The add review form allows customers to create and submit their own personal experiences with other site users. The form is simple and easy to fill in and pre-populates with the ‘Route’. This feature only has one option at present but has been built to allow the site owner to add additional routes that users can review.  
- The user can then edit their review once it has been submitted. To do this, the user needs to be logged in to their account to ensure only their review is protected and only they can edit. 
- The user can update their review as many times as they like, and have full control of the content they add or remove. 

#### Review Page
![User Story Image](static/images/readme_images/user_story_image4.png)

#### Add Review Form
![User Story Image](static/images/readme_images/user_story_image5.png)

#### Submitted Review
![User Story Image](static/images/readme_images/user_story_image6.png)

#### Edit Review Form
![User Story Image](static/images/readme_images/user_story_image7.png)


> #### <p align="center">_As an existing user I want to be able to delete any review I have submitted so that I have full control on the content I submit. 

- The user has full control with their content so once they are logged into their account, they have the ability to delete the review by clicking on the delete button underneath their post. 
- Once the delete button is clicked, the use will be directed to a ‘delete post’ page where they will be asked to confirm they wish to delete. 
- The confirm delete page pre populates the review title, providing the user with additional comfort that they have deleted the correct post. 
- There is a cancel button on the page, when clicked will take the customer back to the main reviews page - and of course, keeping the review alive. 

#### Delete Review Page
![User Story Image](static/images/readme_images/user_story_image8.png)

> #### <p align="center">_As an existing user, I want to be able to log out at any point when I am finished so that I know my account is secure. 

- Within the nav bar, the sign out button will appear once the user is logged into the web app allowing the user to log out quickly and easily. 
- Once the user clicks the sign out button, a flash message will appear to let the customer know they have logged out. 
- The user is then redirected to the login page on the site. This redirect is on purpose in case the user accidentally logs out and wishes to log back in. 

#### On Sign Out
![User Story Image](static/images/readme_images/user_story_image9.png)


### Browser Validation

In addition to testing on google chrome, I tested the game fully on the Safari and Firefox browsers.

- Firefox: All tests successful 
- Safari: All tests successful, however, the form size was smaller than expected. I will look at this as part of a future release. 
- Internet Explorer: All tests successful, same view on the form size as safari however, the website is optimised to be run on Chrome. 

### Responsiveness Validation

#### Dev Tools
The project was built with mobile first in mind. Chrome Dev Tools toggle device toolbar was used to check the site on available devices to ensure the webapp was fully responsive. I checked each page individually on each device type. 

#### Manual Device Check:

I checked the site manually on the following devices - all pages check checked separately.
- Samsung S10
- Iphone X
- Macbook Pro 
- Dell Laptop
- Ipad Pro
- Samasung Tablet
- Monitor Screen 

#### Link And Hover Validation
I went through each page individually to manually check that all links & hover styling worked as intended. This test was performed on both mobile and desktop devices. 

- index.html: 
    - First call to action link on the hero image.
    - Nav Bar: Links, add review modal, add review link, sign in button and sign out link.
    - All links contiained within the body of the page (within each section). Each navigation link on all pages were tested both forward and backward to ensure each page was returning as intended. 
    - Footer links: -- All three social links, 'Discover' link and 'Explore link'. All redirects checked to ensure they were correct. 

- get_post.html:
    - Footer links: -- All three social links, 'Discover' link and 'Explore link'. All redirects checked to ensure they wewre correct. 

- login.html:
    - Sign in link and re direct link to create new account.
    - Footer links: -- All three social links, 'Discover' link and 'Explore link'. All redirects checked to ensure they wewre correct. 

- register.html:
    - Sign up link and re direct link to login to existing account.
    - Footer links: -- All three social links, 'Discover' link and 'Explore link'. All redirects checked to ensure they wewre correct. 

- Navbar
    - Tested each navigation link on all pages both forward and backward to ensure each page was returning as intended. 

- Logo: 
    - Test the logo link on each page to ensure navigation back to index.html. 

#### Form Validation

- Sign in form on login.html: 
    - Checked on both mobile, ipad and desktop devices. 
    - Submit form without username added to ensure input field ‘required’ attribute was working correctly and alert displayed prompted customer to add input. 
    - Submit form without password added to ensure input field ‘required’ attribute was working correctly and alert displayed prompted customer to add input.

- Sign up form on login.html: 
    - Checked on both mobile, ipad and desktop devices. 
    - Submit form without email address added to ensure input field ‘required’ attribute was working correctly and alert displayed prompted customer to input email address. 
    - Submit form without name added to ensure input field ‘required’ attribute was working correctly and alert displayed prompted customer to input email address.

- Add Review Form, Edit Review From and Delete Review Form. 
    - Form fully tested by submitted while leaving one input field empty at a time to ensure the correct ‘required’ attribute was returning and now allowing the form to submit without all required fields being filled in. 

- Add Review Form: 
    - Submitted fully filled in review and reviewed on reviews page to ensure review displayed as intended. 
    - Checkded Mongo DB to ensure data captured correctly

- Edit Review Form
    - Submittled fully edited review and reviewed on reviews page to ensure review displayed as intended. 
    - Checkded Mongo DB to ensure data captured correctly

- Delete Review Form: 
  - Submitted form (clicked delete) and reviewed on reviews page to ensure review was removed as intended. 
  - Checkded Mongo DB to ensure data captured correctly

#### Image Validation

-   I went through each page to ensure all images displayed correctly. 
-   I went through each file to ensure all Alt Text had been applied correctly to each image url to validate accessibility requirements. 


### Site Performance Validation

#### First Test

![Lighthouse Report](static/images/readme_images/lighthouse_image1.png)

The first report from lighthouse returned poor scores for Accessibility performance and best practice. Reasons outlined below. 

- Accessibility: Failing Elements were attributed to 2 main areas:
  - Low contrast text on all of the links placed throughout index.html, the color on these links were scoring low so changed the color to the same blue as I have as the main theme for the website, which improved contrast.
  - Some heading elements were not in a sequentially-decedning order (H5), I changed these to provide better HTML structure. 

- Best Practices: Failing elements where:
  - Does not use HTTPS - 19 insecure requests found
  - Links to cross-origin destinations are unsafe: I updated all links by adding `rel="noopener"` within the link structure.

With these issues fixed, the site now returns a healthy lighthouse score across all key measures: 

#### Second Test

![Lighthouse Report](static/images/readme_images/lighthouse_image2.png)

### CRUD Testing: 

To ensure the standards of CRUD testing were met, I tested the following steps to ensure no errors returned. 

#### Create a new user:
- Created new user on the front end website
- Checked mongo DB collection to ensure the user was added to the database. 
- Log in using new users credentials. 
- Log out of the user account. 
- From mongoDB, delete the record manually to remove the record from the database. 
- Go back to the site and log in using users credentials. 
- Verified that the account had been deleted and the user could no longer log in. 

#### Create a new record (Add Review)
- Fill in the Add Review form and submit.
- Go to MongoDB and verify the new record has been added to the database. 

#### Front end:
![Crud Testing](static/images/readme_images/crud_testing_image1.png)

#### Back end:
![Crud Testing](static/images/readme_images/crud_testing_image2.png)

#### Read the review:
- Go to the review page and verify that the submitted review has been posted to the intended place on the website. 

#### Update the Review:
- Got to review and click ‘Update’. 
- Change the review content. 
- Submit update
- Go to the review page and verify that the submitted review has been posted to the intended place on the website. 
- Go to mongo DB and verify that review has been amended in the database. 

#### Front end:
![Crud Testing](static/images/readme_images/crud_testing_image3.png)

#### Back end:
![Crud Testing](static/images/readme_images/crud_testing_image4.png)

#### Delete the review:
- Go to the review and click ‘delete’. 
- Verify that I am redirected to a ‘confirm delete’ page that ensures the user intends to delete the review. 
- Click delete to verify that I want to delete the review. 
- Go to the review page and verify that the submitted review has been removed. 
- Go to mongo DB and verify that the document has in fact been deleted from the database. 

### Error Handling 

To ensure that any site error is handled gracefully, a 404 error handler function was added to the page. The site was tested on all pages to generate the 404 message, which displays a simple message to the user, with a redirect to the home page.

![404](static/images/readme_images/readme_404.png)



### Final Manual UAT Testing

| Functionality                                                                                    | UAT Result |
| ------------------------------------------------------------------------------------------------ | ---------- |
| All navigation links work as intended                                                            | PASS       |
| All links in footer work as intended                                                             | PASS       |
| Review Page Button works as intended                                                             | PASS       |
| All links on home page redirect to correct pages                                                 | PASS       |
| Add review form generates right attribute for missing field input                                | PASS       |
| Add Review form submit button works as intended                                                  | PASS       |
| Add Review when submitted posts to review page                                                   | PASS       |
| Add Review when submitted updates collection in MongoDB                                          | PASS       |
| Add Review when submitted converts star rating number to star icons                              | PASS       |
| Add Review when submitted flashes correct message to user                                        | PASS       |
| Edit Review when clicked pre loads review form                                                   | PASS       |
| Edit Review form when submitted updates content on front end review site                         | PASS       |
| Edit Review Form when submitted updates MongoBD document with new content                        | PASS       |
| Edit Review form when submitted flashes message to user                                          | FAIL       |
| Delete Review Form redirect is functioning as intended                                           | PASS       |
| Delete review when submitted removes post from review page                                       | PASS       |
| Delete review when submitted removes post from MongoDB.                                          | PASS       |
| Delete review when submitted flashes correct message to user                                     | FAIL       |
| Correct message flashes when username inputted incorrectly on login page                         | PASS       |
| Correct message flashes when user attempts to sign in using username that hasn't been created    | FAIL       |
| Correct message flashes when username inputted incorrectly on login page                         | FAIL       |
| Link on login page redirects as intended                                                         | PASS       |
| Correct message flashes when existing username used to make a new account                        | PASS       |
| Correct message flashes when user signs up successfully                                          | PASS       |
| Sign out link redirects to sign in page                                                          | PASS       |
| Correct message displays when user is signed out                                                 | PASS       |

---

### <p align="center"> Fixed Bugs

| Bug | Fix  |
| ---------- | ---- |
| No user messaging when new review submitted, informing them that the review posted successfully | To resolve this, I updated the add_post route in ap.py to call a flash message in the event of a successful submission. Tested and results are now as expected |
| No user messaging when a review has been updated successfully. | To resolve this, I updated the function in app.py (/edit_post route) to include a flash message when form submission is successful. Tested and working ok. |
| No user messaging when a review has been deleted successfully. | To resolve this, I updated the function in app.py (/delete_post route) to include a flash message when form submission is successful. Tested and working ok. |
| 404 error handler returning as intended but with no messaging.  | I had originally used the code from the Flask documentation, copying and pasting the 404.html code also, however, to resolve the issue I removed the following code `{% block title %}Page Not Found{% endblock %} {% block body %} ` and replaced with `{% block content %}`, this resolved the error and returned the correct messaging. 
 |

---

### Remaining Bugs:

---

## <p align="center">Version Control Management

For this project, I used Git for version control.

- All code was written in Gitpod.
- At regular intervals and when new features were added to the site, - I added my files to the staging environment using the `git add .` command.
- I then committed to the local repository using the `git commit -m` command.
- I then pushed the local git to my GitHub repository using the `git push` command.
- Throughout the development lifecycle of the site, I used commit messages that were in the imperative language.

---

## <p align="center">Deployment

### Deployment Steps

This website was deployed using Heroku. The following steps were taken. 

1. Within the IDE, create a requirements.txt file by running the following command in the terminal `pip3 freeze --local > requirements.txt`
1. Next, create a Procfile by running the following command in the terminal `echo web: python app.py > Procfile`
1. Open Heroku and Log in. 
1. Click the ‘NEW’ button at the top right hand corner, select ‘Create New App’.
1. Provide a name for the project (this must be unique), select the region closest to you and click ‘Create App’.
1. In the Deployment Method section, select Github.
1. Select your Github account and type in your repo in the search bar, once selected, connect. 
1. Navigate to the ‘Settings’ tab and click the Reveal Config Vars button. 
1. Now set the variables for IP, PORT, SECRET_KEY, MONGO_URI and MONGODB_NAME. These must match with those in the env.py file.
1. Within the automatic deploys section, select ‘Enable Automatic Deploys’
1. Select ‘Deploy Branch’
1. Heroku will now start to build the app and will display on screen when ready to open. 


### How To run this Project Locally

Mongo DB account set up and connected to this website. 
Pip3 installed on the machine to enable the required packages. 
Python3 (used as primary language)

Steps: 

1. Sign in to MongoDB account.
1. Create a new cluster and database. Within the database, create three collections following this Schema Design. The database name needs to be north_coast.
1. Click here to access the site's repository
Underneath the repository name, click ‘Code’ which will open a drop down menu.
1. Click the HTTPs section (a red line should be displayed underneath).
1. To clone the repository using HTTPS, under "Clone with HTTPS", click the clipboard icon.
1. Open your IDE terminal
1. Type ‘git clone’ and paste in the url you just copied - it should look like this `$ git clone https://github.com/scotty-james/North-Coast-500.git`
1. Press enter which will then create your local clone.
1. You must ensure that all project requirements are downloaded by running the following command `pip3 install -r requirements.txt`
1. Create a new file called `env.py` and set the correct variables for IP, PORT, SECRET_KEY, MONGO_URI and MONGODB_NAME (these must match the variables set in Heroku). 
1. Create a .gitignore file if not already created and ensure env.py and pycache are added. 
1. To open the application, run the following command in the terminal python3 app.py. 
1. To stop running the application at any time, type `CTRL+C` to quit. 

---

## <p align="center">Credits

### Content

### Media

### Code

---

## <p align="center">Resources

- Flask Documentation
- Python Documentation
- Code Institute Slack Community
- Code Institute Course Content completed to date
- W3schools
- Stackoverflow
- MDN Mozilla

---

## <p align="center"> Acknowledgements

- I would like to thank and acknowledge my mentor Spencer Barriball for his usual encouragement throughout the [project and for the helpful tips and recommendations along the way, thank you for your guidance and support!

- The Code Institute Slack Community which continues to be a fantastic resource when troubleshooting. 


---

## <p align="center">Thank you!</p>

