# Crowdfunding Back End
Fundee

## Planning:
### Concept/Name
Fundee is a fun, approachable crowdfunding platform with the tagline "crowdfunding without the crowd." It aims to reduce project saturation by allowing only a limited number of projects at any given time and capping funding requests at $100,000. This approach ensures that each project receives ample visibility and that backers can easily find and support initiatives they're passionate about without being overwhelmed by too many options.

### Intended Audience/User Stories

**Intended Audience:**

**Project Creators:** Individuals or small teams with creative, innovative, or entrepreneurial projects requiring up to $100,000 in funding. They are looking for a platform where their projects won't be lost in a sea of other campaigns.

**Backers:** People interested in discovering and supporting unique projects without sifting through an oversaturated market. They appreciate a curated selection and enjoy being part of a community where their contributions make a significant impact.

**User Stories:**

- **As a project creator**, I want to submit my project for approval so that it can be featured on Fundee and reach potential backers.
- **As a backer**, I want to browse a curated list of projects so that I can find and support initiatives that interest me.
- **As a backer**, I want to pledge money to a project and select a reward tier so that I can support creators and receive exclusive perks.
- **As a project creator**, I want to provide updates to my backers so that they stay informed about the project's progress.
- **As a user**, I want to create a profile so that I can manage my projects or backing activities in one place.
- **As a backer**, I want to receive notifications about project updates or messages from creators I support.

### Front End Pages/Functionality
- **Home Page**
    - Highlights featured projects
    - Showcases Fundee's unique value proposition
    - Includes a call-to-action for creators and backers to sign up
- **Project Listing Page**
    - Displays a curated list of live projects
    - Allows users to filter projects by category or funding status
    - Provides search functionality
- **Project Detail Page**
    - Shows detailed information about the project, including descriptions, images/videos, and funding goals
    - Displays funding progress bar and time remaining
    - Includes reward tiers and a button to back the project
    - Features updates and comments sections for community engagement
- **User Registration/Login Page**
    - Allows users to sign up using email
    - Provides login functionality for returning users
- **User Dashboard**
    - **For Backers:**
        - Displays backed projects and their statuses
        - Shows messages and updates from creators
    - **For Creators:**
        - Allows submission of new projects for approval
        - Displays statistics on active projects (e.g., funds raised, number of backers)
        - Provides tools to post updates and interact with backers
- **About/FAQ Page**
    - Provides information about Fundee's mission and how it works
    - Answers common questions for both creators and backers
- **Contact Page**
    - Offers a way for users to get in touch with customer support

### API Spec
| URL           | HTTP Method | Purpose                     | Request Body | Success Response Code | Authentication/Authorisation        |
| --------------| ----------- | --------------------------- | ------------ | --------------------- | ------------------------------------|
| **User Authentication & Management**
| /users/       | POST        | Register a new user         | { "username", "email", "password" }        | 201 Created | Public                |
| /users/       | GET         | Retrieve a list of users    | N/A          | 200 OK                | Authenticated Users (Admin)         |
| /users/:id    | GET         | Retrieve user profile by id | N/A          | 200 OK                | Authenticated Users (Owner or Admin)|
| /users/:id    | PUT         | Update user profile by id   | { "username", "email", "first_name", "last_name", "password" }             | 200 OK              | Authenticated Users (Owner)         |
| /users/:id    | PATCH       | Partially update user profile by id | { "username", "email", "first_name", "last_name", "password" }     | 200 OK  | Authenticated Users (Owner)  | 
| /users/:id    | DELETE      | Delete user account by id   | N/A          | 200 OK                | Authenticated Users (Owner)         |
| **Projects Management**
| /projects/    | GET         | Retrieve a list of all live projects | N/A | 200 OK                | Public                              |
| /projects/    | POST        | Submit a new project for approval    | { "title", "description", "goal", "image"}| 201 Created| Authenticated Users                 |
| /projects/:id | GET         | Retrieve info on a specific project  | N/A            | 200 OK     | Public                              |
| /projects/:id | PUT         | Update project details               | { "title", "description", "image" }  | 200 OK     | Authenticated Creator (Owner)       |
| /projects/:id | DELETE      | Delete a project                     | N/A            | 200 OK     | Authenticated Creator (Owner)       |
| **Pledges Management**
| /projects/:id/pledges | GET | Retrieve all pledges for a project   | N/A            | 200 OK     | Authenticated Users (Project Owner) |
| /projects/:id/pledges | POST| Make a pledge to a project           | { "amount", "anonymous" }  | 201 Created| Authenticated Users (Backers)       |
| /projects/:id/pledges/:id   | GET    | Retrieve details of a specific pledge | N/A  | 200 OK     | Authenticated Users (Pledger or Owner)  |
| /users/:id/pledges          | GET    | Retrieve all pledges made by a user   | N/A  | 200 OK     | Authenticated Users (Owner)             |

### DB Schema
![Database Schema](https://github.com/simonewight/crowdfunding_back_end/blob/main/Fundee-Schema.svg)


### A link to the deployed project
https://fundee-app-8581d7ef280c.herokuapp.com/

### A screenshot of Insomnia, demonstrating a successful GET method for any endpoint
![local](https://github.com/simonewight/crowdfunding_back_end/blob/main/screenshots/fundee-local-GET-retrive-user-profile-by-id.png)

![heroku](https://github.com/simonewight/crowdfunding_back_end/blob/main/screenshots/fundee-heroku-GET-retrive-user-profile-by-id.png)

### A screenshot of Insomnia, demonstrating a successful POST method for any endpoint
![local](https://github.com/simonewight/crowdfunding_back_end/blob/main/screenshots/fundee-local-POST-register-new-user.png)

![heroku](https://github.com/simonewight/crowdfunding_back_end/blob/main/screenshots/fundee-heroku-POST-register-new-user.png)

### A screenshot of Insomnia, demonstrating a token being returned
![local](https://github.com/simonewight/crowdfunding_back_end/blob/main/screenshots/fundee-local-POST-get-token-user.png)

![heroku](https://github.com/simonewight/crowdfunding_back_end/blob/main/screenshots/fundee-heroku-POST-get-token-user.png)

###  Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data)

### 1. Register a New User
* Endpoint: POST /users/
* Action: Create a new user account.
* Required Data:
- username: Your desired username (must be unique).
- email: Your email address.
- password: Your password.

### Steps:

1. Send a POST request to /users/ with the required data in JSON format.
2. Ensure the Content-Type header is set to application/json.
3. On success, you'll receive a response confirming the user has been created.

### 2. Obtain an Authentication Token
* Endpoint: POST /api-token-auth/
* Action: Authenticate and receive a token for future requests.
* Required Data:
- username: Your username.
- password: Your password.

### Steps:

1. Send a POST request to /api-token-auth/ with your credentials in JSON format.
2. Ensure the Content-Type header is set to application/json.
3. On success, you'll receive an authentication token.
4. Save this token; you'll need it to authenticate future requests.

### 3. Create a New Project
* Endpoint: POST /projects/
* Action: Create a new project.
* Headers:
* Authorization: Include your token in the format Token your_auth_token_here.
* Content-Type: application/json
* Required Data:
- title: The project's title.
- description: A brief description.
- goal: Funding goal amount (e.g., 1000 for $1000).
- image: URL to an image representing the project.
- is_open: true if the project is open for pledges, false otherwise.
- date_created: (Optional) The creation date (usually auto-generated by the server).

### Steps:

1. Send a POST request to /projects/ with the project details in JSON format.
2. Include the Authorization header with your token.
3. Ensure the Content-Type header is set to application/json.
4. On success, you'll receive a response with the details of the newly created project.


