# Demo CI/CD Pipeline (Jenkins + Docker + Docker Compose)

This repository contains a minimal demo application and a Declarative Jenkins pipeline that:

- Builds a small web app (FastAPI "Hello World")
- Runs unit tests
- Builds a Docker image
- Deploys the app using `docker-compose`
- Performs a health check against `/health`

Files of interest:

- `Jenkinsfile` — Declarative Jenkins pipeline (checkout, build, test, package, deploy, health-check)
- `docker-compose.yml` — Spins up Docker-in-Docker plus Jenkins (root compose) and the app service (app/docker-compose.yml used by pipeline)
- `app/Dockerfile` — Builds the app image
- `app/main.py` — FastAPI demo app
- `app/test.py` — Unit tests (unittest)
- `healthcheck.sh` — Health check script used by the pipeline

Quick local run (manual testing):

1. Start the application locally with docker-compose (this will bring up the `app` service defined at repository root compose):

```bash
docker-compose up -d
```

2. Build the image and start the `app` service only (alternate):

```bash
docker build -t demo-app:local .
docker-compose up -d --build app
```

3. Check health manually:

```bash
./healthcheck.sh
```

Running Jenkins locally (bonus - Docker-in-Docker):

- The provided root `docker-compose.yml` is pre-configured to start a `docker` (dind) service and a `jenkins` service that can communicate with it via TCP. Start them with:

```bash
docker-compose up -d
# then open http://localhost:8080 and create a Pipeline job using the Jenkinsfile in this repo
```

Sample (simulated) pipeline console output snippet:

```
[Pipeline] Start of Pipeline
[Pipeline] stage (Checkout)
Checking out
[Pipeline] stage (Build)
Running syntax check...
Success: compiled app/main.py
[Pipeline] stage (Test)
Ran 2 tests in 0.01s
OK
[Pipeline] stage (Package (Docker))
Successfully built image: demo-app:42
[Pipeline] stage (Deploy)
Creating app_1 ... done
[Pipeline] stage (Health Check)
Health check OK (attempt 1)
[Pipeline] End of Pipeline
```

Notes & assumptions:

- Jenkins needs permission to access the Docker daemon. The root `docker-compose.yml` configures the classic DinD pattern for local demo use only.
- For production CI you'd prefer a coordinate Docker agent or a dedicated build host rather than DinD.

If you'd like, I can:

- Start the docker-compose stack here (if you want me to attempt to run it in this environment).
- Generate a sample Jenkins job XML or a `jenkins` container seed configuration to auto-create the pipeline job.
- Produce a small screenshot: I cannot create an actual screenshot in this environment, but I can give precise steps and a sample log to paste into your CI run.
