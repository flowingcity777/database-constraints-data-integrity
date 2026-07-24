# Database Constraints & Data Integrity

## Codecademy SQL Project

## Overview

**Database Constraints & Data Integrity** is a SQL project focused on improving the reliability, consistency, and integrity of an existing database by applying industry-standard database constraints.

The project demonstrates how to clean existing data, enforce validation rules, strengthen table relationships, and maintain referential integrity using SQL Data Definition Language (DDL) statements.

Throughout the project, existing tables are updated by adding constraints such as **NOT NULL**, **UNIQUE**, **CHECK**, **PRIMARY KEY**, and **FOREIGN KEY** while preserving valid data.

---

## Features

* Improved existing database structure
* Cleaned incomplete data before applying constraints
* Added NOT NULL constraints
* Enforced UNIQUE values
* Created CHECK constraints for data validation
* Added PRIMARY KEY and FOREIGN KEY constraints
* Strengthened referential integrity
* Updated existing records while maintaining data consistency

---

## SQL Concepts Practiced

* ALTER TABLE
* UPDATE
* INSERT INTO
* NOT NULL
* UNIQUE
* CHECK
* PRIMARY KEY
* FOREIGN KEY
* Data Validation
* Data Cleaning
* Referential Integrity

---

## Project Workflow

The project follows a realistic database migration process:

1. Inspect existing data
2. Clean missing or inconsistent values
3. Apply integrity constraints
4. Create relationships between tables
5. Validate data consistency
6. Update existing records

This workflow reflects common practices used when improving production databases.

---

## Database Improvements

The project enhances multiple tables by:

### Parts Table

* Enforcing unique part codes
* Preventing NULL descriptions
* Adding a primary key
* Creating relationships with manufacturers

### Reorder Options

* Preventing invalid prices and quantities
* Applying business rules with CHECK constraints
* Linking reorder options to parts using foreign keys

### Locations

* Preventing duplicate storage locations
* Validating inventory quantities
* Strengthening table relationships

### Manufacturers

* Maintaining referential integrity
* Updating manufacturer relationships
* Ensuring valid manufacturer references

---

## Technologies Used

* SQL
* PostgreSQL
* Relational Databases

---

## Project Structure

```text
database-constraints-data-integrity
│
├── database_constraints.sql
└── README.md
```

---

## What I Learned

Through this project, I gained hands-on experience with:

* Improving existing database schemas
* Applying database constraints safely
* Cleaning data before enforcing validation rules
* Protecting data quality using SQL constraints
* Maintaining referential integrity
* Following a structured database migration workflow

---

## Future Improvements

Potential future enhancements include:

* Named database constraints
* Transaction management
* Trigger-based validation
* Stored procedures
* Automated data auditing
* Additional integrity checks

---

## Acknowledgements

This project was completed as part of the **Codecademy SQL** curriculum and focuses on applying database constraints and integrity rules using SQL.
