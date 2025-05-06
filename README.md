# Todo Application

A full-stack todo application with React frontend and FastAPI backend.

## Features

- Create, read, update, and delete tasks
- Mark tasks as complete or incomplete
- Clean, responsive UI
- REST API with Swagger documentation
- Database persistence with PostgreSQL
- Containerized deployment with Docker

## Tech Stack

### Frontend
- React with TypeScript
- Vite
- Tailwind CSS
- Axios for API requests
- Jest for testing

### Backend
- Python 3.11
- FastAPI
- SQLAlchemy
- Alembic for migrations
- PostgreSQL
- Pytest for testing

### DevOps
- Docker & Docker Compose
- GitHub Actions for CI/CD

## Project Structure

```
todo-app/
├── frontend/           # React frontend
│   ├── src/            # Source code
│   │   ├── components/ # React components
│   │   ├── services/   # API services
│   │   └── types/      # TypeScript type definitions
│   ├── Dockerfile      # Frontend Docker config
│   └── ...
├── backend/            # FastAPI backend
│   ├── app/            # Application code
│   │   ├── api/        # API routes
│   │   ├── core/       # Core configuration
│   │   ├── models/     # Database models
│   │   ├── repositories/ # Data access layer
│   │   ├── schemas/    # Pydantic schemas
│   │   └── services/   # Business logic
│   ├── alembic/        # Database migrations
│   ├── tests/          # Backend tests
│   ├── Dockerfile      # Backend Docker config
│   └── ...
├── docker-compose.yml  # Docker Compose configuration
└── ...
```

## Running Locally Without Docker

### Backend

1. Set up Python 3.11 environment:
   ```
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   ```
   cp .env.example .env
   # Edit .env with your PostgreSQL credentials
   ```

3. Run migrations:
   ```
   alembic upgrade head
   ```

4. Start the backend server:
   ```
   uvicorn app.main:app --reload
   ```

5. Access the API at http://localhost:8000 and Swagger documentation at http://localhost:8000/docs

### Frontend

1. Install dependencies:
   ```
   cd frontend
   npm install
   ```

2. Start the development server:
   ```
   npm run dev
   ```

3. Access the frontend at http://localhost:5173

## Running with Docker

1. Start the application:
   ```
   docker-compose up -d
   ```

2. Access the frontend at http://localhost:3000 and the API at http://localhost:8000

3. To stop the application:
   ```
   docker-compose down
   ```

## Testing

### Backend Tests

```
cd backend
pytest
```

### Frontend Tests

```
cd frontend
npm test
```

## API Documentation

API documentation is available at http://localhost:8000/docs when the backend is running.

## License

MIT