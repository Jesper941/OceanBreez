## CONTENTS

- [CONTENTS](#contents)
- [AUTOMATED TESTING](#automated-testing)
  - [W3C Validator](#w3c-validator)
- [Lighthouse](#lighthouse)
  - [LAPTOP RESULTS](#laptop-results)
  - [MOBILE RESULTS](#mobile-results)
  - [Full Testing](#full-testing)
- [Bugs](#bugs)
  - [Known Bugs](#known-bugs)
  - [Solved Bugs](#solved-bugs)

Testing was ongoing throughout the entire project. I used the Chrome developer tools while coding the website to pinpoint and troubleshoot any issues.

I have gone through each step of the quiz using Google Chrome developer tools to ensure that each page is responsive on a variety of different screen sizes and devices.

- - -

## AUTOMATED TESTING

I have written 3 simple tests for my project. More information about them can be found in the [tests.py](tests.py)

## MANUAL TESTING

### W3C Validator

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the website. It was also used to validate the CSS.

* [HTML] ( Pass - Checked the templates in the bookings templates as well as the templates in the "django_todo" folder )
  
* [CSS Styling] ( Pass - Checked the CSS styling for the website using  https://jigsaw.w3.org/css-validator/ )
  
* [Javascript] ( Pass - Checked the Javascript code using https://jshint.com/


## Lighthouse

My Lighthouse score was really good for accessibility both on desktop and mobile.

### LAPTOP RESULTS

HOME PAGE

![desktop](assets/images/desktop-lighthouse.png)

MENU PAGE

![desktop]

CONTACT PAGE

![desktop]

BOOKING PAGE

![desktop]


### MOBILE RESULTS

HOME PAGE

![mobile]

MENU PAGE

![mobile]

CONTACT PAGE

![mobile]

BOOKING PAGE

![mobile]

- - -

### Full Testing

Full testing was performed on the following devices, and additional testing for other devices was carried out using developer tools:

Laptop, Mobile M, Mobile L, and Tablet.

Each device tested the site using the following browsers:

Google Chrome on Windows.

`Index Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| **NAVBAR** | 
| Ocean Breeze text in top left corner | To take the user to the index page | Click the Ocean Breeze text | Directs you to the index page | Pass |
| "Home" button in the navbar | Take the user to the index page | Click the "Home" text in the navbar | Directs you to the index page | Pass |
| "Menu" text in navbar | To take the user to the menu page | Click the "Menu" text in the navbar | Directs you to the menu page | Pass |
| "Booking" text in navbar | To take the user to the booking page where they can login or register a new account | Click the "Booking" text in the navbar | Directs you to the Booking page | Pass |
| "Contact" text in the navbar | To take the user to the contact page | Click the "Contact" page in the navbar | Directs you to the contact page | Pass |
|  |  |  |  |  |

| `Booking Page` |
| Login link | To take the user to the login page | Click on the "Login" link | Directs you to the login page | Pass |
| Register link | To take the user to the registration page to create their new account | Click on the "Register" link | Directs you to the registration page | Pass |

| `Login Page` |
| Enter a blank or non-registered username or password | Get alerted to enter valid username or password | Enter a username with blank spaces or invalid information | Alerted to enter valid username or password | Pass |
| Enter a registered username and password | For the the user to be directed to the booking form | Enter correct login information | Directs you to the booking form | Pass |

| `Registration Page` |
| Enter valid information to create a new account | To create a new account and redirect user to the "Creation succesful" page | Fill out the registration form correctly | Directs you to the Creation successful page and successfully creates a new user in the database | Pass |

| `Registration Success Page`|
| "Take Me Home" button | To take the user to the index page | Click the button | Directs the user to the index page | Pass |

| `Booking Success Page`|
| "Take Me Home" button | To take the user to the index page | Click the button | Directs the user to the index page | Pass |

| `Book A Table Page`|
| Change Existing Booking button | To take the user to the "Change Booking" page | Click the "Change Existing Booking" button | Directs user to the "Change Booking" page | Pass |
| Enter valid booking information | To successfully book a table and direct user to "Booking Success" page | Fill in the form with valid information and pick a future time and date | Allows user to continue when clicking the "Submit" button | Pass |
| Submit booking button | To confirm the booking in the database and take the user to the "Booking Success" page | Click the button | Directs user to " Booking Success" page and creates a booking in the database | Pass
| Enter a time that doesn't exist | Get alerted to chose a valid time for the booking | Fill in the form with an invalid time | User gets alerted to pick a valid time | Pass |
Enter a date that has already passed | Get alerted to pick a valid date | Enter an invalid date | User gets alerted to pick a valid time | Pass |

| `Change Existing Booking Page` |
| Enter new valid booking information | To successfully change the booking information and direct user to "Booking Success" page | Fill in the form with new valid information and pick a new future time and date | Allows user to continue when clicking the "Submit" button | Pass |
| Submit booking button | To confirm the change of the booking in the database and take the user to the "Booking Success" page | Click the button | Directs user to " Booking Success" page and successfully changes the booking in the database | Pass
| Enter a time that doesn't exist | Get alerted to chose a valid time for the booking | Fill in the form with an invalid time | User gets alerted to pick a valid time | Pass |
Enter a date that has already passed | Get alerted to pick a valid date | Enter an invalid date | User gets alerted to pick a valid time | Pass |
| Cancel Booking Button | To take the user to the "Cancel Booking" page" | Click the Cancel Booking button | Directs user to the "Cancel Booking" page | Pass |

| `Cancel Booking Page` |
| "Select booking" drop down menu | To show user a list of their booking/s | Click the drop down menu | Shows the user a list of their existing booking/s | Pass |
| Any booking in the users list of bookings | To select one of the bookings to cancel | Click on one of the existing bookings | Selects the booking the user clicked on and let's them continue canceling the booking | Pass |
| "Cancel Booking" button | To delete the selected booking from the database and redirect the user to the "Cancelation Successful" page | Click the "Cancel Booking" button | Deletes the selected booking from the database and redirects user to the "Cancelation Successful" page | Pass |


## Bugs

### Known Bugs

| Known Bug No | Bug Issue | Plan to Resolve |
| :--- | :--- | :--- |
| 1 |  | :--- |

### Solved Bugs

| Bug No | Bug Issue | How Resolved |
| :--- | :--- | :--- |
| 1 |  | :--- |