## Technology Stack and Software Architecture

The chosen technology stack is lightweight, modern, and well-suited for building a small-scale web-based task management application:

- **Frontend:** HTML, CSS, and JavaScript — for a fast and simple user interface.
- **Backend:** Python with FastAPI — for building a RESTful API with automatic Swagger documentation.
- **Database:** SQLite — a lightweight, file-based SQL database, perfect for development and small apps.
- **Swagger UI:** Comes built-in with FastAPI, enabling easy testing and API visualization.
- **Docker:** Used to containerize the entire application for consistent deployment.
- **CI/CD:** GitHub Actions will be used to automate testing and deployment pipelines.

### Software Architecture

The application follows a classic **Three-Tier Architecture**:

1. **Presentation Layer** – The frontend, responsible for interacting with the user.
2. **Application Layer** – The backend (FastAPI), handling all business logic.
3. **Data Layer** – The SQLite database, storing task-related data.

This model ensures separation of concerns, modularity, and allows the application to scale in complexity or size over time.

### Components Overview

#### Frontend:
- `TaskList` – displays current tasks
- `TaskForm` – for creating/editing tasks
- `SearchBar` – for filtering/searching tasks
- `TagFilter` – for organizing tasks
- `ArchivedTasks` – view completed tasks

#### Backend:
- REST endpoints (e.g., `/tasks`, `/search`, `/archive`)
- Task service logic (e.g., filtering, marking as done)
- Recurring task handler
- Database access layer (communicates with SQLite)

### Architecture Diagram

   [User Browser]
          ↓
   [Frontend: HTML/CSS/JS]
          ↓  HTTP
   [Backend: FastAPI REST API]
          ↓
   [SQLite Database]

### Extendability

This architecture is modular and easy to extend. Potential future additions include:

- Switching to a more powerful database (PostgreSQL, MySQL)
- Adding authentication (login/signup)
- Building a mobile client using the same API
- Integrating notifications or reminders
