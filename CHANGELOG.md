# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2024-03-16

### Added
- Docker support with multi-stage builds for optimized production and test environments
- Docker Compose setup with PostgreSQL database service
- Created init.sql script for initializing databases if not present
- Poetry dependency management with `pyproject.toml` and `poetry.lock`
- Docker-specific configurations with `.dockerignore`
- Containerized test environment with separate test stage

### Changed
- Updated project structure to support containerized development
- Enhanced development workflow with Docker-based testing
- Separated main and dev packages in pyproject.toml for decoupling test dependencies

### Fixed
- Bugfix with event_loop fixture for async tests

### Removed
- Removed `requirements.txt` file in favor of Poetry dependency management


## [1.0.0] - 2025-03-09

### Added
- Initial project setup with `FastAPI` framework
- Dual database access patterns with `psycopg2` (sync) and `asyncpg (async)
- SQLAlchemy 2.0+ ORM with both sync and async session management
- Comprehensive test suite using `pytest` with async support
- Code coverage reporting with `pytest-cov`
- HTML test reports via `pytest-html`
- CORS middleware configuration
- Type validation with Pydantic v2
- Project documentation and README
- Structured project layout with src/, tests/, and report/ directories
- Included sample pytest and coverage reports in media/ directory for reference



[1.1.0]: https://github.com/ysskrishna/fastapi-sync-async-starter/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/ysskrishna/fastapi-sync-async-starter/releases/tag/v1.0.0