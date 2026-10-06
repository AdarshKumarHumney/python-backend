# POS SYSTEM

A command line backend system for managing inventory, user, admin and sale - built with python and SQLite
    
--------

## TECH STACK

-Python - 3.11
- SQLITE (via Python's built in sqlite3 module)
- bcrypt (password hashing)
- python-dotenv(environment variable)

## FEATURES
- Admin and user registration and credential-based login with lockout after three failed attempts
- Add, update search and delete inventory items by id and name
- Allow user to add inventory items to cart
- Register the purchase of User
- Keep track of the sale and print the receipt for the user
- All password are hashed with help of bcrypt
- Parameterized  query throughout

## PROJECT STRUCTURE

## Project Structure

```
pos-system/
├── database.py              # Connection management, schema creation
├── security.py              # bcrypt hashing, login verification
├── inventory_management.py  # Intermediate between inventory.py and database.py
├── inventory.py             # CRUD for inventory
├── admin_management.py      # Intermediate between admin.py and database.py
├── admin.py                 # CRUD for admin, talks with inventory.py
├── user_management.py       # Intermediate between user.py and database.py
├── user.py                  # CRUD for user, POS logic happens here
├── main.py                  # Entry point, CLI menu
├── .env                     # Environment variables (not committed to git)
└── README.md
```

## Setup

```bash
# Clone the repo
git clone https://github.com/AdarshKumarHumney/POS.git
cd POS

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

**Admin path:** Master password gate → Admin registration → 
Credential-based login with bcrypt verification → Inventory management / CRUD

**User path:** User registration → Credential-based login with 
bcrypt verification → Cart management → Checkout → Receipt generation


**Database design:**
6 normalized tables (Inventory, user, admins, cart, sale, receipt) with 
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
- Upsert, how to handle adding something new if there is a collision with primary key and attribute
- ACID-compliant transactions — rolling back on any failure so no partial writes reach the database, committing only when the full checkout succeeds
---

## Roadmap

- [ ] Add pytest test suite for admin and transaction modules
- [ ] Migrate to PostgreSQL + SQLAlchemy
- [ ] Expose as REST API via FastAPI

