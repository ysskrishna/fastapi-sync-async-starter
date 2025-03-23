# FastAPI Sync-Async Starter

A modern Python web application template built with FastAPI, demonstrating sync vs async operations using SQLAlchemy 2.0, psycopg2, and asyncpg. Features comprehensive testing with pytest-asyncio and pytest-cov, includes Docker support with multi-stage builds, Poetry for dependency management, and production-ready rate limiting with Redis support.

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
  - Containerized test environment with separate test stage

- **Production Features**
  - CORS middleware configuration
  - Type validation with Pydantic v2
  - Clean and scalable project structure
  - Docker support with multi-stage builds
  - Containerized development environment
  - Poetry dependency management
  - Optimized production and test environments
  - Rate limiting with Redis support:
    - Basic rate limiting (5 requests/minute)
    - Shared rate limiting across endpoints
    - Burst rate limiting (5/minute; 10/hour)
    - Rate limiting for slow endpoints
    - Environment-based configuration (Redis for production, memory for testing)

## Prerequisites

- Python 3.8+
- PostgreSQL database
- Redis (for rate limiting in production)
- Poetry 2.1.1 (Python package manager)
- Docker and Docker Compose (for containerized development)

## Installation

### Local Development Setup

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

### Docker Setup

1. Build and start the containers:
```bash
docker-compose up --build
```

This will:
- Build the FastAPI application container with multi-stage optimization for development and production
- Start a PostgreSQL database container with persistent volume
- Start a Redis container for rate limiting
- Set up the necessary networks and volumes
- Initialize the database with the provided schema
- Run api-tests and generate pytest and coverage reports
- Manage environment variables automatically

## Running the Application

### Local Development
Start the FastAPI server:
```bash
poetry run python main.py
```

### Docker Environment
The application will automatically start when using Docker Compose:
```bash
docker-compose up
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
│   ├── core/                     # Core functionality (database, config, rate limiting)
│   ├── models/                   # SQLAlchemy models, pydantic schemas
│   └── routers/                  # API endpoints
├── tests/
│   ├── routers/                  # API endpoint tests
│   └── conftest.py               # Test configurations and fixtures
├── scripts/                      # Utility scripts
├── report/                       # Generated test and coverage reports
│   ├── coverage/                 # Coverage reports generated by pytest-cov
│   └── pytest/                   # Test reports generated by pytest-html
├── media/                        
│   ├── example_coverage_report/  # Sample coverage report
│   └── example_pytest_report/    # Sample pytest report
├── .coveragerc                   # Coverage configuration
├── .dockerignore                 # Docker ignore rules
├── .env                          # Environment variables
├── .gitignore                    # Git ignore rules
├── CHANGELOG.md                  # Project changelog
├── docker-compose.yml           # Docker Compose configuration
├── Dockerfile                   # Docker build configuration
├── main.py                      # Application entry point
├── pytest.ini                   # Pytest configuration
├── pyproject.toml               # Poetry project configuration
├── poetry.lock                  # Poetry lock file
└── README.md                    # Project documentation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
