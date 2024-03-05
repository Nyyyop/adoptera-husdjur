# Adoptera Husdjur

Adoptera Husdjur is a web application developed as part of the "Webbserverprogrammering 1" course, curriculum year 23/24, at NTI Gymnasiet. The application provides a platform for users to browse and adopt pets.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [License](#license)

## Overview

Adoptera Husdjur is built with the Flask framework and Python. It utilizes various Python concepts such as instances, classes, modules, and `__name__`. For routing, Flask's `route`, `request`, `response`, and `endpoints` are used.

The application serves as a platform for pet adoption. Users can browse through a list of pets available for adoption, view detailed profiles of each pet, and express their interest in adopting a pet by submitting a form.

## Installation

To get started with Adoptera Husdjur, follow these steps:

1. Clone the repository: `git clone https://github.com/Nyyyop/adoptera-husdjur.git`
2. Navigate to the project directory: `cd adoptera-husdjur`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment:
    - For Windows: `venv\Scripts\activate`
    - For macOS/Linux: `source venv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Set the Flask app environment variable:
    - For Windows: `set FLASK_APP=app.py`
    - For macOS/Linux: `export FLASK_APP=app.py`
7. Run the application: `flask run`

The application should now be running locally on your machine. You can access it by opening a web browser and navigating to `http://localhost:5000`.



## Features

Adoptera Husdjur offers the following features:

- Browse through a list of available pets for adoption
- View detailed profiles of each pet, including their name, age, breed, and description
- Express interest in adopting a pet by submitting a form
- Search for pets based on specific criteria, such as species or breed
- Sort the list of pets by various attributes, such as age or name
- Receive notifications or updates about new pets added to the platform
- Connect with other users who have adopted pets through the platform's community forum

## Usage

Once the application is up and running, you can access it at http://localhost:5000. Here are some features and functionalities you can expect:

- Browse available pets, such as cats, dogs, and rabbits at the route `/pets`
- View detailed profiles of each pet at the route `/pets/<pet_id>`
- Express your interest in adopting a pet by submitting a form at the route `/adopt/<pet_id>`

## License

This project is licensed under the [MIT License](LICENSE).