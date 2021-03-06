# email_validation_with_db

## Objectives:

- Practice reading from and inserting into a database
- Validate user input before adding it to the database
- Practice using regex
- Practice using flash messages
- Practice redirecting after going to a POST route
- Consider front-end versus back-end validations

Create an application that asks a user to enter an email address and validates it.

### index.html
A simple form for the user to submit an email.

<img width="299" alt="Screen Shot 2022-01-04 at 6 47 15 PM" src="https://user-images.githubusercontent.com/92617960/148147688-4f567123-1a8d-46a7-b7a3-b86e5b534a6c.png">

### Error
If the email address is not valid, have a notification "Email is not valid!" to display on the homepage.

<img width="298" alt="Screen Shot 2022-01-04 at 6 47 34 PM" src="https://user-images.githubusercontent.com/92617960/148147711-6b4724d4-5a8a-4600-bcf3-557eb0827388.png">

### success.html
Once a valid email address is entered, save to the database the email address the user entered. On the success page, display all the email addresses entered along with the date and the time when the email addresses were entered.

<img width="297" alt="Screen Shot 2022-01-04 at 6 47 50 PM" src="https://user-images.githubusercontent.com/92617960/148147734-7044c054-2b7b-40cf-bb41-265b5b81fefd.png">

- [ ] Create a new Flask project

- [ ] Create a new database with a table containing an email address field

- [ ] Set up the root route to display a form to input an email address

- [ ] Validate that the email is in the correct format

- [ ] If invalid, redirect to the root route with an error message

- [ ] If valid, redirect to the success route that displays a success message

- [ ] Have the success route template also display a list of all the email's in the database

- [ ] NINJA Bonus: Also validate that the email being added is unique

- [ ] NINJA Bonus: Add a delete button on the success route allowing for the deletion of a specific email from the database
