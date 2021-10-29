# Flask Jsonapi Football Backend

## Installation

Tested on Python 3.7.

As usual, create a virtual environment and install the requirements with pip.

    pip install -r requirements.txt

Run docker-compose to create db for use.

    docker-compose -f docker-compose.dependencies.yaml up

## Running

    flask db upgrade

After that, you can run the application with the following command:

    python manage.py

