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
- Poetry (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ysskrishna/fastapi-sync-async-starter
cd fastapi-sync-async-starter
```

2. Create and activate a virtual environment using Poetry:
```bash
# Install dependencies and create virtual environment
poetry install
```


## Running the Application

Start the FastAPI server:
```bash
poetry run python main.py
```

The API will be available at `http://localhost:8000`

### API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Testing

The project includes a comprehensive test suite using pytest. Here are the different ways to run tests:

### Run all tests
```bash
poetry run pytest
```

### Run tests with cleared cache
```bash
poetry run pytest --cache-clear
```

### Run specific test file
```bash
poetry run pytest tests/routers/test_async_endpoints.py
```

After running the test suite, detailed reports will be generated in the following locations:

- `report/pytest/index.html`: Interactive HTML report showing test results, including:
  - Test case execution summary
  - Pass/fail statistics
  - Detailed error messages and tracebacks
  - Test execution time

- `report/coverage/index.html`: Comprehensive code coverage report containing:
  - Overall coverage percentage
  - File-by-file coverage analysis
  - Line-by-line coverage highlighting
  - Missing coverage identification

You can open these HTML reports in any web browser for a detailed view of test results and coverage analysis.

Example reports are available in the repository:
- [Example Pytest Report](media/example_pytest_report/index.html): See a sample of the test execution report
- [Example Coverage Report](media/example_coverage_report/index.html): View a sample code coverage analysis


## Project Structure

```
fastapi-sync-async-starter/
├── src/
│   ├── core/                     # Core functionality (database, config)
│   ├── models/                   # SQLAlchemy models, pydantic schemas
│   └── routers/                  # API endpoints
├── tests/
│   ├── routers/                  # API endpoint tests
│   └── conftest.py               # Test configurations and fixtures
├── report/                       # Generated test and coverage reports
│   ├── coverage/                 # Coverage reports generated by pytest-cov
│   └── pytest/                   # Test reports generated by pytest-html
├── media/                        
│   ├── example_coverage_report/  # Sample coverage report
│   └── example_pytest_report/    # Sample pytest report
├── .coveragerc                   # Coverage configuration
├── .gitignore                    # Git ignore rules
├── main.py                       # Application entry point
├── pytest.ini                    # Pytest configuration
├── README.md                     # Project documentation
├── pyproject.toml                # Poetry project configuration and dependencies
├── poetry.lock                   # Poetry lock file for deterministic builds
└── .env                          # Environment variables
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
