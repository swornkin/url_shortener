# url_shortener

A simple and functional URL shortening service built with Flask and SQLite, featuring:
- RESTful API
- Click tracking & stats
- Dockerized setup
- Basic automated test suite using pytest

---

## Features

- Shortens long URLs into unique codes
- Tracks clicks and timestamps
- Redirects users from short URLs to original ones
- Includes test for core functionality
- Docker support for easy deployment

---

## Project Structure

```bash
url_shortener/
│
├── app.py             # Main Flask app with routes
├── database.py        # SQLite setup and connection
├── test_routes.py     # Basic test with pytest
├── requirements.txt   # Dependencies
├── Dockerfile         # Docker setup
└── README.md          # Project overview
```

---

## API Usage

### POST /shorten

**Request:**
```json
{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "short_url": "http://localhost:5000/abc123"
}
```

---

### GET /<short_code>

Redirects to the original URL.

---

### GET /stats/<short_code>

**Response:**
```json
{
  "short_code": "abc123",
  "clicks": 7
}
```

---

## Running Tests

```bash
pytest test_routes.py
```

---

## Docker

Build and run:

```bash
docker build -t url-shortener .
docker run -p 5000:5000 url-shortener
```

Then access the app at: http://localhost:5000

---

## Tech Stack

- Python 3.11
- Flask
- SQLite
- pytest
- Docker

---

## License

This project is for learning and demonstration purposes.

---

## Created by Markellos Stylianou (https://github.com/swornkin)
