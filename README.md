# Django Support Chat Application

A clean, scalable, and responsive customer support chat application built with Django. This project acts as a foundation for a full-scale AI-integrated support system.

## Features
- **Modern UI**: Responsive landing page and dynamic chat interface.
- **Dynamic Messaging**: Fetch API integration for real-time messaging without full page reloads.
- **Model Architecture**: Dedicated `Conversation` and `Message` models following Django best practices.
- **Extensible API**: The `MessageAPIView` is designed to seamlessly integrate with LLM APIs (like OpenAI) or webhook services in the future.

## Setup Instructions

### Prerequisites
- Python 3.x
- Django 4.x/5.x

### Installation
1. Clone the repository and navigate into it.
2. Ensure you have Django installed (`pip install django`).
3. Apply the database migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```
5. Access the application in your browser at `http://127.0.0.1:8000/`.
