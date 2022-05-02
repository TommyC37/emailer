# Emailer Read Me

## Purpose

The purpose of *Emailer* is to offer a simple way to automate email sends via gmail. It enables users to:

1. Create an account.
2. Create sets of "series" (i.e. automated email steps)
3. Initiate a series for specific recipients

## How it works: Series creation

A series is created with a GUI interface. The user can:

1. Add email steps
2. Add email subject lines
3. Add email body copy
4. For the series as a whole, you can specify whether the send dates/times should be relative or absolute

When a series is created it is stored in a table in a mySQL database.

## How it works: Series Initation

When a series is initiated, the user can specify:

1. Who to send to (name + email)
2. Any specific changes to each step in the series
3. When to start the initial email

Once initated, each email step is added as an entry into a "pending emails" table in the database. Each entry includes:

1. Email to name
2. Email to address
3. Email copy
4. Subject line
5. Send date
6. Send time

## How it works: Email Sends

A cronjob is set up on the server to check once every hour (on the hour) if any emails are set to go out during that hour.

For each email, a Python script is fired to send the email with a wait time equal to `current_time - send_time`.
