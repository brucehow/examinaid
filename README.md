# ExaminAid &middot; [![Flask 1.1.2](https://img.shields.io/badge/flask-1.0.2-blue.svg)](https://pypi.org/project/Flask/) [![Python 3.7.2](https://img.shields.io/badge/python-3.7.2-blue.svg)](https://www.python.org/downloads/release/python-372/) 

## Overview

**ExaminAid** is a UWA Computer Science assessment preparation application containing various resources in the form of test questions and answers. The application is accessible to anyone who creates an account on the server where ExaminAid is running and contains all the question sets available to users. ExaminAid is completely free and has an intuitive and simple-to-use user interface for everyone, both students and teachers. The creators of ExaminAid welcome any feedback via the contact form on the ExaminAid website.

## Design and Development

Every question set supported by our application has a different combination of question types; the 3 main question types supported by our application include **multiple choice**, **short answer**, and **open answer** questions. Each question set is represented by a JSON file which contains information about the unit, including the unit code, and unit name, as well as the total number of marks, alongside the actual questions themselves. For the question sets that are supported by default, **immediate feedback** is available for most multiple choice and short answer questions, and the option for **custom feedback** is available on open answer questions. More information about this is provided below.

There are 2 types of accounts users can have. By default, upon signing up to our application, users are granted a **student** account, which can view question sets, take tests and view the results of past tests. However, **administrators** are not only able to view question sets, but are also able to mark open answer questions, as well as manage, add and delete users. User accounts are switched between administrator and student permission levels via the command line; no account is able to make this change in the main application interface for security reasons. The **USEFUL.md** document outlines the commands available to developers wishing to explore this functionality. Similarly, any pages that require administrator-level access will redirect when a user who is **not** an administrator attempts to access the page; this includes student accounts and logged-out users.

ExaminAid does **not** store passwords in plain text. Rather, the backend database stores salted and hashed strings that represent these passwords. When a user log into our application, the password they enter is checked against this string. Users are able to change their passwords while logged in, by first confirming their email, then their current password, and then entering their new, desired password.

## Application Structure
The application structure and explanation are as below:
```
examinate
├── README.md                           
├── USEFUL.md
├── app
│   ├── __init__.py
│   ├── feedback                        <-- dir containing completed tests
│   ├── forms.py                        <-- structure for WTForms
│   ├── models.py                       <-- authentication and user control
│   ├── questions                       <-- dir containing question sets
│   │   ├── <question_file>.json
│   │   └── units.json                  <-- question set overview
│   ├── routes.py                       <-- page and authentication routes
│   ├── static 
│   │   ├── css                         <-- dir containing css files for each component
│   │   │   ├── *.css
│   │   ├── resources                   <-- dir containing image resources
│   │   │   ├── *.svg
│   │   │   ├── authors
│   │   │   │   ├── *.png
│   │   └── scripts                     <-- dir containing js scripts
│   │       ├── *.js
│   ├── templates                       <-- html page templates
│   │   ├── *.html
│   └── unitJSON.py                     <-- handles exam test files
├── app.db                              <-- light weight database file
├── backendtesting.py                   <-- backend unit test
├── requirements.txt                    <-- application required dependencies
├── selenium
│   └── frontendtesting.side            <-- selenium front-end testing
└── test.db                             <-- db used for unit testing
```

## Features

### General
- **Contact Form** - Allows users to submit feedback and questions about our site. This is a HTML form with interfaces with a script in Google Sheets to store form submissions in a separate online document. The sheet which receives this data is available [here](https://docs.google.com/spreadsheets/d/1tRqt7958lMhJuw4GvrrazpACogWdf6A6B2dD_zZ_HmE/edit?usp=sharing).
- **Reset / Change Password** - Requires a login. Users can change their password by confirming their email and previous password.

### Student Dashboard
- **Start Test** - Directs the user to `newtest.html` where the user can choose a test to complete. Our application currently supports 4 course tests, as well as a demonstration test.
- **Previous Attempts** - Allows the user to view their previous test attempts. Each entry contains the test unit code, automated marks, manual marks, the marking status and a link containing the test feedback

### Teacher Dashboard
**Admin user account required**
- **Mark Completed Tests** - Allows the user to view a list of tests that require marking. The user can view the student's test feedback which shows the test information, list of incorrect automatic questions and the students responses to the questions. Teachers can manually allocate a mark and update the student's feedback.
- **View Previous Tests** - Displays a list of completed tests by all students. Each test entry will show the unit code, student that completed the test, automatic marks, manual marks, total marks, completion date, the marking status and a link to the file feedback.
- **Manage Tests** - Allows a teacher to add tests of varying formats, or remove existing tests.
- **Manage Users** - Allows a teacher to add or remove user logins. Cannot change an account's status (between student / teacher) for security reasons; this can only be done at the command line.

### Styling
- Boostrap has been used throughout the application to structure the webpage.
- Styling components has been separated into different `.css` files which are located in the `app/static/css` dir
- FontAwesome has been used to provide unique icons that are easily accessible such as the GitHub and BackNavigation buttons

## Libraries Used
- [Bootstrap](https://getbootstrap.com/)
- [jQuery](https://jquery.com/)
- [Font Awesome](https://fontawesome.com/)

## Authors
- [Bruce How](https://github.com/brucehow)
- [Lachlan D Whang](https://github.com/ForsakenIdol)
- [Paul O'Sullivan](https://www.github.com/paulosllvn)
- [Bryan Yeo](https://github.com/Darkstorm1337)
