# Redis Cache Service (FastAPI + Redis)

A production-style FastAPI service demonstrating:

* Async Redis integration
* External API caching
* Lifespan management
* Structured Pydantic schemas
* Unit testing + E2E testing
* Code quality tooling (Ruff, Black, MyPy, Pylint, Bandit)

---

## 📦 Tech Stack

* Python 3.11+
* FastAPI
* Redis (async)
* httpx
* Pydantic v2
* pytest
* uv (package manager)

---

## 📂 Project Structure

```
redis-practice/
│
├── app/
│   ├── main.py
│   ├── cache.py
│   ├── config.py
│   └── schemas.py
│
├── tests/
│   ├── conftest.py
│   ├── test_cache.py
│   └── test_e2e.py
│
├── pyproject.toml
├── .env.example
└── README.md
```

---

# Setup

## 1️⃣ Clone the repository

```
git clone <your-repo-url>
cd redis-practice
```

## 2️⃣ Install uv (if not installed)

```
pip install uv
```

## 3️⃣ Install dependencies

```
uv sync
```

This installs runtime and development dependencies.

---

# Environment Configuration

Create a `.env` file in the project root.

Example:

```
REDIS_HOST=XXXX
REDIS_PORT=XXXX
CACHE_TTL_SECONDS=XXXX
THIRD_PARTY_URL=XXXX
```

You can copy from `.env.example`.

---

# Running Redis Locally

You must have Redis running.

## Option A — Install locally

Mac:

```
brew install redis
redis-server
```

Linux:

```
sudo apt install redis-server
redis-server
```

## Option B — Run using Docker (Recommended)

```
docker run -p 6379:6379 redis
```

---

# Run the Application

```
uv run uvicorn app.main:app --reload
```

Open Swagger documentation:

```
http://localhost:8000/docs
```

Endpoint:

```
GET /random-users
```

---

# How It Works

### First Request

* Fetches data from third-party API
* Transforms response
* Stores result in Redis with TTL
* Returns `"source": "api"`

### Subsequent Requests (within TTL)

* Returns cached data
* Returns `"source": "cache"`

---

# Testing

We use:

* pytest
* pytest-asyncio
* httpx ASGITransport
* asgi-lifespan

## Run All Tests

```
uv run pytest
```

## Run With Verbose Output

```
uv run pytest -v
```

## Fail on Warnings

```
uv run pytest -W error
```

---

# What Is Tested

## ✅ Unit Tests

* RedisCache.get()
* RedisCache.set()
* RedisCache.delete()
* RedisCache.exists()
* JSON parsing
* Redis error handling

## ✅ End-to-End Test

* Full request lifecycle
* FastAPI lifespan
* Redis integration
* Cache hit/miss behavior

---

# Code Quality & Static Analysis

## Ruff (Lint)

```
uv run ruff check .
```

## Black (Formatter)

```
uv run black .
```

## MyPy (Type Checking)

```
uv run mypy .
```

## Bandit (Security Scan)

```
uv run bandit -r app
```

## Pylint (Code Quality Score)

```
uv run pylint app
```

---

# Architecture Overview

* Redis abstraction layer (`RedisCache`)
* Environment configuration via `BaseSettings`
* Async lifespan initialization
* Typed response models
* Dependency-injected cache instance
* Clean separation of concerns

---

# Production Considerations

To evolve this into a production-grade microservice:

* Use Redis Cluster or managed Redis (AWS ElastiCache, Azure Cache, etc.)
* Add health check endpoint
* Add structured logging
* Add metrics (Prometheus)
* Add Dockerfile
* Add CI pipeline
* Add cache stampede protection
* Add upstream retry strategy

---

# Learning Goals Demonstrated

* Async FastAPI architecture
* Redis caching strategies
* Clean abstraction design
* Proper testing architecture
* Dependency lifecycle management
* Production-ready coding standards

---

# 🏁 Final Notes

This project is a learning-focused backend microservice demonstrating real-world patterns used in production systems.

It reflects professional backend engineering practices and scalable architecture principles.
