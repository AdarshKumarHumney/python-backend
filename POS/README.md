# POS SYSTEM

A command line backend system for managing inventory, user, admin and sale - built with python and SQLite
    
--------

## TECH STACK

-Python - 3.11
- SQLITE (via Python's built in sqlite3 module)
- bycrpt (password hasing)
- python-dotenv(environment variable)

## FEATURES
- Admin and user registration and credential-based login with lockout after three failed attempts
- Add, update search and delete inventory items by id and name
- Allow user to add inventory items to cart
- Register the purchase of User
- Keep track of the sale and print the recipt for the user
- All password are hashed with help of bycrpt
- Parameterised querry throughout

## PROJECT STRUCTURE

POS SYSTEM
 -database.py #connection management and schema creation
 -security.py #bycrpt hashing,login verification
 -inventory-management.py #intermediate between inventory.py and database.py
 -inventory.py #CRUD for inventory
 -admin-management.py #intermediate between admin.py and database.py
 -admin.py #CRUD for admin and talks with inventory.py
 -user-management.py #intermediate between user.py and databse.py
 -user.py #CRUD for user and also the POS happens here
 -main.py #Entry point, CLI
 -.env #Environment variable
 -README.md

##
## Setup

```bash
# Clone the repo
git clone https://github.com/AdarshKumarHumney/POS.git
cd library-system

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and set your MASTER_PASSWORD

# Run
python main.py
```

---

## Key Implementation Notes

**Authentication flow:**
Admin Registration Login/User Registration Login
Admin Registration->login Credentials with bycrpt verification->Inevntory Management/CRUD
User Registration -> Login credentials with bycrpt verification -> CRUD for cart -> Sale ->Recipt

**Database design:**
6 normalized tables (Inventory, user, admins, cart, sale, recipt) with 
foreign key constraints and ON CONFLICT handling for upserts.

**Security:**
- `secrets` module used for salt generation
- `.env` file keeps credentials out of source code
- Parameterized queries prevent SQL injection at every query

---

## What I Learned

- Dependency injection for keeping database connections modular and testable
- How bcrypt salting works at the implementation level, not just conceptually
- Separation of concerns across multiple files vs. one monolithic script
- Fetching rows as dictionaries using sqlite3.Row or row_factory
- Rollback Transaction, stop the process during transaction phase if encountered with any problem and no new write function in the database 
- commitTransaction, commit to database only when eveything works smooth and fine till the final recipt
- Upsert, how to handle adding something new if there is a collsion with primary key and attribute
- ACID compliant checkout function
---

## Roadmap

- [ ] Add pytest test suite for admin and transaction modules
- [ ] Migrate to PostgreSQL + SQLAlchemy
- [ ] Expose as REST API via FastAPI