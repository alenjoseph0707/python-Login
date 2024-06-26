


# SecureLogin

SecureLogin is a Flask-based web application that allows users to sign up, log in, and log out. It includes functionalities for user registration, authentication, and session management. User login events are logged to the terminal for monitoring purposes.

## Features

- User registration (sign up)
- User authentication (log in)
- User session management (log out)
- Logging of user login events to the terminal with username and password
- Simple and responsive design

## Prerequisites

- Python 3.7+
- Flask
- Werkzeug
- JSON

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/alenjoseph0707/SecureLogin.git
   cd SecureLogin
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```sh
   pip install flask
   ```

## Usage

1. **Generate a secret key:**

   ```sh
   python generate_secret_key.py
   ```

   Copy the generated secret key and paste it in `app.secret_key` in `app.py`.

2. **Run the application:**

   ```sh
   python app.py
   ```

3. **Access the application:**

   Open your web browser and navigate to `http://127.0.0.1:5000`.

4. **Sign up and log in:**

   - Sign up with a new username and password on the signup page.
   - Log in with the newly created credentials on the login page.
   - Log out using the logout button.

## Project Structure

```
SecureLogin/
│
├── generate_secret_key.py   # Script to generate a secret key
├── users.json               # JSON file to store user data
├── app.py                   # Main application file
├── templates/
│   ├── index.html           # Home page template
│   ├── login.html           # Login page template
│   └── signup.html          # Signup page template
└── static/
    └── styles.css           # CSS styles
```

## Logging

User login events are logged to the terminal with the following format:

```
User 'username' with password 'password' logged in at 26/Jun/2024 17:05:12
```

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any bugs or improvements.

## License

This project is licensed under the MIT License.

---
