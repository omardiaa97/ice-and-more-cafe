## HarvardX CS50W: Web Programming with Python and JavaScript

### Course's link
See [here](https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript).


### Requirements
The final project is my opportunity to design and implement a dynamic website of my own. So long as my final project draws upon this course’s lessons

In this project, I'm asked to build a web application of my own. The nature of the application is up to me, subject to a few requirements:

  - My web application must utilize at least two of Python, JavaScript, and SQL.
  - My web application must be mobile-responsive.
  - In README.md, include a short writeup describing your project, what’s contained in each file I created or modified, and (optionally) any other additional information the staff should know about your project.
  - If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to requirements.txt!

Beyond these requirements, the design, look, and feel of the website are up to me!

### Capstone project

My final project is a freelance restaurant cafe website that well designed and has an admin panel that enable the admin (Restaurant owner) to add, change or delete his menu items (Prices, descriptions and names)

The project was built using Django as a backend framework and JavaScript as a frontend programming language. All generated information are saved in database (SQLite).

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
