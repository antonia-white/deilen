# Deilen

This website is a full stack ecommerce store to allow people to buy house plants and plant related homeware from the mockup plant company Deilen (the Welsh word for 'leaf').

To visit the website, please visit the deployed site [here](insert link to deployed site).

![Responsive Mockup](documentation/testing/responsive-mockup.png)

***

## User Stories

As a user of the Deilen website, I want to:
  1. ?
  2. ?
  3. ?
  4. ?
  5. ?
  6. ?
  7. ?
  8. ?

***

## UX

### Colour Scheme
- A earthy and natural blend of greens, browns and greys. This gives the website a fresh, organic and natural look.
    >![colour palette](documentation/testing/color-palette.png)
- No accessibility issues were returned when passing the colour scheme through the official [WebAIM](https://webaim.org/resources/contrastchecker/).
    >![webaim screenshot](documentation/testing/webaim-screenshot.png)

### Typography

- Google Fonts
  Font styles were taken from the open source [Google Fonts](https://fonts.google.com/).
  - the typography for the text throughout the website is [Font Name](Link To Font). Small blurb about font.
  - The typography for the brand logo is font-family [Font Name](Link To Font). Small blurb about font.

***

### Wireframes

- Home wireframe

 ![Home wireframe](documentation/wireframes/deilen-homepage-wireframe.png)



 - Products wireframe

 ![Products wireframe](documentation/wireframes/deilen-all-products-wireframe.png)



 - Shopping bag wireframe

 ![Shopping bag wireframe](documentation/wireframes/deilen-shopping-cart-wireframe.png)

 

***

## Database Model
- Database schema for Deilen

 ![database schema](documentation/wireframes/deilen_schema.png)

***

## Features 

### Existing Features 

__Feature__

  - Describe the feature and what it allows a user to do.
  - Does the feature have any defensive programming?

  ![Picture of feature](documentation/testing/example.png)


### Admin Features

Description of what admins have control over

__Feature__

  - Describe the feature and what it allows a admin to do.
  - Does the feature have any defensive programming?

  ![Picture of feature](documentation/testing/example.png)


### Features Left to Implement 

- Describe the feature
  - Why hasn't it yet been implemented and what steps would you take to start implementing this feature.


***

## Technologies
- [HTML](https://en.wikipedia.org/wiki/HTML) was used as the markup language
- [CSS](https://en.wikipedia.org/wiki/CSS) was used for custom styling
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for custom website interactivity
- [GitPod](https://gitpod.io) was used as a cloud based iDE
- [GitHub](https://github.com/) was used to manage the Git repository
- [Heroku](link to deployed site) was used for deployment
- [Git](https://git-scm.com/) was used for version control
- [Python](https://www.python.org/downloads/) used as ...
- [Django](https://www.djangoproject.com/) used as ...
- [Pip3](https://pip.pypa.io/en/stable/) was the package manager used to install the dependencies
- [Bootstrap](https://getbootstrap.com/) was used for website layout and responsive components
- [Google Fonts](https://fonts.google.com/) was used to provide website fonts and icons
- [Am I Responsive](http://ami.responsivedesign.is/) was used to generate a mock-up image
- [Dev Tools](https://en.wikipedia.org/wiki/Web_development_tools) was used for testing and responsiveness
- [Wireframe.cc](https://wireframe.cc/pro/) was used for creating wireframes
- [DrawSQL](https://drawsql.app/) was used for creating the database schema

***

## Testing

To view all testing documentation, refer to [TESTING.md](TESTING.md).

***

## Deployment

The site was deployed to Heroku. The live link can be found [here](link to deployed site)

The steps to deploy a Heroku app are as follows: 
1.  Log in to Heroku or create an account if required.
2.  Create a Heroku app - select 'New', from the drop-down menu select Create New App. The app name provided must be unique.
3.  Select a region.
4.  Create.
5.  Navigate to the Resources tab and add a Heroku PostgreSQL database.
6.  Access the Settings Tab and find the Config Vars. For this project you will need the following config vars:
    *   MONGO_DBNAME = the name of your mongo database.
    *   MONGO_URI = the uri for your mongo database.
    *   DATABASE_URL = the url of your heroku postgres database.
    *   SECRET_KEY = a secret key for your app.
    *   PORT = 5000
    *   DEBUG = set to 'True' during development and 'False' upon deployment.
    *   IP = Your IP address

  Please see this [official documentation](https://devcenter.heroku.com/articles/config-vars) on Heroku configuration for more details.

7.  Navigate to the Deploy tab.
8.  Select Github as the deployment method.
9.  Follow steps to link to the appropriate GitHub account.
12. If you wish, enable Automatic Deploys for automatic deployment when you push updates to Github. Or alternatively, select the correct branch for deployment from the drop-down menu and click Deploy Branch for manual deployment.

Final steps: 
1. Create a Procfile in your repository containing `web: python run.py` so that Heroku will identify the app as a Python app.
2. Create an untracked file called env.py in your repo and input the config vars you previously established in Heroku.
3. Create a requirements.txt file
    - If you want to freeze your own packages into this file, run `pip3 freeze --local > requirements.txt` in the console.
    - To install only the packages that are already listed in the Deilen repo requirements (if making a local copy/clone) run `pip3 install -r requirements.txt` in the console.

### Cloning

Cloning a repository makes it easier to contribute, fix merge conflicts, add or remove files, and push larger commits. To clone this repository from GitHub to a local computer use the following steps:

1.  On GitHub, navigate to the main page of the repository.

2.  Above the list of files, click Code.

3.  Click Use GitHub CLI, then the copy icon.

4.  Open Git Bash and change the current working directory to the location where you want the cloned directory.

5.  Type git clone, and then paste the URL that was copied from step 3 above - i.e., `git clone https://github.com/antonia-white/deilen.git`

6. Press Enter to create the local clone.

### Forking
A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project.

To fork this project go to the top left of the repository, where you see the Fork Icon and click Fork.  This will create a copy of the repository for you.


## Credits 

### Content 

- All text throughout the website is self-written.
- 

### Media
- 

### Acknowledgements

- My Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN)
- My friends and family for manually testing the site.

***