# FastAPI MCQ Management API

This FastAPI-based API manages multiple-choice questions (MCQs) stored in an Excel file. It allows users to retrieve random questions based on criteria, authenticate with Basic Auth, and enables admin users to add new questions.

## Overview

This API provides endpoints to interact with MCQs stored in an Excel file. Users can authenticate using Basic Auth and retrieve random sets of questions based on criteria like subject and type of test (use). Admin users can add new questions to the MCQ database.

### Architecture Choices

- **FastAPI**: Chosen for its high performance, type checking, and easy-to-use API creation.
- **Excel File Storage**: MCQs are stored in an Excel file for easy management.

## Endpoints

### Authentication

- **`/login`**: POST request to authenticate users using Basic Auth.

### API Endpoints

- **`/healthcheck`**: GET request to check API functionality.
- **`/questions/`**: GET request to retrieve random MCQs based on specified criteria.
- **`/questions/new`**: POST request to add new questions (admin access).

## Usage Examples

### Authentication

To authenticate, use Basic Auth with the following credentials:
- **Username**: `alice`, `bob`, `clementine` (for regular users)
- **Password**: `wonderland`, `builder`, `mandarine`

### Example Requests

#### Login
```bash
curl -X POST -u username:password http://localhost:8000/login






curl -X GET -u username:password "http://localhost:8000/questions/?count=10&use=test&type=math"




curl -X POST -u admin:4dm1N -H "Content-Type: application/json" -d '{"question": "What is 2+2?", "subject": "Math", "correct": ["4"], "use": "test", "responseA": "2", "responseB": "3", "responseC": "4", "responseD": null}' http://localhost:8000/questions/new




How to Run

# Clone this repository.
# Install dependencies listed in requirements.txt.
# Run the FastAPI server using uvicorn main:api --reload.
# Use appropriate tools (e.g., curl, Postman) to interact with the API.


Testing


# For testing the API, use the provided test_api.sh file containing sample curl requests.
# The tests cover different scenarios including successful requests, authentication failures, and adding new questions.

Expected Outcome


# Successful authentication returns a token or a success message.
# Retrieving questions should return a list of MCQs based on specified criteria.
# Adding a new question should return a success message upon completion.
# Error Handling
# Invalid authentication credentials return a 401 Unauthorized status.
# Incorrect endpoint calls return appropriate error messages.


Dependencies

fastapi
uvicorn
pandas
openpyxl
