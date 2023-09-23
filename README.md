# PIZZA-RESTAURANT


This is a Flask-based RESTful API for managing pizza restaurants and their menus. The API allows you to perform CRUD (Create, Read, Update, Delete) operations on restaurants, view available pizzas, and create associations between restaurants and pizzas.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [API Routes](#api-routes)
- [Project Structure](#project-structure)
- [Author](#author)
- [License](#license)

## Getting Started

### Prerequisites

Before you can run this application, you need to have the following installed:

- Python 3.10.12
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- SQLite (or another relational database)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Uel-s/PIZZA-RESTAURANT
   ```

2. Navigate to the project directory:

   ```bash
   cd pizza-restaurant
   ```

3. Create a virtual environment and activate it:

   ```bash
   pipenv --python 3.10.12 install and pipenv shell
   
   ```

4. Install the required packages:

   ```bash
   cd server
   ```

5. Set up the database:

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

## Usage

### Running the Application

To run the application, execute the following command:

```bash
python3 app.py
```

The API will be available at `http://localhost:5555`.

### API Routes

The API offers the following routes:

- **GET /restaurants**: Get a list of all restaurants.

- **GET /restaurants/:id**: Get information about a specific restaurant by providing its `id`.

- **DELETE /restaurants/:id**: Delete a restaurant and its associated menu items (pizzas) by providing its `id`.

- **GET /pizzas**: Get a list of all available pizzas.

- **POST /restaurant_pizzas**: Create a new menu item by associating an existing pizza with a restaurant. You should provide a JSON object with the following properties in the request body:

  ```json
  {
    "price": 5,
    "pizza_id": 1000,
    "restaurant_id": 3
  }
  ```

  

Example usage:

- To get a list of all restaurants: `GET http://localhost:5555restaurants`

- To get information about a specific restaurant: `GET http://localhost:5555/restaurants/:id`

- To delete a restaurant: `DELETE http://localhost:5555/restaurants/:id`

- To get a list of all available pizzas: `GET http://localhost:5555/pizzas`

- To create a new menu item: `POST http://localhost:5555/restaurant_pizzas` with the JSON data in the request body.

## Project Structure

The project structure is organized as follows:

- `app.py`: The main Flask application file containing the API routes and initialization code.

- `model.py`: Defines the database models using SQLAlchemy, including `Pizzas`, `Restaurants`, and `Restaurant_Pizzas`.

- `migrations/`: Contains database migration files generated by Flask-Migrate.

- `venv/`: The virtual environment where Python packages are installed.

- `requirements.txt`: Lists the required Python packages for the project.

## AUTHOR

[AUTHOR](#kariukiwaweru@gmail.com)





## LICENSE

[LICENSE](#license)