# Mothly report (Angular + Clarity + FastApi)

client:
http://localhost:4200

server:
http://localhost:8000

swagger:
http://localhost:8000/docs

### How to build?

1. Install uv package manager:

`# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh`

2. Build server

`
cd monthly-report

# instal the dependencies
uv sync 

# Run server wathcer
uv run fastapi dev server/main.py
`

3. Build client

`
cd monthly-report/client

npm install

npx ng serve
`

### Server

Mix between ORM and raw sql queries.

model.py - Where you put DTO class definitions.

schema.py - Define ORM classes.

repository.py - Encapsulates database operations into a class, related to an entity
(crud operations).

dependency.py - Define FastApi dependencies to decouple app components. Usually expose
repository, service or variables(e.g. settings) as dependencies.

controller.py - Define all endpoints for a router inside a controller. The controller
avoids duplication e.g. we don't want to have in all endpoint functions e.g. parameter session 
(database session). Controllers are part from the fastapi-utils module.

