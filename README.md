# Product-availability-automated-script
Script that checks if a certain product is available in a web page
I made a program for a friend, that checks every 15 minutes (with windows task scheduler) if a certain graphics card is available to buy.
It extracts the text of the purchase button, if it says that its available, it will send an email to him.
This was done using libraries like beautifulsoup, requests and smtplib.
