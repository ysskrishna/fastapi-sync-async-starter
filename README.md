# FastAPI Sync-Async Starter

A modern Python web application template built with FastAPI, demonstrating sync vs async operations using SQLAlchemy 2.0, psycopg2, and asyncpg. Features comprehensive testing with pytest-asyncio and pytest-cov, plus Pydantic v2 for type safety.

## Features

- **FastAPI Framework Integration**
  - Modern Python web framework with automatic OpenAPI documentation
  - Built-in Swagger UI and ReDoc interfaces
  - High-performance ASGI server with uvicorn

- **Database Layer**
  - Dual database access patterns with `psycopg2` (sync) and `asyncpg` (async)
  - SQLAlchemy 2.0+ ORM with both sync and async session management
  - Type-safe database operations and model relationships
  - Structured database schema management

- **Testing Infrastructure**
  - Comprehensive test suite using `pytest`
  - Async endpoint testing with `pytest-asyncio`
  - Code coverage reporting with `pytest-cov`
  - HTML test reports via `pytest-html`
  - Database fixtures and test data management

- **Production Features**
  - CORS middleware configuration
  - Type validation with Pydantic v2
  - Clean and scalable project structure

## Prerequisites

- Python 3.8+
- PostgreSQL database
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ysskrishna/fastapi-sync-async-starter
cd fastapi-sync-async-starter
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```


## Running the Application

Start the FastAPI server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Testing

The project includes a comprehensive test suite using pytest. Here are the different ways to run tests:

### Run all tests
```bash
pytest
```

### Run tests with cleared cache
```bash
pytest --cache-clear
```

### Run specific test file
```bash
pytest tests/routers/test_async_endpoints.py
```


## Project Structure

```
fastapi-sync-async-starter/
├── src/
│   ├── core/          # Core functionality (database, config)
│   ├── models/        # SQLAlchemy models, pydantic schemas
│   └── routers/       # API endpoints
├── tests/
│   ├── routers/       # API endpoint tests
│   └── conftest.py    # Test configurations and fixtures
├── .coveragerc        # Coverage configuration
├── .gitignore         # Git ignore rules
├── main.py            # Application entry point
├── pytest.ini         # Pytest configuration
├── README.md          # Project documentation
├── requirements.txt   # Project dependencies
└── .env               # Environment variables
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
