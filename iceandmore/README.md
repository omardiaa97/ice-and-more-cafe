## HarvardX CS50W: Web Programming with Python and JavaScript

### Course's link
See [here](https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript).


### Requirements
The final project is my opportunity to design and implement a dynamic website of my own. So long as my final project draws upon this course’s lessons

In this project, I'm asked to build a web application of my own. The nature of the application is up to me, subject to a few requirements:

  - My web application utilize python, JavaScript, and SQL.
  - My web application is mobile-responsive.
  - README File, includes a short writeup describing your project, what’s contained in each file I created or modified, and (optionally) any other additional information the staff should know about your project.
  - Python Packages used in the project are added to the requirements.txt!

### Capstone project

My final project is a restaurant cafe website that well designed, has:
1-single HTML Page that contains 4 sections that u can switch between them via the navigation bar with an animation:
  I-Intro section contains (Image of a restaurant, its name and some words) 
  II-Menu section (That displays all the items and categories added by the owner from the admin panel)
  III-About us Section (Contains some images from facebook, instagram , some usefull links to social media pages) 
  IV-Contact Us Section (Contains the real location of the restaurant and feedback form (doesn't work right now, but it doesn't give any error)

2- Admin panel that enable the admin (Restaurant owner) to add, change or delete his menu items (Prices, descriptions and names) and the categories with a friendly user iterface (Embedded Admin Panel from Django)

This project uses javascript, has an admin panel and mobile responsive in addition to it's a real freelance project that will be delivered to a real customer to use it for his business

The project was built using Django as a backend framework and JavaScript, bootstrap and jQuery in the frontend. All generated information are saved in  SQLite database.

All webpages of the project are mobile-responsive.

#### Installation
  - Install project dependencies by running `pip install -r requirements.txt`. Dependencies include Django and Pillow module that allows Django to work with images.
  - Make and apply migrations by running `python manage.py makemigrations` and `python manage.py migrate`.
  - Create superuser (admin account) with `python manage.py createsuperuser`. to be able to manipulate your data.
  - Run project `python manage.py runserver`
  - Go to website address and register an account.


#### Files and directories
  - `website` - main application directory.
    - `static` contains all static content.
        - `assets` contains all media files and photos used in the project.
        - `script` - all JavaScript files used in project.
            - `app.js` - this script run in `index.html` because it is included in base template. it has some
                          jquery code that works with the aid of bootstrap to make some animations and actions
        - `css` - contains all source CSS files.
    - `templates/website` contains index.html
    - `admin.py` - It contains registered admin classes and models to be used in admin panel.
    - `models.py` contains two models I used in the project. `Item` model extends the `Category` model
    - `urls.py` - all application URLs.
    - `apps.py` - Contains some project configurations
    - `views.py` respectively, contains all application views.
  - `iceandmore` - project directory.


The project's video: https://youtu.be/hW52tx2LrmA
