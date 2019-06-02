# Known Issues and bugs

## Current known bugs

```
- Arrow for vehicle list malfunctions sometimes visually
- Update profile function in account settings page does not work
- Same account can be logged into at the same time on different devices
- When more than 7 numbers are entered in account settings to update user licences, it crashes the application
- Distance shows NaN when the page first initially loads due to unable to collect users location before display
- When clicking back from the browser it does not reset the car availability
- Simulation goes out of bounds
- Missing the price in the car list
- Invalid credential popup has a dot
- Confirmation and booking page cancel button off centred
```

## Issues and Risks

```
Django Paypal, there wasn’t enough documentation support django paypal to be implemented in our application on what we wanted. Customer ID details needed to be stored after the initial payment of $10 and then later on when the car is returned it gets the user details and pays the existing card. Suggested to use temporary database to store users details however, the database will be dropped when the database connection terminates. The user details could be stored for more than 24 hours which would be a security risk. So the alternative solution was, Stripe payment, returns a customer id for us to store and can access the users payment details through the id without breaching any security risks.  
```
```
PostgreSQL for testing, although heroku postgreSQL database being a scalable application and can run tests on the cloud while the application is in production. There was a slight issue when trying to deploy a test database for testing in django. In some cases the test database could overwrite the existing normal database. This would cause an issue in deleting all known cars and user details from the database. Solution to this issue was used SQLite for testing, When running the test script on heroku, it will create a temporary Local SQLite database for testing. Once all the tests has passed the database would be dropped and deleted leaving no trace of the database.  
```
```
Security risks is a huge problem in our current application, without the technical skills of someone in security we are unable to perform any safety measures in storing users payment details. Other application settings has database password and username written, this is a huge risk in the application, as databases could be completed dropped and altered.
```
