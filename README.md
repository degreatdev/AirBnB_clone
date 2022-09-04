#               AirBnB clone - The console

## Over view
In this project we are building a clone of AirBnB website which wil contain

    1. A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
    2. A website (the front-end) that shows the final product to everybody: static and dynamic
    3. A database or files that store data (data = objects)
    4. An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

##### For the first part of the project we will focus on the COMMAND interpreter(console)
## The console
    1. create your data model
    2. manage (create, update, destroy, etc) objects via a console / command interpreter
    3. store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI we will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
The console will be a tool to validate this storage engine

## How to Start the console

1. Interactive mode:
    $ ./console.py
##### example
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

```
2. Non-interactive mode
    $ echo "help" | ./console.py
##### example
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```