# AI ChatOps Incident Assistant

AI-powered ChatOps platform designed to assist DevOps teams in investigating incidents by analyzing system logs and providing automated insights.

## Project Goal
Simulate a production-grade DevOps system integrating AI, cloud infrastructure, and observability tools.

## Tech Stack
- FastAPI (Python)
- Docker (coming next)
- AWS (planned)
- Kubernetes (planned)
- Terraform (planned)

## Local Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

## Project Structure

app/
 ├── api/        # API routes
 ├── core/       # Main FastAPI setup
 ├── services/   # Business logic and AI integration
 ├── models/     # Pydantic models / ML input-output
 └── utils/      # Helper functions
infra/           # Terraform / infrastructure code
k8s/             # Kubernetes manifests
helm/            # Helm charts
docs/            # Project documentation
