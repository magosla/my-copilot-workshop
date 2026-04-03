"""
FastAPI Task Management API - Starter Code

This starter code provides the basic structure for your Task Management API.
Follow the assignment instructions to complete each task.

To run this application:
1. Install dependencies: pip install fastapi uvicorn
2. Run the server: uvicorn starter-code:app --reload
3. Open your browser to: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

# Create FastAPI application instance
app = FastAPI(
    title="Task Management API",
    description="A simple REST API for managing tasks",
    version="1.0.0"
)

# Pydantic model for Task data validation
class Task(BaseModel):
    """
    Task model with validation rules
    TODO: Add validation constraints (min/max length) for title and description
    """
    id: int
    title: str
    description: str
    completed: bool = False

class TaskCreate(BaseModel):
    """
    Model for creating a new task (without ID)
    TODO: Add the same validation rules as Task model
    """
    title: str
    description: str
    completed: bool = False

# In-memory storage for tasks (replace with a database in production)
tasks_db = {}
next_task_id = 1


# TODO: Task 1 - Create a welcome endpoint
@app.get("/")
def read_root():
    """
    Welcome endpoint
    Returns a greeting message for the API
    """
    # TODO: Return a welcome message dictionary
    pass


# TODO: Task 2 - Implement CRUD endpoints

@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    """
    Create a new task
    
    Args:
        task: TaskCreate object with task details
        
    Returns:
        Created task with assigned ID
    """
    # TODO: 
    # 1. Use global next_task_id to assign an ID
    # 2. Create a new task with the ID
    # 3. Store it in tasks_db
    # 4. Increment next_task_id
    # 5. Return the created task
    pass


@app.get("/tasks")
def get_all_tasks():
    """
    Retrieve all tasks
    
    Returns:
        List of all tasks
    """
    # TODO: Return all tasks from tasks_db as a list
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    """
    Retrieve a specific task by ID
    
    Args:
        task_id: ID of the task to retrieve
        
    Returns:
        Task object if found
        
    Raises:
        HTTPException: 404 if task not found
    """
    # TODO: 
    # 1. Check if task_id exists in tasks_db
    # 2. If found, return the task
    # 3. If not found, raise HTTPException with status_code=404
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate):
    """
    Update an existing task
    
    Args:
        task_id: ID of the task to update
        task: Updated task data
        
    Returns:
        Updated task object
        
    Raises:
        HTTPException: 404 if task not found
    """
    # TODO:
    # 1. Check if task exists
    # 2. Update the task in tasks_db
    # 3. Return the updated task
    # 4. Raise 404 if not found
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    """
    Delete a task
    
    Args:
        task_id: ID of the task to delete
        
    Returns:
        Success message
        
    Raises:
        HTTPException: 404 if task not found
    """
    # TODO:
    # 1. Check if task exists
    # 2. Delete it from tasks_db
    # 3. Return a success message
    # 4. Raise 404 if not found
    pass


# TODO: Task 3 - Add validation and improve error handling
# Update the Task and TaskCreate models above with Field() validators:
# - title: min_length=1, max_length=100
# - description: max_length=500
#
# Example:
# title: str = Field(..., min_length=1, max_length=100, description="Task title")


# Bonus: Add a PATCH endpoint to toggle task completion status
@app.patch("/tasks/{task_id}/toggle")
def toggle_task_completion(task_id: int):
    """
    Toggle the completion status of a task
    
    Args:
        task_id: ID of the task to toggle
        
    Returns:
        Updated task
    """
    # TODO: Implement this bonus endpoint
    pass


if __name__ == "__main__":
    import uvicorn
    # Run the server when this file is executed directly
    uvicorn.run(app, host="0.0.0.0", port=8000)
