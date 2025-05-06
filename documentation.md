# Todo Application Documentation

## 1. Project Overview

### Purpose
The Todo Application is a minimal, full-stack web application designed to help users manage tasks with simplicity and efficiency. It showcases a modern technology stack, clean architecture, and a modular design that serves as a strong foundation for further development.

### Primary Goals
- Deliver a functional and minimal to-do app using modern tools
- Emphasize modularity, scalability, and maintainability
- Implement a clean and testable architecture
- Serve as a hands-on learning project for full-stack web development
- Showcase CI/CD and deployment workflows with Docker

---

## 2. User Stories & Use Cases

### 2.1 User Stories
As a user, I want to:
- Create new tasks to track my responsibilities
- View my list of tasks to manage what I need to do
- Mark tasks as completed to monitor progress
- Delete tasks that are no longer relevant

### ✅ 2.2 Use Cases

#### UC1: Task Creation
- **Actor:** User
- **Preconditions:** Application is accessible
- **Flow:**
  1. User enters task title
  2. User submits task
  3. System validates and saves task
  4. UI updates with new task
- **Alternative Flow:** Display error on validation failure

#### UC2: Task Completion
- **Actor:** User
- **Preconditions:** Task exists
- **Flow:**
  1. User toggles completion checkbox
  2. System updates task status
  3. UI reflects the change
- **Alternative Flow:** Display error if update fails

#### UC3: Task Deletion
- **Actor:** User
- **Preconditions:** Task exists
- **Flow:**
  1. User clicks delete
  2. Task is removed from database
  3. UI refreshes the list
- **Alternative Flow:** Display error if deletion fails

---

## 3. Software Architecture

### 3.1 Architecture Model
The project follows a layered architecture, promoting separation of concerns:

```
[Frontend (React + Tailwind)]
         ↓ HTTP/JSON (RestAPI)
[API Layer (FastAPI)]
         ↓
[Service Layer (Business Logic)]
         ↓
[Repository Layer (SQLAlchemy)]
         ↓
[Database (PostgreSQL)]
```

### 3.2 Justification
Benefits of this layered architecture:
- Modular and maintainable codebase
- Easier testing and debugging
- Scalable structure for future features
- Independent development per layer

## 4. System Design

### 4.1 Component Descriptions

#### Frontend (`/frontend`)
- Built with React and Tailwind CSS
- Axios used for RESTful API interaction
- Functional components with React Hooks
- Unit tested with Jest and Testing Library

#### Backend (`/backend`)
- FastAPI framework for APIs
- Pydantic models for validation
- SQLAlchemy ORM for DB operations
- Alembic for database migrations

### 4.2 Database Design

```
Table: todos
+------------+--------------+---------------------------+
| Column     | Type         | Description               |
+------------+--------------+---------------------------+
| id         | Integer (PK) | Unique task identifier     |
| title      | String       | Description of the task    |
| completed  | Boolean      | Task completion status     |
| created_at | Timestamp    | Record creation time       |
+------------+--------------+---------------------------+
```

---

### 4.3 API Documentation
FastAPI automatically creates the documentation of the REST endpoints, accessible through `/docs`.

## 5. Testing

### 5.1 Unit Testing
- **Backend:** Pytest tests API routes and services
- **Frontend:** Jest & React Testing Library validate UI functionality

### 5.2 Test Scenarios

**1. Task Creation Flow**
- Input task title
- Submit form
- Expect task in list and in DB

**2. Task Completion Flow**
- Toggle checkbox
- Verify UI and DB status update

**3. Task Deletion Flow**
- Click delete
- Task is removed from UI and DB

---

## 6. DevOps and Deployment

### 6.1 CI/CD Pipeline

```
[GitHub Push] → [GitHub Actions]
       ↓
 ┌────────────┐   ┌────────────┐
 │ Run Backend│   │ Run Frontend│
 │   Tests    │   │    Tests    │
 └─────┬──────┘   └─────┬──────┘
       ↓                ↓
[Docker Build for Backend + Frontend]
       ↓
[Push to Container Registry]
       ↓
[Render Auto Deployment (Free Tier)]
```

### 6.2 Deployment Architecture

```
[Browser Client]
      ⇅
[Nginx - Frontend Container]
      ⇅
[FastAPI - Backend Container]
      ⇅
[PostgreSQL - Database Container]
```

### 6.3 Infrastructure Details

```
Production Stack:
─────────────────────────────────────
│ Component │ RAM    │ CPU   │ Port │
├───────────┼────────┼───────┼──────┤
│ Frontend  │ 512 MB │ 0.5   │ 80   │
│ Backend   │ 512 MB │ 0.5   │ 8000 │
│ Database  │ 1 GB   │ 1.0   │ 5432 │
─────────────────────────────────────
│ Volumes:                          │
│ - DB: 5GB                         │
│ - Logs: 1GB                       │
│ Network:                          │
│ - Internal Docker Network         │
│ External Access: HTTPS (via Render)
─────────────────────────────────────

Requirements:
- Docker Engine 20.10+
- Docker Compose 2.0+
- HTTPS certificate (via Render)
```

---

## 7. Work Environment

### 7.1 Repository Structure

```
/
├── frontend/             # React client
├── backend/              # FastAPI server
├── docker-compose.yml    # Multi-container orchestration
└── documentation.md      # Project docs
```

### 7.2 GitHub Actions Workflow

`/.github/ci-cd.yml` is the GitHub actions workflow configuration, used for CI/CD, and does the following:
- Backend and frontend linting and static code analysis
- Backend and frontend tests
- Docker containerization
- Building (without pushing)
- Render is set up to redeploy on each push to the main branch

---

## 8. Code Quality

### Tools Used

#### Backend
- **Black** – Code formatting
- **Flake8** – Linting
- **MyPy** – Type checking

#### Frontend
- **ESLint** – Linting
- **Prettier** – Code formatting

### CI Integration
All quality checks are enforced via GitHub Actions:
- Lint checks on PR
- Tests on commit
- Type checks on backend

---

## 9. Conclusion

### Completed Features
- Core CRUD operations
- CI/CD automation
- Containerized backend & frontend
- Unit and integration tests
- Deployment on Render (auto deploy on commit)

### Limitations:


### Future Enhancements
- Authentication system
- Task categories/tags
- Task deadlines
- Search and filtering

### Learning Outcomes
- Built a full-stack web application from scratch
- Gained hands-on experience with modern deployment tools
- Practiced CI/CD, testing, and Dockerization
- Applied clean and layered architecture design principles

## 10. Running

You can run this project locally with `docker-compose up` (frontend is accessible at port 8000, backend at 3000, and database at 5432). It is deployed on render at `https://to-do-frontend-1by4.onrender.com/`. Backend is at `https://to-do-backend-ds3k.onrender.com/`.
