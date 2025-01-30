
---

# HNG Internship Task 0

This is **Task 0** for the **HNG Backend Internship**. The project involves building a simple public API that returns specific information in JSON format. The API provides the following details:

- **Email Address**: The email used to register for the HNG Internship.
- **Current Datetime**: The current date and time in ISO 8601 format.
- **Github URL**: The URL of the project's codebase on GitHub.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Flask
- Flask-CORS

---

## Setup

Follow these steps to set up and run the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/abdirashidabubakar50/task_0_backend.git
   cd task_0_backend
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install Flask flask_cors
   ```

5. **Run the Application**:
   ```bash
   python app.py
   ```

6. **Access the API**:
   Open your browser or use a tool like `curl` or Postman to access the API at:
   ```
   http://127.0.0.1:5000/
   ```

---

## API Documentation

### Endpoint

- **GET `/`**

### Response Format

A successful response will return the following JSON structure:
```json
{
  "current_date_time": "2025-01-30T20:11:13.911165Z",
  "email": "abdirashidabubakar7@gmail.com",
  "github_url": "https://github.com/abdirashidabubakar50/task_0_backend"
}
```

### Example Usage

You can test the API by sending a `GET` request to the deployed endpoint:
```bash
curl https://task-0-backend.vercel.app/
```

---

## Deployment

This project is deployed on **Vercel**. You can access the live API here:
```
https://task-0-backend.vercel.app/
```

---

## Backlinks

- [HNG Internship Hire Page](https://hng.tech/hire/python-developers)

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push your branch and submit a pull request.

---

## Author

- **Abdirashid Abubakar**
- Email: [abdirashidabubakar7@gmail.com](mailto:abdirashidabubakar7@gmail.com)
- GitHub: [abdirashidabubakar50](https://github.com/abdirashidabubakar50)

---
