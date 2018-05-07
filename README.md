# Pony server

This code implements a backend server which serves a filtered, paginated
collection of ponies.

## Install the dependencies

You will need to install Python 3 then run:

    virtualenv -p python3 env
    source env/bin/activate
    pip install -r requirements.txt

## Run the server

Load fixtures and run the server:

    ./manage loaddata ponies
    ./manage runserver

To check that everything is working as expect, point your browser to:

    http://localhost:8000/v1/ponies

## Learn more

You can learn more by reading this blog post:

    https://medium.com/@JeremyLaine/server-side-pagination-and-filtering-with-angular-6-280a7909e783
