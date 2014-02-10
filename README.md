Prerequisites:
python 2.7
pip
sqlite

To set up:  
`pip install -r requirements.txt`  
`python manage.py syncdb`  

To test:  
`python manage.py runserver`  

The problem
===========

Add the following views:
- A view to browse books in a series
- A view to browse books by artist
- A view to browse books by writer
- A view to allow an authenticated user to curate their own collection (i.e. indicate which books they own)

Extra Credit
------------
Create a restful api to access books by series, writer, or artist
