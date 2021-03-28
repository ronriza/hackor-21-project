# hackor-21-project

The COVID Vaccine Availability Notification Tool notifies the user via email if COVID vaccines are available at a nearby site, within New York state.

You must set env variables in order to send email notifications and/or twilio sms notifications (email password, twilio SID & AUTH token).
To try out this tool using its default behavior, update sample.csv with data in the following format with no header:
    age, zip (within NY), desired radius to search, email, phone number
