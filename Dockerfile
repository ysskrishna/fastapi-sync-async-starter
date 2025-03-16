# Use the official Python image
FROM python:3.12-slim as base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=2.1.1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

# Install dependencies
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get remove -y curl && apt-get autoremove -y

# Set path for Poetry
ENV PATH="/root/.local/bin:$PATH"

# Set work directory
WORKDIR /app

# Copy only essential files
COPY pyproject.toml poetry.lock ./

# # Ensure poetry.lock is up to date. Uncomment this to update the lock file while building the image.
# RUN poetry lock --no-update

# Install dependencies only for main
RUN poetry install --no-root --only main

# Copy the rest of the application
COPY . .


# ==========================
# Testing Stage
# ==========================

FROM base as test

# Install dev dependencies for testing
RUN poetry install --with dev

# Default command for test stage
CMD ["poetry", "run", "pytest"]


# ==========================
# Production Stage
# ==========================

FROM base as production

# Expose the port the app runs on
EXPOSE 8000

# Default command to run the production stage
CMD ["poetry", "run", "python", "main.py"] 