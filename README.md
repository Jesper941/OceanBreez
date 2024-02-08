# The Ocean Breeze

"Welcome to the Ocean Breeze! A cozy restaurant located by the shore with amazing, fresh food with freshly caught fish and seafood."

![responsiveness](assets/images/responsive-quiz.png)

LIVE WEBSITE

You can view a live version of the website here.(<https://young-anchorage-44026-d8f70dc45a2a.herokuapp.com/>)

GITHUB PAGES

You can view the GitHub code pages here. (<https://github.com/Jesper941/OceanBreez>)

## CONTENTS

- [The Ocean Breeze](#the-ocean-breeze)
  - [CONTENTS](#contents)
      - [Visitors Goals](#visitors-goals)
      - [First-Time Visitor Goals](#first-time-visitor-goals)
      - [Returning Visitor Goals](#returning-visitor-goals)
      - [Frequent Visitor Goals](#frequent-visitor-goals)
  - [Strategy](#strategy)
    - [Sets Of Goals](#sets-of-goals)
      - [Set Of Goals 1 - Initial Setup](#set-of-goals-1---initial-setup)
      - [Set Of Goals 2 - Templates](#set-of-goals-2---templates)
      - [Set Of Goals 3 - Booking System](#set-of-goals-3---booking-system)
      - [Set Of Goals 4 - CRUD Aspect Of The Booking System](#set-of-goals-4---crud-aspect-of-the-booking-system)
  - [Scope](#scope)
  - [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Function Styling](#function-styling)
  - [Features](#features)
  - [How to Play](#how-to-play)
    - [Navigation](#navigation)
    - [Future Implementations](#future-implementations)
    - [Accessibility](#accessibility)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Local Development](#local-development)
      - [How to Fork](#how-to-fork)
      - [How to Clone](#how-to-clone)
  - [Testing](#testing)
  - [Credits](#credits)
    - [Code Used](#code-used)
    - [Content](#content)
    - [Media](#media)
    - [Feedback](#feedback)

---

#### Visitors Goals

The main goal for any visitor would be to test their knowledge of the history of the National Hockey League and its players.
Another goal is to see who's the most knowledgeable among their friends or family members.
To spend some time having fun with an interactive and interesting quiz.
Divided into different categories, the visitor's goals may look like this:

#### First-Time Visitor Goals

- I want to see what kind of food the restaurant has to offer.
- I want to see where the restaurant is located.
- I want to know how to get in contact with the restaurant.
- I want to be able to book a table either via phone or through the website.
- I want to be able to register to the booking feature easily.
- I want the booking system to be smooth and easy to use.

#### Returning Visitor Goals

- I want to be able to change my booking.
- I want to be able to change the information in my current booking.
- I want to see if the restaurant have anything new on the menu since visiting last.

#### Frequent Visitor Goals

- I want to be able to have multiple bookings at the same time
- I want to be able to chose which booking i want to change if i have more than one.

---

## Strategy

### Sets Of Goals

This project was developed with 5 milestones (epics) in mind. From each of these milestones a number of dev goals and user stories were created, each one given a prioritisation using the MoSCoW method. The detail of these milestones, goals and stories is outlined below.

#### Set Of Goals 1 - Initial Setup

- Goal 1 -Install Flask, Django and any other library necessary to complete the project.
- Goal 2 - Make sure the "manage.py runserver" command works and that the website can go live
- Goal 3 - Create all the necessary folders such as "templates", "bookings" and "static"

#### Set Of Goals 2 - Templates

- Goal 1 - Set up a base, an index landing page, a menu page, a contact page and a booking page
- Goal 2 - Fill each page with the content i wanted it to have
- Goal 3 - Make sure the pages are estethically pleasing and responsive

#### Set Of Goals 3 - Booking System

- Goal 1 - Add the registration and login form to the booking page
- Goal 2 - Set up all the necessary steps for the admin site
- Goal 3 - Create the models needed to have both user registration and bookings possible and be uploaded to the database
- Goal 4 - Ensure that admins can create, edit or cancel any booking or delete any user if needed

#### Set Of Goals 4 - CRUD Aspect Of The Booking System

- Goal 1 - Allow the users to register to the website
- Goal 2 - Allow the user to book a table once they've registered
- Goal 3 - Allow the user to chose date, time, what name to book the table in and to add some contact information
- Goal 4 - Allow the user to make multiple bookings
- Goal 5 - Allow the user to select an existing booking and edit/add/remove information from the booking.
- Goal 6 - Allow the administrator to cancel, reschedule or edit all any booking
- Goal 7 - Allow the administrator to edit or delete registered users
- Goal 8 - Allow users to cancel their bookings

## Scope

So with all of these user stories and developing goals in mind, the list of things that i wanted and that were necessary ended up as such:

- A responsive website that's usable on any modern device
- An easily navigatable website that's user friendly and not too bulky with uneccessary content
- Main pages such as:
  - An index / homepage with information about the restaurant and it's history
  - A menu page where the users can inspect the food that's being served before deciding to book a table
  - A contact page where users can find the restaurant's location and contact information
  - A table booking page where users can register in order to book, view, edit, cancel or add information to their booking
- An admin site where the administrators can create, edit or remove bookings
- An admin site where the administrators can create, edit or delete registered users

## Design

### Colour Scheme

Here is the color palette for the colors that I've used to create this website.

![The Ocean Breeze color palette](bookings/static/img/ColorPaletteOceanBreeze.png)

### Typography

I use the 'Lora', 'Times New Roman' and 'serif' font style for the entire website.

### Function Styling

- Starting off with the home page where the visitor has to enter a valid username.
  A blank space for their username will not be valid and a message will be prompted as in the picture.

![username](assets/images/enter-valid-name.png)

- Once you've entered a valid username, the introduction area will disappear and the quiz will appear.

![quiz-appearing](assets/images/quiz-area.png)

- If you enter an incorrect answer, the answer you chose will turn red. Your point score will stay the same, and when you hit the "next question" button, the question number counter will increase.

![wrong](assets/images/wrong.png)

- If you answer a question correctly, the question you chose turns green. Your point score will increase by one and as soon as you click the "next question" button, the question number counter will increase.

![correct](assets/images/correct.png)

- If you end up with a score of 3 or lower, you get the following message.

  ![low-score](assets/images/low-score.png)

- If you end up with a score of 4 and 6, you get the following message.

  ![mid-score](assets/images/mid-score.png)

- If you end up with a score of 7 or higher, you get the following message.

  ![high-score](assets/images/high-score.png)

- If you press the "Replay" button by the end of the quiz, you get taken straight back to the first question of the next quiz.

  ![replay](assets/images/replay.png)

---

## Features

What does this quiz feature?

- 10 challenging NHL-related questions.
- Multiple-choice answers for each question.
- Interactive design with user-friendly buttons.
- Real-time scoring to track your progress.
- A final score page with personalized feedback.
- Replay the quiz to improve your score.

## How to Play

- Visit the NHL Quiz webpage.
- Enter your name in the provided field.
- Click the "Start Quiz" button.
- Answer each question by clicking on the multiple-choice options.
- Click the "Next Question" button to advance.
- After 10 questions, see your final score and feedback.
- Click "Replay" to play the quiz again and beat your previous score.

### Navigation

There is really only one page, but the NHL-shield logo in the top left corner will load the index.html and take you back to the beginning of the quiz where you enter your username.

![logo-link](assets/images/link-shield.png)

### Future Implementations

- Add a choice for the player on how many questions the quiz should be.
- Add images that show up when the correct answer has been chosen.
- Increase the library, or array, of questions for the quiz.

---

### Accessibility

In order to ensure that the website has good accessibility, I have used different semantic tags,
such as header, main, section, etc.

- I have used an "alt" attribute on the banner image.
- Using colors that mix well together and allow the visitor to easily read the answers, read the options, and find the buttons without struggle.

---

## Technologies Used

### Languages Used

I used HTML and CSS to build this website.

### Local Development

Instructions on how to fork and clone the project.

#### How to Fork

1. Log in (or sign up) to Github.
2. Go to the repository for this project, (https://github.com/Jesper941/nhlquiz.git)
3. Click the Fork button in the top right corner.

#### How to Clone

Log in (or sign up) to GitHub.

1. Go to the repository for this project, (https://github.com/Jesper941/nhlquiz.git)
2. Click on the code button, select whether you want to clone with HTTPS, SSH, or GitHub CLI, and copy the link shown.
3. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
4. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

## Testing

You can find all of the testing done in the [TESTING.md file](TESTING.md)

## Credits

Here i'm gonna list the credits to all the sources that helped me out during this project.

### Code Used

1. Some general tips and tricks from youtuber Brocode and his video: <https://youtu.be/HGTJBPNC-Gw?si=MoPalcBbt6jw2o88>
2. For the stroke text i went here for help: <https://css-tricks.com/adding-stroke-to-web-text/>
3. I took a lot of help from this website when i needed help with coding and styling the pseudo-elements for the links in the nav bar: <https://stackoverflow.com/questions/10143357/how-to-make-these-buttons-not-appear-as-blue-links>
4. For help with coding the responsive flexboxes for my text containers, i took help from the flexbox section of this website: <https://www.w3schools.com/css/css3_flexbox_responsive.asp>
5. To truly understand the meaning and difference between margin and padding, i took help from these sites. <https://www.w3schools.com/css/css_margin.asp> and <https://www.w3schools.com/css/css_padding.asp>
6. i couldn't figure out how to make the text-containers to not go across the full width of the page, so i use some of the code here to learn and use in my text containers: <https://www.w3schools.com/css/css_max-width.asp>
7. I found some help on how to solve blank space validation: https://stackoverflow.com/questions/1151032/javascript-blank-space-validation
8. How to properly use the firstChild property: https://developer.mozilla.org/en-US/docs/Web/API/Node/firstChild
9. How to use the innerText property to change the text of elements after a function or event happens: https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/innerText

### Content

I wrote the code myself but with some help from the sites and people mentioned above on how to execute my idea.

### Media

Background image in the header: <https://www.hockeymonkey.com/media/magefan_blog/Hockey_Trivia_Banner.jpg>

### Feedback

If you have any feedback or questions, please reach out to me via my email: Jesper941@hotmail.com

<https://www.scaler.com/topics/bootstrap-tutorial/bootstrap-datepicker/>
<https://docs.djangoproject.com/en/5.0/>
<https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django>
