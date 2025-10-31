# SmartPharma Backend Project

This is the backend for the SmartPharma application, built using Django and PostgreSQL. The project utilizes Django REST Framework for building RESTful APIs and implements JWT authentication for secure access.

## Project Structure

- `manage.py`: Command-line utility for administrative tasks.
- `requirements.txt`: List of dependencies required for the project.
- `.env`: Environment variables for configuration.
- `README.md`: Project documentation.
- `core/`: Contains core settings and configurations for the Django project.
- `apps/`: Contains various Django apps for different functionalities.
- `utils/`: Contains utility functions and helpers.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd smartpharma_backend
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the environment variables in the `.env` file.

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the API at `http://localhost:8000/api/`.
- Use JWT for authentication by including the token in the headers.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License

This project is licensed under the MIT License.