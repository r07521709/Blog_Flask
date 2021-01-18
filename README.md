
## Blog

A blog implemented based on Flask framework. It contains CRUD (Create, Read, Update, Delete) operations and allow users to register and login to post, modify or delete their posts.

- Front End: HTML & CSS, Bootstrap
- Back End: Python, Flask


## Database

To create the initial database, just import the db object from an interactive Python shell and run the SQLAlchemy.create_all() method to create the tables and database:
```
>>> from app.models imoprt db
>>> db.create_all()
```

