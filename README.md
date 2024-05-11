# Django Analytics Project

This is a Django project for analytics purposes, featuring a dashboard with pivot tables and charts. 
This project leverages Django, Python, and Flexmonster Pivot Table & Charts to transform raw data into interactive visualizations.

## Key Tools and Technologies used

1. Python
2. Django
3. Virtual Environment
4. Flexmonster Pivot Table & Charts (JavaScript library)
5. SQLite

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AnaghaARao/Analytics_Project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd django-analytics-project
    ```

3. Install the required dependencies

4. Run migrations to create the database schema:

    ```bash
    python manage.py migrate
    ```

## Usage

1. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

2. Access the dashboard by visiting [http://127.0.0.1:8000/dashboard/](http://127.0.0.1:8000/dashboard/) in your web browser.

## Features

- **Dashboard with Pivot Tables**: The dashboard provides an interactive interface with pivot tables generated using Flexmonster.
- **Charts**: Charts are included on the dashboard to visualize data.
- **Data Source**: Data is fetched from the `Order` model and serialized as JSON for use in the dashboard.
