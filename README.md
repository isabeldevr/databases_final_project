# databases_final_project

## Overview

This project is the creation of a sushi restaurant data generator and data manager. Scraping ingredients for various sushi items using the Edamam API, the program then populates a Django-based restaurant application with this data. The application includes models for: menu items, ingredients, allergies, orders and payments, providing our idea of the implementation of a database for a sushi restaurant.

## Features
- Scrapes the Edamam API to extract sushi ingredients.
- Uses Python scripts to generate ingredients and menu items.
- Loads sushi menu information into a Django application.
- Manages dietary requirements and allergies for every dish on the menu.


## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Django
- MongoDB
- "dotenv" for environment variable management.
- "requests" library for API requests.
- "faker" library for data generation.

## Installation & Setup

1. Take the project files out of the repository by performing a **Clone the Repository**.

2. Install Dependencies: Install the Python modules that are necessary, as mentioned in 'requirements.txt'.

3. Set Up Environment Variables: Configure the database and API keys in the '.env_example' file.

4. Set Up Django: Make database migrations and configure Django settings.

5. MongoDB Configuration: Verify that MongoDB is operational and reachable.


