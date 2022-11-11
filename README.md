# Deilen

This website is a full stack ecommerce store to allow people to buy house plants and plant related homeware from the mockup plant company Deilen (the Welsh word for 'leaf').

To visit the website, please visit the deployed site [here](https://deilen-shop.herokuapp.com/).

![Responsive Mockup](documentation/testing/deilen-amiresponsive.png)

***

## Target Audience
  - Homeowners looking to buy decorative house plants.
  - Interior designers looking to buy plants for indoor spaces e.g., an office space.
  - People looking to gift a house plant to a loved one.

## User Stories
  1. User Authentication / Accounts
     - Site users should be able to register an account that allows a user to sign in and out of the site.
     - A user should be able to create a profile to store personal information to make checkout easier with default personal information to automatically populate form fields at checkout.
     - Users should be able to ammend profile information to keep records up-to-date and also have the ability to delete their account.
     - A user should be able to reset their password via email authentication so the account is not lost if the password is forgotten.
  2. Site Navigation
     - Site users should be able to navigate fluidly throughout the website without having to use the back button.
     - A user should be able to direct themselves through the site with confidence and clarity to where they are navigating too.
     - Users should be able to search the site for specific related content that they seek.
  3. Shopping
     -  Users should be able to view the products that Deilen offer for purchase.
     - A user should be able to add any products they want to buy to their bag for review.
     - A user should be able to add multiples of an item to their bag if they so wish.
     - Users should be able to filter and sort results based on their shopping goals.
     - Site users should be able to view all product information before adding a product to their bag.
  4. Bag (Wheelbarrow)
     - Users should be able to view all items, and quantities that they have added to their wheelbarrow.
     - Site users should be able to amend their order in their wheelbarrow, changing the quantities of a product or removing the product entirely from the wheelbarrow.
     - A user should be shown the delivery costs and any additional costs of their order.
     - Users should be able to safely navigate to the checkout to finalise their order.
  5. User Checkout
     - A user should be able to checkout securely and pay for their order, finalising the transaction and confirming delivery address.
     - Site users should be able to checkout and purchase products regardless of if they have a Deilen account or not.
  6. Profiles
      - Site users should be able to create a profile to store their default delivery address, which will auto-populate the checkout view. 
      - Site users should also be able to view their previous order history.
      - Profile users should be able to signin, signout, view their profile and ammend their default delivery information. 
  8.  Site Admin
      - Site admins should have secure access to product manipulation.
      - Admins will be able to add new products.
      - Admins will be able to edit existing products.
      - Admins will be able to delete products from the store.

***

## UX

### Colour Scheme
- A earthy and natural blend of pastel pink yellow and green with darker shadesof clay-brown and blue-grey. This gives the website a fresh, organic and natural look.
    >![colour palette](documentation/testing/deilen-colours.png)
- No accessibility issues were returned when passing the colour scheme through the official [WebAIM](https://webaim.org/resources/contrastchecker/).
    >![webaim screenshot](documentation/testing/webaim-screenshot.png)

### Typography

- Google Fonts
  Font styles were taken from the open source [Google Fonts](https://fonts.google.com/).
  - the typography for the text throughout the website is [Work Sans](https://fonts.google.com/specimen/Work+Sans). This font was designed by Wei Huang and is optimised for on-screen text usage at medium-sizes (14px-48px). Overall, features are simplified and optimised for screen resolutions; for example, diacritic marks are larger than how they would be in print. This font is loosely based on early Grotesques and, in my opinion, gives the website a crisp feel.
  - The typography for the brand logo and page titles is font-family [Corben](https://fonts.google.com/specimen/Corben). Which was designed by Vernon Adams Corben as a simple web friendly display font with ample curves and ligatures. Corben is designed to be easy on the eye with a touch of classic display lettering. For me, Corben gives the logo and headers a classic, sophisticated feel. 
- Accessibility
  The website was designed with accessibility in mind, by providing alt attributes for all img elements and being mindfu of visual impairment when designing the website. For example, originally I had a hover effect to increase font-size on footer links. After consideration this was removed as the hover effect caused verticle displacement.

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

 ![database schema](documentation/wireframes/deilen-schema.png)

***

## Features 

### Existing Features 

__Navigation Bar__
  - Allows the user to navigate around the Deilen site. The Deilen logo will direct the user to the homepage, there are also Profile buttons and a button to take a user to their Shopping Cart or "wheelbarrow". The wheelbarrows icon signal if there are items currently sitting in the bag.
  - The search bar allows users to search for a keyterm throughout the site, this is useful if the user has a particular product in mind to purchase.
  - Buttons will be available to the user depending on whether they are logged into their account or not.
  - The mobile navbar condenses all the same elements into a burger menu, this retains screensaver for other elements e.g., products.
  ![Nav Bar](documentation/testing/navbar.png)
  ![Mobile Nav Bar](documentation/testing/mobile-navbar.png)
  
  __Footer__
  - The footer contains the address of the company, useful links, business information and links to social media accounts. All of which either open modals or open new tabs directed away from the website.
  - The footer design matches that of the header to give a cohesive feel to the website.
  ![Footer](documentation/testing/footer.png)
  
  __Homepage__
  - The homepage consists of a eye-catching photo to instantly suggest the purpose of the website to the user.
  - There is a section dedicated to advertising company special offers, currently on display is the Halloween offer where free delivery is granted to orders over £666.
  - On the homepage there are also buttons to direct the user to the main shop i.e., to view the plant products and .....
  ![Homepage](documentation/testing/homepage.png)
  
  __Shop Floor__
  - The shop floor displays the plants that the user is able to buy through the website.
  - Each plant has its own card, the user can see to which category the plant belongs e.g., if the plant is an air purifier or a succulent. The user can also see at a glance the care difficulty of the plant - this informs clients of the attention and care a plant needs and can therefore decide if a plant is suitable for its intended purpose.
  - Each plant product displays a price per item as well as a field to select a quantity of the product (max quantity selection is 99 items of a single product).
  ![Shop Floor](documentation/testing/shop-floor.png)
  
  __Product Filtering__
  - Describe the feature and what it allows a user to do.
  - Does the feature have any defensive programming?
  ![Product filtering](documentation/testing/product-filtering.png)
  
  __Shopping Bag ("Wheelbarrow")__
  - The wheelbarrow is always accessible to users, even when empty. The wheelbarrow allows users to view what is currently in their bag for purchase. From here, a user can amend their order, continue shopping or proceed to checkout.
  ![Wheelbarrow](documentation/testing/wheelbarrow.png)
  
  __Checkout__
  - Once item(s) have been added to the wheelbarrow the user will then be able to checkout. Upon checkout there is a brief review of the users basket i.e., what they intend to purchase. The user will then be required to fill out their delivery information and then proceed to fill out their payment information. Once payment is completed the order is made.
  - Does the feature have any defensive programming?
  ![Checkout](documentation/testing/checkout.png)

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

- Update preloader to be more themed to the site.
 - This has not yet been done due to time constraints, so [Bootstrap's spinners](https://getbootstrap.com/docs/5.2/components/spinners/#about) have been used as an interim. 
 - In the future, I will work to replace the Bootstrap spinner with either this [potted-plant](https://icons8.com/icon/OKMC0MrrQY5I/potted-plant) or [plant in sunshine](https://icons8.com/icon/YW744aCDWOMe/plant) preloader.

- Add digital wallets for easier checkout.
  - This would make checkout simpler and faster for the user by paying with the click of a button rather than filling out their card details into the Stripe input.
  - However, Stripe's documentation warns that the integration of digital wallets are "currently only available in the U.S., and not yet available in the UK and euro area." Therefore, this would need to change or I would need to change online payment provider before this could be implemented.
  - Please see the [Stripe Docs](https://stripe.com/docs/issuing/cards/digital-wallets) explaining how digital wallets can be intergrated into Stripe in the US.

- Auto populate countries field with the value 'United Kingdom' as Deilen are currently unable to ship abroad.
  - This would be useful to prevent users having to needlessly scroll through the country input to select the UK - as this is currentlythe only shipping destination.
  - I intend to implement this feature by following this [documentation](https://pypi.org/project/django-countries/#show-certain-countries-first) and discourse on [this stackoverflow thread](https://stackoverflow.com/questions/44025372/setting-a-default-value-in-choicfield-in-django).

- Checkout Webhooks
  - Adds redundancy to the order payment incase the browser is closed after the payment is confirmaed but before the order form has been submitted. This would stop the chance of payment going through without the order having been created.
  - I would follow the [Stripe documentation](https://stripe.com/docs/webhooks) on webhooks and follow Code Institute's walkthrough project in order to implement webhooks in my site.

***

## Technologies

- [GitPod](https://gitpod.io) was used as a cloud based iDE
- [GitHub](https://github.com/) was used to manage the Git repository
- [Heroku](https://deilen-shop.herokuapp.com/) was used for deployment
- [Git](https://git-scm.com/) was used for version control
- [Django](https://www.djangoproject.com/) used as the project's web framework
- [Pip3](https://pip.pypa.io/en/stable/) was the package manager used to install the dependencies
- [Bootstrap](https://getbootstrap.com/) was used for website layout and responsive components
- [AWS S3 Buckets](https://aws.amazon.com/products/storage/?hp=tile&tile=solutions) was used to provide storage of static and media files for the deployed site.
- [Gmail](https://mail.google.com/mail) was used for an STMP server to send company emails
- [PostgreSQL](https://www.postgresql.org/) was used as the projects database management system 
- [Google Fonts](https://fonts.google.com/) was used to provide website fonts and icons
- [Am I Responsive](http://ami.responsivedesign.is/) was used to generate a mock-up image
- [Dev Tools](https://en.wikipedia.org/wiki/Web_development_tools) was used for testing and responsiveness
- [Wireframe.cc](https://wireframe.cc/pro/) was used for creating wireframes
- [DrawSQL](https://drawsql.app/) was used for creating the database schema
- [W3C HTML Validator](https://validator.w3.org/#validate_by_input+with_options) and [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) were used to check HTML and CSS files for errors
- [pep8ish](https://pep8ish.herokuapp.com/) is Code Institute's Python Linter and was used to check Python files for errors

### Languages
- [HTML](https://en.wikipedia.org/wiki/HTML) was used as the markup language
- [CSS](https://en.wikipedia.org/wiki/CSS) was used for custom styling
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for custom website interactivity
- [Python](https://www.python.org/downloads/) was used for the backend functionality of the site

***

## Testing

To view all testing documentation, refer to [TESTING.md](TESTING.md).

***

## Deployment

The site was deployed to Heroku. The live link can be found [here](https://deilen-shop.herokuapp.com/)

The steps to deploy a Heroku app are as follows: 
1.  Log in to Heroku or create an account if required.
2.  Create a Heroku app - select 'New', from the drop-down menu select Create New App. The app name provided must be unique.
3.  Select a region.
4.  Create.
5.  Navigate to the Resources tab and add a Heroku PostgreSQL database.
6.  Access the Settings Tab and find the Config Vars. For this project you will need the following config vars:
    *   DATABASE_URL = the url of your heroku postgres database.
    *   SECRET_KEY = a secret key for your app.
    *   PORT = 5000
    *   DEBUG = set to 'True' during development and 'False' upon deployment.
    *   IP = Your IP address.
    *   USE_AWS = set to 'True'.
    *   AWS_ACCESS_KEY_ID = amazon web services publishable API key.
    *   AWS_SECRET_ACCESS_KEY = amazon web services secret API key, must be stored securly.
    *   STRIPE_PUBLIC_KEY = stripes publishable API key.
    *   STRIPE_SECRET_KEY = stripes secret API key, must be stored securly.
    *   EMAIL_HOST_PASS = 16 character password given once SMTP server setup in mail account settings.
    *   EMAIL_HOST_USER = the active email address that site emails will be sent from.

  Please see this [official documentation](https://devcenter.heroku.com/articles/config-vars) on Heroku configuration for more details.

7.  Navigate to the Deploy tab.
8.  Select Github as the deployment method.
9.  Follow steps to link to the appropriate GitHub account.
12. If you wish, enable Automatic Deploys for automatic deployment when you push updates to Github. Or alternatively, select the correct branch for deployment from the drop-down menu and click Deploy Branch for manual deployment.

Final steps: 
1. Create a Procfile in your repository containing `web: gunicorn deilen.wsgi:application` so that Heroku will identify that Gunicorn is acting as the webserver and run using the projects wsgi module.
2. Create an untracked file called env.py in your repo and input the config vars you previously established in Heroku.
3. Create a requirements.txt file
    - If you want to freeze your own packages into this file, run `pip3 freeze --local > requirements.txt` in the console.
    - To install only the packages that are already listed in the Deilen repo requirements (if making a local copy/clone) run `pip3 install -r requirements.txt` in the console.


### Setting up Stripe
For instruction to set upstripe payments, please visit [the Stripe documentation](https://stripe.com/docs/payments/accept-a-payment#web-collect-card-details).
Provided below is a brief explanation of Stripe setup:

1. Create a **stripe account** at [stripe.com](https://stripe.com/en-gb)
2. In the terminal, install Stripe:
```
pip3 install stripe
```
3. In the project settings file, ensure `STRIPE_CURRENCY` is set to 'gbp' and `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY` are retirived from the environment, with a default empty value, e.g.:
```
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', '')
```
4. These API keys are avliable to you from the **home** page of your Stripe account, under a section titled **"for developers"**. Copy the **Publishable key** and assign it to a new Heroku config var called `STRIPE_PUBLIC_KEY`. Then do the same for the **Secret key**, assigning it to a config var called `STRIPE_SECRET_KEY`.


### Setting up AWS
The deployed site uses AWS S3 Buckets to store the webpages static and media files. More information on how you can set up an AWS S3 Bucket can be found below:

1. Create an AWS account [here](https://portal.aws.amazon.com/billing/signup#/start/email).
2. Login and locate **S3 buckets** and create a new bucket.
3. Underneath **Object Ownership** select **ACLs enabled**.
4. Uncheck **Block Public Access** to make the bucket public, then finally **Create Bucket**.
5. Inside your new bucket navigate to the **Properties** tab. Within **Static Website Hosting** click **Edit** and edit the Static website hosting to **Enabled**. Copy the default values for the index and error documents and click **Save Changes**.
6. Navigate to the **Permissions** tab, within **Cross-origin Resource Sharing (CORS)**, click **Edit** and then paste in the following:

  ```
    [
        {
            "AllowedHeaders": [
            "Authorization"
            ],
            "AllowedMethods": [
            "GET"
            ],
            "AllowedOrigins": [
            "*"
            ],
            "ExposeHeaders": []
        }
    ]
  ```

7. In the **Bucket Policy** section click **Edit** and then **Policy Generator**. Open the **Select Type of Policy** dropdown, select **S3 Bucket Policy** and within **Principle** allow all principals by typing *.
8. Open up **Actions** dropdown menu, now select **Get Object** and in the previous tab copy the **Bucket ARN number**. Paste this in the policy generator in the **Amazon Resource Name (ARN)** field.
9. **Add statement > Generate Policy** and copy the generated policy, paste this into the **Bucket Policy Editor**.
10. Before saving, add /* at the end of your **Resource Key**, this will allow access to all resources within the bucket. Save.
11. Find **Access Control List (ACL)** and **Edit**.
12. Next to **Everyone (public access)**, check the **list** checkbox and save your changes.

#### IAM

1. Within IAM, in the sidebar select **User Groups** and then **Create group**, name the group.
2. In **Policies**, **Create policy**.
3. Navigate to the JSON tab and select **Import Managed Policy**, search for **S3** and select **AmazonS3FullAccess** followed by **Import**.
4. Navigate back to your S3 bucket and copy the **ARN Number**. Return to **This Policy** and update the **Resource Key** including your ARN Number . Copy this line to include all files by adding /* at the end. This code section should look like the following:
```
"Resource": [
    "YOUR-ARN-NUMBER-HERE",
    "YOUR-ARN-NUMBER-HERE/*"
]
```

5. Ensure the policy is named and has a description, then **Create Policy**.
6. Within the group created earlier, under permissions click **Add Permission** and select **Attach Policies**.
7. In the sidebar find **Users** and **Add User**.
8. Provide a username and check **Programmatic Access**, then click 'Next'.
9. Ensure the new policy is selected and navigate through until you click **Add User**.
10. VERY IMPORTANT: Download the **CSV file**, this contains the user's AWS access key and AWS secret access key.


#### Connecting AWS to Django

1. In the terminal:

```
  pip3 install boto3
  pip3 install django-storages 
```  

2. Add **storages** to your installed apps within your settings.py file.
3. In settings.py file add:

```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'your-bucket-name-here'
    AWS_S3_REGION_NAME = 'your-region-here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
```
4. Add  `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to Heroku config vars. These can be found in the CSV file downloaded when setting up AWS.
5. Add `USE_AWS` to Heroku config vars with value set to 'True'.
6. Remove the `DISABLE_COLLECTSTAIC` variable.
7. Within your settings.py add: 

```
  AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```
8. Within the bucket config in settings.py, add:

```
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
```

9. In the root directory of your project create **custom_storages.py**. Include the following:

```
  from django.conf import settings
  from storages.backends.s3boto3 import S3Boto3Storage

  class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

  class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

10. Navigate back to you AWS S3 Bucket and **Create Folder** called **media**, you can then **Upload > Add Files** all media files needed for the site.
11. Under **Permissions** select the option **Grant public-read access** and click **Upload**.

### Gmail STMP Server Setup
The following steps are for Gmail and may differ to other providers.

1. Navigate to **settings**, access the **Accounts and Import** tab and scroll to **other Google account settings**.
2. In the **security** tab and turn on **2-Step Verification**. Once completed access **App passwords**, select **Mail** for the app dropdown and select **Other** for the device type dropdown and type in "Django".
3. A 16 character password will be generated, copy this and enter as a Heroku config variable named `EMAIL_HOST_PASS` alongside your email address for `EMAIL_HOST_USER` variable.
4. In your project's settings.py file add the folloeing:
```
if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'deilen.example@gmail.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
```

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

- The Returns Policy was generated with [Termly's Return and Refund Policy Generator](https://termly.io/products/refund-return-policy-generator/).
- The Shipping and Delivery Policy was generated with [Termly's Shipping Policy Generator](https://termly.io/products/shipping-policy-generator/) and adapted.
- Frequently asked questions and answers content was sampled from the houseplant shop [Bloombox Club](https://bloomboxclub.com/).

### Media

- Icons were taken from both [Google Font Icons](https://fonts.google.com/icons) and [FontAwesome](https://fontawesome.com/).
- The favicon was generated with [favicon.io](https://favicon.io/) using Twitter emojis.
- The all site images were taken from the open source site [Unsplash](https://unsplash.com/).
- The product images were taken from [Kaggle](https://www.kaggle.com/), a website for dataset downloads. Specifically, images were taken from the [Healthy and Wilted Houseplant Images](https://www.kaggle.com/datasets/russellchan/healthy-and-wilted-houseplant-images) dataset. Only healthy houseplant images were used as product images.

### Acknowledgements

- My Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN)
- My friends and family for manually testing the site.

***