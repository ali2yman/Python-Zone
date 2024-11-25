<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crowd-Funding Console App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f9;
            color: #333;
        }
        h1, h2 {
            color: #444;
        }
        pre {
            background-color: #f0f0f0;
            padding: 10px;
            border: 1px solid #ddd;
            overflow-x: auto;
        }
        code {
            color: #c7254e;
            background-color: #f9f2f4;
            padding: 2px 4px;
            border-radius: 4px;
        }
        ul {
            list-style: disc;
            padding-left: 20px;
        }
        a {
            color: #3498db;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .menu {
            background-color: #fff;
            padding: 10px;
            border: 1px solid #ddd;
        }
    </style>
</head>
<body>
    <h1>Crowd-Funding Console App</h1>
    <p>The Crowd-Funding Console App is a command-line application designed to allow users to create and manage crowdfunding campaigns. It includes an authentication system, project management features, and user-friendly data validation.</p>

    <h2>Features</h2>
    <h3>1. Authentication System</h3>
    <ul>
        <li><strong>Registration:</strong> Users can register by providing the following information:
            <ul>
                <li>First Name</li>
                <li>Last Name</li>
                <li>Email (validated using regex)</li>
                <li>Password (with confirmation)</li>
                <li>Mobile Phone (validated against Egyptian phone numbers)</li>
            </ul>
        </li>
        <li><strong>Login:</strong> Users can log in using their email and password after registration.</li>
    </ul>

    <h3>2. Project Management</h3>
    <ul>
        <li><strong>Create a Campaign:</strong>
            <ul>
                <li>Title</li>
                <li>Details</li>
                <li>Total Target (e.g., 250,000 EGP)</li>
                <li>Start and End Date (validated using regex)</li>
            </ul>
        </li>
        <li><strong>View All Projects:</strong> Users can view all active projects.</li>
        <li><strong>Edit a Project:</strong> Only the owner of a project can edit its details using its title to locate it.</li>
        <li><strong>Delete a Project:</strong> Only the owner of a project can delete it.</li>
        <li><strong>Search for a Project (Bonus):</strong> Users can search for projects using a date.</li>
    </ul>

    <h2>Files Overview</h2>
    <h3>1. <code>data.json</code></h3>
    <p>Stores user data including:</p>
    <ul>
        <li>First Name</li>
        <li>Last Name</li>
        <li>Email</li>
        <li>Password</li>
        <li>Mobile Phone</li>
    </ul>

    <h3>2. <code>projects.json</code></h3>
    <p>Stores project data including:</p>
    <ul>
        <li>Owner (email for uniqueness)</li>
        <li>Title</li>
        <li>Details</li>
        <li>Total Target</li>
        <li>Start Date</li>
        <li>End Date</li>
    </ul>

    <h3>3. <code>validation.py</code></h3>
    <p>Contains validation logic for:</p>
    <ul>
        <li><strong>Email:</strong> Validates email format using regex.</li>
        <li><strong>Name:</strong> Ensures names meet specific criteria.</li>
        <li><strong>Password:</strong> Ensures strong passwords.</li>
        <li><strong>Phone Number:</strong> Validates Egyptian phone numbers.</li>
    </ul>

    <h3>4. <code>authentication.py</code></h3>
    <p>Handles user authentication:</p>
    <ul>
        <li><strong>Load and Save JSON Files:</strong> Reads and writes user data.</li>
        <li><strong>Register Function:</strong> Registers a new user and saves their data.</li>
        <li><strong>Login Function:</strong> Allows users to log in with valid credentials.</li>
    </ul>

    <h3>5. <code>projects.py</code></h3>
    <p>Contains functions for managing projects:</p>
    <ul>
        <li><strong>validate_date:</strong> Validates the start and end dates of a campaign using regex.</li>
        <li><strong>create_project:</strong> Allows users to create a new project.</li>
        <li><strong>view_projects:</strong> Displays all existing projects.</li>
        <li><strong>edit_project:</strong> Edits a project’s details if the user is the owner.</li>
        <li><strong>delete_project:</strong> Deletes a project if the user is the owner.</li>
        <li><strong>find_project_by_title:</strong> Locates a project by its title (used in edit and delete functions).</li>
    </ul>

    <h3>6. <code>main.py</code></h3>
    <p>Acts as the entry point of the application. Includes the main menu:</p>
    <div class="menu">
        <pre>
Crowd-Funding Console App  
----------------------------------  
1. Register  
2. Login  
3. Create Project  
4. View All Projects  
5. Edit Your Project  
6. Delete Your Project  
7. Search Projects by Date  
8. Exit
        </pre>
    </div>

    <h2>How to Run</h2>
    <ol>
        <li>Clone the repository:
            <pre>git clone https://github.com/your-repo-url.git</pre>
        </li>
        <li>Navigate to the project directory:
            <pre>cd crowd-funding-app</pre>
        </li>
        <li>Install dependencies (if any).</li>
        <li>Run the application:
            <pre>python main.py</pre>
        </li>
    </ol>

    <h2>Future Enhancements</h2>
    <ul>
        <li>Add user-friendly error messages.</li>
        <li>Implement advanced search and filtering options.</li>
        <li>Build a GUI for enhanced usability.</li>
    </ul>

    <p>Feel free to contribute and enhance the project! 😊</p>
</body>
</html>
