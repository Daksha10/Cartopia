
# Cartopia: A Simple Inventory Management System

Cartopia is a web application built with Flask (backend) and HTML, CSS, JavaScript (frontend) for managing inventory and orders.  This README provides a comprehensive overview of the project.

## Table of Contents

- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Directory Structure](#directory-structure)
- [Technology Stack](#technology-stack)
- [Database Schema](#database-schema)
- [API Endpoints](#api-endpoints)


## Features

- **Product Management:** Add, view, and delete products.  Includes units of measure (UOM).
- **Order Management:** Create new orders, view order details, and see a summary of all orders.
- **User Interface:** Clean and user-friendly interface built with HTML, CSS, and JavaScript.


## Setup and Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Daksha10/Cartopia.git
     ```

2. **Create a Virtual Environment (Recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
     ```

4. **Set up Database:**

   - Create a MySQL database named `Cartopia`.  You'll need to adjust the database credentials in the `.env` file to match your setup.  The `Cartopia` database should contain tables for `Products`, `Orders`, `Order_details`, and `UOM` (units of measure).  Sample table structures are described in the [Database Schema](#database-schema) section below.

5. **Run the Application:**

   ```bash
   python backend/server.py
     ```

   The application will start on port 5000 (or the PORT environment variable if set).  Open your web browser and navigate to `http://localhost:5000` (or the appropriate address).


## Directory Structure

```markdown
cartopia/
├── backend/              # Backend code (Flask)
│   ├── orders_dao.py     # Data Access Object for orders
│   ├── products_dao.py   # Data Access Object for products
│   ├── prd.py            # (Example) Simple product data retrieval
│   ├── server.py         # Main Flask server
│   └── sql_connection.py # Function to establish database connection
├── ui/                  # Frontend code (HTML, CSS, JS)
│   ├── index.html        # Main dashboard page
│   ├── manage-product.html # Product management page
│   ├── order.html        # Order creation page
│   └── static/           # Static assets (CSS, JS, images)
│       └── css/
│       └── js/
│       └── images/
├── .env                  # Environment variables (DB credentials)
├── requirements.txt      # Project dependencies
└── vercel.json           # Configuration for Vercel deployment
```

## Technology Stack

- **Backend:** Python, Flask, MySQL, mysql-connector-python, python-dotenv
- **Frontend:** HTML, CSS, JavaScript, jQuery, Bootstrap, Flask-Bootstrap, Flask-CORS


## Database Schema

(Note:  This is a simplified schema. Adapt as needed.)

**Products Table:**

| Column Name     | Data Type    | Constraints    |
|-----------------|---------------|-----------------|
| product_id      | INT           | PRIMARY KEY, AUTO_INCREMENT |
| name            | VARCHAR(255) | NOT NULL        |
| uom_id          | INT           | NOT NULL, FOREIGN KEY (UOM) |
| price_per_unit  | DECIMAL(10, 2)| NOT NULL        |

**Orders Table:**

| Column Name    | Data Type    | Constraints    |
|----------------|---------------|-----------------|
| order_id       | INT           | PRIMARY KEY, AUTO_INCREMENT |
| customer_name  | VARCHAR(255) | NOT NULL        |
| total          | DECIMAL(10, 2)| NOT NULL        |
| datetime       | TIMESTAMP     | DEFAULT CURRENT_TIMESTAMP |

**Order_details Table:**

| Column Name    | Data Type    | Constraints               |
|----------------|---------------|---------------------------|
| order_id       | INT           | FOREIGN KEY (Orders)       |
| product_id     | INT           | FOREIGN KEY (Products)     |
| quantity       | INT           | NOT NULL                   |
| total_price    | DECIMAL(10, 2)| NOT NULL                   |

**UOM (Units of Measure) Table:**

| Column Name | Data Type    | Constraints    |
|-------------|---------------|-----------------|
| uom_id      | INT           | PRIMARY KEY, AUTO_INCREMENT |
| uom_name    | VARCHAR(255) | NOT NULL        |


## API Endpoints

- `/getProducts`:  GET request to retrieve all products.
- `/getUOM`: GET request to retrieve all units of measure (UOM).
- `/insertProduct`: POST request to add a new product.  Requires JSON payload with `product_name`, `uom_id`, and `price_per_unit`.
- `/getAllOrders`: GET request to retrieve all orders with details.
- `/insertOrder`: POST request to add a new order. Requires JSON payload with `customer_name`, `grand_total`, and an array of `order_details` (each with `product_id`, `quantity`, and `total_price`).
- `/deleteProduct`: POST request to delete a product. Requires `product_id` in the request body.
