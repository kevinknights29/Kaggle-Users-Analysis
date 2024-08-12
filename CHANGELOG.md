## 0.1.3 (2024-08-12)

### Fix

- added git pull to format job and merged commit and push steps
- added continue on error to format job for pre-commit to apply changes
- updated version job trigger
- added commit changes to format job

## 0.1.2 (2024-08-12)

### Fix

- removed check argument from mypy job

## 0.1.1 (2024-08-12)

### Fix

- updated ruff job due typo
- updated tests directories

## 0.1.0 (2024-08-12)

### Feat

- added github actions ci pipeline
- added devcontainer for frontend
- added devcontainer for backend
- added pre-commit config and pyproject.toml

### Fix

- added .venv to PATH for each job with python dependencies installation
- added matrix for multiple jobs execution
- updated python versions to 3.12 to avoid erros in ci pipeline

### Refactor

- added sample requirements.txt
- updated pre-commit hooks
- updated .gitignore with pre-commit hooks
