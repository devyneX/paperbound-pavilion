## Description

Paperbound Pavilion is an online bookstore where customers can buy and review their
favorite books. The system allows the users to easily find and order books. They have the
option to pay both online and with cash on delivery. The platform also allows users to rate
and review different books.

## Features

### Authentication

#### Login using email
Users can sign in to their accounts using their registered email address and password. They'll enter their email and password in designated fields and may have the option to stay logged in for convenience.

#### Registration
New users can create accounts by providing a username, email, and password. They may also fill in optional fields like their full name or date of birth. After filling out the form, they'll typically need to verify their email address to complete the registration process.

#### Logout
Users can log out of their accounts, which clears their session data and effectively signs them out of the platform. After logging out, they're usually redirected to the homepage or login page.

### Homepage

#### Bestsellers
The homepage features a section showcasing products that are top sellers. These products are displayed in a visually appealing manner, often with images, titles, and prices. Users can scroll through the list and may have options to filter or sort the bestsellers based on different criteria.

#### Popular on the website
Another section highlights items or content that are currently trending or highly popular among users. This section typically includes thumbnails or previews of the popular items, along with their titles and possibly ratings. The content shown here may be personalized based on the user's interests or browsing history.

###  User Dashboard

####  Profile Info
Users can view and manage their profile information from the dashboard. This includes details such as their username, email address, and any additional information they've provided during registration.

####  Order History
The dashboard displays a history of the user's past orders, including details such as order dates, items purchased, and order statuses.

####  Addresses
Users can manage their shipping and billing addresses from the dashboard. They can add new addresses, edit existing ones, and delete outdated ones.

####  Reviews
Users can view and manage any reviews they've submitted for products on the platform. They can edit or delete their reviews as needed.

###  Update profile information
-  **Name:**  Users have the option to update their displayed name on the platform.
-  **Email:**  Users can change their email address associated with their account.
- **Phone No:** Users can add or update their phone number in their profile information.
- **Password:** Users can update their account password for improved security.

###  Cart
####  Add Books to Cart
Users can add books or other items to their cart while browsing the platform. This allows them to gather items they're interested in purchasing before proceeding to checkout.

####  Remove Books from Cart
Users can remove items from their cart if they no longer wish to purchase them. This gives users control over the contents of their cart before finalizing their order.

###  Checkout cart

####  Ask for address
-  Users are prompted to select from previously used addresses for shipping.
-  Users have the option to add a new address for shipping if needed.

###  Payment

####  Online using bank/BKash
Users can make payments online using bank transfers or mobile financial services like BKash.

####  Cash on delivery
Users have the option to pay for their orders with cash upon delivery.

###  Automated mail
Once an order is confirmed, the system automatically sends an email notification to the user with details of their order and confirmation.

###  Review books

####  Add rating and comments
Users can provide ratings and comments for books they have purchased or read, allowing them to share their opinions and experiences with other users.

###  Advance search
####  Users can use advanced search using 

-  Price range.
-  Publication date range.
-  Author name.
-  Book name.
-  Book genre.
-  Book language.
-  Publisher name.

### Admin Panel 
####  CRUD books
Admins have the ability to perform CRUD operations (Create, Read, Update, Delete) on book listings, allowing them to manage the inventory of available books.

###  CRUD customer orders
Admins can view, manage, and update customer orders, including order statuses and tracking information.

### CRUD user accounts
Admins have control over user accounts and can perform CRUD operations as needed, such as creating new accounts, updating account details, and deleting accounts if necessary.

###  Internationalization
The platform supports internationalization, allowing users to view content in different languages and formats based on their preferences.



## Dev

### Prerequisites
1. Python
2. Docker 
3. Poetry
3. Node

### Get Started
- Clone
```bash
git clone https://github.com/devyneX/paperbound-pavilion.git
```
- Run db and redis
```bash
make run-dependencies
```
- Update 
```bash
make update
```
- Install frontend dependencies
```bash
npm install
```
- Run this in the terminal 
```bash
npm run tailwind
```
 while you do development to compile TailwindCSS on demand.
- Run server
```bash
make run-server
```

- Run Celery worker
```bash
make run-celery
```

### Get updates 
- Pull
- Run `make update`

### Linting
- Run `make lint`

### Adding Packages
To add python package with poetry
```bash
make add-lib package_name
```

To add dev python package with poetry
```bash
make add-lib-dev package_name
```

### Translations
- Run `make translations`

### Code Guidelines
- Inherit models from `src.core.models.BaseModel`
- Templates to be extend from 
  - `src/core/templates/_base.html`
    - base template without navbar
  - `src/core/templates/base.html`
    - base template with navbar
  - `src/store_admin/templates/admin_base.html`
    - admin base template 
- Templates to include 
  - `src/core/templates/_form.html`
    - prebuilt form 
    - include as `{% include '_form.py' with submit_text="your-custom-submit-text" %}`
  - `src/core/templates/form.html`
    - prebuilt form with form_title
    - include as `{% include 'form.py' with form_title="your-custom-form-title" submit_text="your-custom-submit-text" %}`

### Contributing
- Create a new branch
- Make changes
- Push changes
- Create a PR
