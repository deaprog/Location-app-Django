# LocationApp

This repository contains a Django backend and Angular frontend for managing hierarchical location data (Country, State, City, Zip Code). The application allows users to inject data from an SQLite file, serve it through APIs, and display it in a frontend application.

---

### Features

- List countries, states, cities, and zip codes.
- Implement search filters for partial matches (e.g., "ort" returns "Portugal").
- Filter sub-items based on parent relationships (e.g., states by country, cities by state).

---

## Project Structure

The project has the following key components:

- **Frontend**: Built using Angular.
- **Backend**: A Django REST framework providing the APIs.
- **Data**: Imported from an SQLite database into Django models and served through APIs.

---

## Setup and Installation

### 1. Clone the Repository
Clone the project from your version control system:

```bash
git clone <repository-url>
```
### 2. Navigate to the cd location_project directory:

```bash
cd cd location_project
```

### 3. Set Up a Virtual Environment:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 4. Install Dependencies:

```bash
pip install -r requirements.txt
```

### 5. Run Migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Run the Development Server:

```bash
python manage.py runserver
```

## Unit Testing

```bash
python manage.py test
```
