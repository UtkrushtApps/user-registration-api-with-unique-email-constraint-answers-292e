# Solution Steps

1. 1. Set up the FastAPI app structure with 'app' directory and files for main, models, schemas, and db config.

2. 2. In app/db.py, configure the async SQLAlchemy engine and session using environment variables and dotenv.

3. 3. In app/models.py, define the User model with unique constraint on email and fields for id, email, and name.

4. 4. In app/schemas.py, define the Pydantic schemas: UserCreate (input) and UserRead (output), enforcing email format with EmailStr.

5. 5. In app/main.py, initialize FastAPI, create a DB dependency, and add a startup event to create tables at launch.

6. 6. Implement the /users/ POST endpoint: check for existing email via the API, add DB-level unique constraint, handle errors and rollback.

7. 7. Implement the /users/ GET endpoint to list all registered users.

8. 8. Write requirements.txt with FastAPI, uvicorn, SQLAlchemy (async), asyncpg, etc.

9. 9. Write a Dockerfile that installs dependencies, copies code, and runs the app with uvicorn.

10. 10. Write docker-compose.yml to launch both the API and a Postgres database, configure environment variables, and set network/ports.

11. 11. Test the endpoints: POST /users/ (should block duplicate emails with proper error) and GET /users/ (should list users).

