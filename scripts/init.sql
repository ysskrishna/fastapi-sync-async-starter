SELECT 'CREATE DATABASE fastapi_starter'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'fastapi_starter')\gexec

SELECT 'CREATE DATABASE fastapi_starter_test_db'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'fastapi_starter_test_db')\gexec