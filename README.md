# Crowdfunding Back End
Fundee

## Planning:
### Concept/Name
Fundee is a fun, approachable crowdfunding platform with the tagline "crowdfunding without the crowd." It aims to reduce project saturation by allowing only a limited number of projects at any given time and capping funding requests at $150,000. This approach ensures that each project receives ample visibility and that backers can easily find and support initiatives they're passionate about without being overwhelmed by too many options.

### Intended Audience/User Stories

**Intended Audience:**

**Project Creators:** Individuals or small teams with creative, innovative, or entrepreneurial projects requiring up to $150,000 in funding. They are looking for a platform where their projects won't be lost in a sea of other campaigns.

**Backers:** People interested in discovering and supporting unique projects without sifting through an oversaturated market. They appreciate a curated selection and enjoy being part of a community where their contributions make a significant impact.

**User Stories:**

**As a project creator**, I want to submit my project for approval so that it can be featured on Fundee and reach potential backers.
**As a backer**, I want to browse a curated list of projects so that I can find and support initiatives that interest me.
**As a backer**, I want to pledge money to a project and select a reward tier so that I can support creators and receive exclusive perks.
**As a project creator**, I want to provide updates to my backers so that they stay informed about the project's progress.
**As a user**, I want to create a profile so that I can manage my projects or backing activities in one place.
**As a backer**, I want to receive notifications about project updates or messages from creators I support.

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
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL           | HTTP Method | Purpose             | Request Body | Success Response Code | Authentication/Authorisation |
| --------------| ----------- | ------------------- | ------------ | --------------------- | ---------------------------- |
| /register/    | POST        | Register a new user | User object  | 201 created           | Public                       |
|     |             |         |              |                       |                              |
|     |             |         |              |                       |                              |
|     |             |         |              |                       |                              |
|     |             |         |              |                       |                              |
|     |             |         |              |                       |                              |
|     |             |         |              |                       |                              |
|     |             |         |              |                       |                              |
|     |             |         |              |                       |                              |

### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )