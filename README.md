# Django Images Utils

## Overview

This is a Django-based web application that provides a backend for Images.

## Technologies Used

- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL / MySQL / SQLite (Choose one)
- **Frontend:** React.js / Vue.js (if applicable)
- **Authentication:** JWT / OAuth / Django Authentication
- **Deployment:** Docker, Nginx, Gunicorn, AWS / DigitalOcean / Heroku

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/muhammad-hamza-liaqat/python-images-utils.git
cd server
```

### 2. Create and activate a virtual environment

```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and define the necessary variables:

```env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/db_name
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

The project should now be running at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## API Documentation

If using Django REST Framework, navigate to:

```
http://127.0.0.1:8000/api/
```

For API schema documentation, consider using tools like Swagger (`drf-yasg`) or ReDoc.

## Running Tests

```bash
python manage.py test
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request

## License

This project is licensed under the MIT License.

## Contact

For any questions or support, reach out at [mh408800@gmail.com](mailto:mh408800@gmail.com).
