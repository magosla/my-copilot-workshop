# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern REST APIs using the FastAPI framework. You'll create a task management API with endpoints for creating, reading, updating, and deleting tasks, while understanding key concepts like HTTP methods, request validation, and API documentation.

## 📝 Tasks

### 🛠️ Setup and Create Your First Endpoint

#### Description

Install FastAPI and create a basic API server with a welcome endpoint. FastAPI is a modern, fast web framework for building APIs with Python, and it automatically generates interactive documentation for you!

#### Requirements

Completed program should:

- Install FastAPI and uvicorn (ASGI server) using pip
- Create a basic FastAPI application instance
- Implement a GET endpoint at the root path `/` that returns a welcome message
- Run the server and test it in your browser at `http://localhost:8000`
- View the automatic API documentation at `http://localhost:8000/docs`

**Example Output:**

```json
{
  "message": "Welcome to the Task Management API!"
}
```

### 🛠️ Build Task CRUD Endpoints

#### Description

Create a complete set of CRUD (Create, Read, Update, Delete) endpoints for managing tasks. Each task should have an ID, title, description, and completion status.

#### Requirements

Completed program should:

- Implement a POST endpoint `/tasks` to create a new task
- Implement a GET endpoint `/tasks` to retrieve all tasks
- Implement a GET endpoint `/tasks/{task_id}` to retrieve a specific task by ID
- Implement a PUT endpoint `/tasks/{task_id}` to update an existing task
- Implement a DELETE endpoint `/tasks/{task_id}` to delete a task
- Use Pydantic models to validate request and response data
- Store tasks in a Python dictionary or list (no database required for this assignment)

**Example Task Object:**

```json
{
  "id": 1,
  "title": "Complete FastAPI assignment",
  "description": "Build a REST API with FastAPI",
  "completed": false
}
```

### 🛠️ Add Data Validation and Error Handling

#### Description

Enhance your API with proper data validation rules and error handling to make it more robust and user-friendly.

#### Requirements

Completed program should:

- Add validation rules to ensure task titles are between 1 and 100 characters
- Add validation to ensure task descriptions don't exceed 500 characters
- Return appropriate HTTP status codes (200 for success, 201 for created, 404 for not found, 422 for validation errors)
- Handle the case when a user tries to access or modify a non-existent task
- Include helpful error messages in the response
- Test all validation rules using the interactive API docs

**Example Error Response:**

```json
{
  "detail": "Task with ID 999 not found"
}
```
