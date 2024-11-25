# Crowd-Funding Console App

The **Crowd-Funding Console App** is a command-line application that allows users to create and manage crowdfunding campaigns. It features an authentication system, project management capabilities, and user-friendly data validation. The app is designed to facilitate the creation of fundraising projects while ensuring security and usability.

---

## Features

### **1. Authentication System**
- **Registration**:
    - First Name
    - Last Name
    - Email (validated using regex)
    - Password (with confirmation)
    - Mobile Phone (validated against Egyptian phone numbers)
- **Login**:
    - Users can log in using their email and password after successful registration.

### **2. Project Management**
- **Create a Campaign**:
    - Title
    - Details
    - Total Target (e.g., 250,000 EGP)
    - Start and End Date (validated using regex)
- **View All Projects**:
    - Users can view all active projects.
- **Edit a Project**:
    - Users can edit their own projects by locating them via the title.
- **Delete a Project**:
    - Only the owner of a project can delete it.
- **Search for a Project** *(Bonus)*:
    - Search for projects by date.

---

## File Overview

### **1. `data.json`**
Stores user data including:
- First Name
- Last Name
- Email
- Password
- Mobile Phone

### **2. `projects.json`**
Stores project data including:
- Owner (email for uniqueness)
- Title
- Details
- Total Target
- Start Date
- End Date

### **3. `validation.py`**
Handles all validation logic:
- **Email**: Validates format using regex.
- **Name**: Ensures names meet specified criteria.
- **Password**: Ensures strong password standards.
- **Phone Number**: Validates Egyptian phone numbers.

### **4. `authentication.py`**
Manages user authentication:
- **Load and Save JSON Files**: Reads and writes user data securely.
- **Register Function**: Registers new users and saves their details.
- **Login Function**: Allows users to log in with valid credentials.

### **5. `projects.py`**
Contains project management functions:
- **`validate_date`**: Validates start and end dates using regex.
- **`create_project`**: Allows users to create a new project.
- **`view_projects`**: Displays all projects.
- **`edit_project`**: Enables editing a project if the user is the owner.
- **`delete_project`**: Deletes a project only if the user is the owner.
- **`find_project_by_title`**: Locates a project by its title for editing or deletion.

### **6. `main.py`**
The main entry point of the application. Includes the following menu:
```plaintext
Crowd-Funding Console App
1. Register
2. Login
3. Create Project
4. View All Projects
5. Edit Your Project
6. Delete Your Project
7. Search Projects by Date
8. Exit
