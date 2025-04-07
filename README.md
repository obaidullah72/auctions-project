# Django Real-Time Auction System

## Overview

This is a Django-based web application that provides a real-time auction system where users can place bids on items and see updates instantly using WebSockets.

## Technologies Used

- **Backend:** Django, Django Channels, Django REST Framework
- **Database:** PostgreSQL / MySQL / SQLite (Choose one)
- **Real-time Communication:** WebSockets (via Django Channels)
- **Channel Layer:** Redis
- **Frontend:** HTML/JavaScript (basic implementation, can be enhanced with React.js / Vue.js)
- **Authentication:** Django Authentication
- **Deployment:** Docker, Nginx, Gunicorn, AWS / DigitalOcean / Heroku

## Features

- Real-time bidding updates using WebSockets
- Live auction countdown capability (to be implemented)
- Multiple users can watch and bid on a single auction item
- Persistent storage of auction and bid data
- Basic bid validation

## Installation

### 1. Clone the repository

```bash
git clone https://https://github.com/obaidullah72/auctions-project.git
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
pip install -U 'channels[daphne]'
pip install channels_redis
```

### 4. Install and configure Redis

- On Ubuntu: `sudo apt-get install redis-server`
- On Mac: `brew install redis`
- Ensure Redis is running: `redis-server`

### 5. Configure environment variables

Create a `.env` file in the project root and define the necessary variables:

```env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/db_name
REDIS_URL=redis://localhost:6379/0
```

### 6. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

The project should now be running at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Usage

1. Access an auction at `/auction/<auction_id>/`
2. Place bids using the input field
3. Watch real-time updates as other users bid
4. Current highest bid updates automatically for all connected users

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

## Future Enhancements

- Add user authentication for bidding
- Implement auction countdown timer
- Display bid history
- Enhance frontend with React.js/Vue.js
- Add more robust error handling

## License

This project is licensed under the MIT License.

## Contact

For any questions or support, reach out at [obaidullah3372@gmail.com](mailto:obaidullah3372@gmail.com).
