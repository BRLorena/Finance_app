# MyFinanceApp

MyFinanceApp is a Flask-based API for managing financial transactions such as balances, invoices, and incomes.

## Installation

Follow these steps to set up the project environment:

1. **Clone the Repository**

- git clone https://yourrepositoryurl.com/myfinanceapp.git
- cd myfinanceapp
  <br><br>

2. **Set up a Virtual Environment**

- For Unix/MacOS:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```
- For Windows:
  ```
  python -m venv venv
  .\venv\Scripts\activate
  ```
  <br><br>

3. **Install Dependencies**

- pip install -r requirements.txt
  <br><br>

4. **Set Up Environment Variables**

- Create a `.env` file in the root directory and add the necessary configurations:

- FLASK_APP=run.py
- FLASK_ENV=development
- DATABASE_URL=YourDatabaseURL

<br><br>

5. **Initialize the Database**

- flask db upgrade
  <br><br>

6. **Run the Application**

- flask run

## Project Structure

```
/myfinanceapp/
│
├── app/
│ ├── init.py
│ ├── config.py
│ ├── models.py
│ ├── views.py
│ ├── services.py
│ ├── static/
│ ├── templates/
│ └── utilities/
│
├── migrations/
│
├── tests/
│ ├── init.py
│ ├── test_config.py
│ └── test_routes.py
│
├── venv/
│
├── .gitignore
├── requirements.txt
└── run.py
```

### Folder Descriptions

- **app/**: Contains the Flask application and its modules like configurations, models, views, and services.
- **migrations/**: Manages database schema changes.
- **tests/**: Stores tests for the application.
- **venv/**: Holds the Python virtual environment details.
- **run.py**: The entry point for the Flask application.

## Usage

Once the application is running, you can access the following API endpoints:

- **GET `/balance`**: Retrieve the current balance.
- **POST `/invoice`**: Create a new invoice.
- **PUT `/invoice/<id>`**: Update an existing invoice.
- **DELETE `/invoice/<id>`**: Delete an invoice.
- **POST `/income`**: Record a new income.
- **GET `/total-invoice`**: Get the total amount of all invoices.

## Testing

Run the following command to execute tests:

- pytest

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
