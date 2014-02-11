Prerequisites:  
python 2.7  
[pip](http://www.pip-installer.org/en/latest/installing.html)  
sqlite  

To set up:  
`pip install -r requirements.txt`  
`python manage.py syncdb`  

To test:  
`python manage.py runserver`  

The problem
===========

Add the following views:
- A view to browse books in a series, artist, or writer
- A view to allow an authenticated user to curate their own collection (i.e. indicate which books they own)

Extra Credit
------------
Create a restful api to access books by series, writer, or artist

#### Delivery instructions
Do *not* fork this repository (for the sake of anyonymity).  Instead, clone this repo, check in your solution, zip up the files, and email the zip back to us.
