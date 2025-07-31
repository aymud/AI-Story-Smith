<div align="center">
    <h1>AI Story Smith</h1>
    <a href="https://c8d057d3-32e9-4ebc-bd70-ab84787c4379.e1-us-east-azure.choreoapps.dev">Launch App</a>
    <h2>A Choose-Your-Own-Adventure Game Powered by AI</h2>
    
<p align="center">
  <video src="https://github.com/user-attachments/assets/c093aef3-a41d-43bf-af85-9e8493e6a3b4"></video>
</p>
</div>

---

## 📌 Table of Contents

1. [Project Overview](#1--overview)
2. [Development Philosophy](#2--development-philosophy)
3. [Folder Structure](#3--folder-structure)
4. [Running the App Locally](#4--running-the-application-locally)
5. [Technology Stack](#5--technology-stack)

## `1` 🎯 Overview

**AI Story Smith** is a full-stack web application that allows users to play a dynamic "choose your own adventure" 
game, where the story is generated in real-time using OpenAI's large language models (LLMs).
Users select a theme (e.g., fantasy, sci-fi), and the app generates story prompts with branching paths. 
As users make choices, the narrative unfolds uniquely each time.

- **Frontend**: Built with React and React Router.
- **Backend**: FastAPI with SQLite database.
- **AI/LLM Integration**: OpenAI API.
- **Deployment**: CI/CD via Choreo on Azure.

## `2` 📚 Development Philosophy

A philosophy is a set of guiding principles. It provides a foundation for the project's design and implementation.
The philosophy for this project was an emphasis on both best practices and practical learning.
- **Modularity**: The system is divided into clear, independent modules (frontend and backend), each focusing 
   on specific functionalities. This allows for easier maintenance, scalability, and debugging.
- **Simplicity & Clarity**: Code is written to be easy to read and maintain.
- **Learning & Exploration**: The project was also driven by my curiosity to dive into new technologies like 
  React, FastAPI, and AI integration. It was an opportunity to deepen my understanding
  of modern web development while experimenting with real-world applications of artificial intelligence.

## `3` 📂 Folder Structure

```
├── frontend/
├──── src/                - Contains the source code for the React application
│     ├── components/          
│     ├── challenge/     
│     ├── util.js         
│     ├── App.jsx         - Core component that manages the game's logic and user interface
│     ├── main.tsx        - Entry point for rendering the React app into the HTML template
├──── index.html          - Template file which is served up when script is run
├──── .eslint.config.js   - ESLint configuration for linting code
├──── package.json        - Configuration file for npm packages and project settings
├── backend/
│     ├── .choreo/        - Choreo deployment settings
│     ├── core/           - Core operations of the application like generating the story
│     │   ├── models.py   - Pydantic models to load llm data
│     ├── database/       - Database connection
│     ├── models/         - Database table definitions along with table relationships
│     │   ├── job.py
│     │   ├── story.py    - 
│     ├── routers/        - FastAPI endpoints for the application
│     ├── schema/         - Pydantic API schemas for data validation and serializations
├──── main.py           
├──── pyproject.toml      
└── README.md
```

## `4` 🚀 Running the Application Locally
Before you begin, ensure you have met the prerequisites, and then
follow these steps to run the application locally.
> [!IMPORTANT]
>
> Because the project includes a frontend and a backend, you need to install & run each separately.

<details><summary><b>Show instructions</b></summary>

1. **Clone the repository**: Start by cloning the repository to your local machine.
2. **Navigate to the frontend/backend directory**: Go to each folder within the project's root directory.
3. **Install dependencies**
4. **Set up environment variables**:
   - Create a .env file in the backend and frontend directory.
   - Add your OpenAI API key
   - _Note: Refer to the `.env.development` file for the required environment variables._
5. Start the development server:
    ```shell
    npm run dev # For the frontend
    ```
   
    ```shell
    uv run main.py # For the backend
    ```
   _Note: Uvicorn is a web server and allows us to serve our fastapi application._

</details>

<details><summary><b>Prerequisites</b></summary>

- Python
  - uv (Python package manager) so our dependencies remain private and isolated to this project rather than the system.
  - Unlike pip, uv is faster and more efficient, offering better performance for managing the virtual environment and dependencies for the backend.
- Node.js: Make sure you have Node.js installed.
  Node.js includes npm (package manager) by default.  
  To confirm that Node.js is installed correctly, open your terminal or command prompt and run the following commands:
    - ```shell 
      node -v # Displays the current version of Node.js.
      ```
    - ```shell
      npm -v # Displays the current version of npm.
      ```
- An Integrated Development Environment (IDE)
  - PyCharm
  - Visual Studio Code
  - _Note: May need to change the python interpreter to the one in the local project._
- OpenAI Account
  - Sign up for an account at [OpenAI](https://platform.openai.com/).
  - Obtain your API key from the OpenAI dashboard.
  - Set up the environment variables in the `.env` file in the backend directory with your OpenAI API key.
  - _Note: You need to set up a payment method because the API is pay as you go._

</details>

## `5` 🛠️ Technology Stack
- **Frontend**: React, Javascript
- **Backend**: FastAPI, Python, uv (Python package manager)
  - Pydantic is used for data validation. It allows us to do python type handling and to map data 
    that’s not a python object into a python object.
  - All services like database sessions and OpenAI clients are passed into route handlers using FastAPI’s 
    dependency injection system.
  - _Note: FastAPI automatically generates API documentation, which you can view at `localhost/redoc` or `localhost/docs`._
- **AI/LLM**: OpenAI
  - Used this because it provides a powerful and flexible way to generate coding challenges. 
    Also, it is easy to use and integrate with the application.
- **Database**: SQLite
    - Database runs locally, a file that is created in the backend directory.
    - SQLAlchemy Object Relational Mapper
    - Allows us to write Python classes that represent SQL (Structured Query Language) tables, 
      making it easier to interact with the database with the python wrapper instead of writing raw SQL queries ourselves.
- CI/CD: Choreo
  - Used because it provides a simple and free way to deploy the application to Azure cloud 
    without having to manage the infrastructure.

<p align="center">
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/34a68d56-a7a9-439a-8651-1ebebbd367b2" />
</p>
<p align="center"><em>Tech Stack Diagram</em></p>

<p align="center">
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/68e320eb-88f0-4480-adb6-c90b1f9d3ca5" />
</p>
<p align="center"><em>Database Relational Model Diagram</em></p>