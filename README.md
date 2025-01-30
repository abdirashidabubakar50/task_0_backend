# HNG Internship Task 0

- This is task 0 for  HNG backend internship. The project involves a public API that  returns the following information in JSON format:
        - Email Address used to register for HNG internship
        - Current datetime as an  ISO 860 formatted timestamp
        - The Github URL for the project's codebase

# Prerequisites
 - python3
 - Flask
 - Flask-Cors
    
# SETUP

 1. #### Clone the project from github
    ```bash
     git clone https://github.com/abdirashidabubakar50/task_0_backend.git
     ```
2. #### Initialize a virutal environment
    ```bash
    python3 -m venv <name>
    ```
3. #### Install dependencies
    ```bash
    pip3 install Flask
    pip3 install flask_cors
    ````
4. #### Run the app locally
    ```bash
    python3 app.py
    ```

# API Documentation

## Endpoint

```GET / ```
## Response Format
Successful response format will return the following

``` { "current_date_time": "2025-01-30T20:11:13.911165Z", "email": "abdirashidabubakar7@gmail.com", "github_url": "https://github.com/abdirashidabubakar50/task_0_backend"} ```

## Example Usage
For Usage send GET/info request to the deployed endpoint

```bash
https://task-0-backend.vercel.app/
```