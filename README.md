# Bestbuy

A small console-based store application written in Python.  
The project is focused on practicing object-oriented programming concepts such as classes, encapsulation and composition.

The application models:

- `Product` – a single product type with price, quantity and active state  
- `Store` – a collection of products that can be queried and ordered from  
- `main` – a simple text-based user interface to interact with the store

---

## Features

- **List all products in the store**  
- **Show total quantity** of all items in stock  
- **Create an order interactively**:
  - select products by number
  - enter desired quantity for each product
  - see the total price for the order
- **Automatic product deactivation** when quantity reaches zero
- **Validation & error handling**:
  - no negative prices or quantities
  - cannot buy more items than are in stock
  - cannot buy inactive products
  - orders only allowed for products that belong to the store

---

## Tech Stack

- Python 3.x (no third-party libraries required)

---
