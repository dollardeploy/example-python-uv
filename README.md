# Python FastHTML Web App Boilerplate

A lightweight Python web application template using FastHTML with the following key features:

## Key Features

- HTTP server for dynamic HTML components
- Default port 8000
- uv package manager for fast dependency management
- Hot reloading support

## Prerequisites

- Python 3.13+
- uv package manager

## Quick Start

### Clone Repository
```bash
git clone https://github.com/dollardeploy/example-python-uv/
cd example-python-uv
```

### Build
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
```

### Run
```bash
# Development mode
uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## DollarDeploy Configuration

To deploy this application with DollarDeploy, use the following settings:

- **Type**: `native`
- **Build => Build Command**: `uv sync`
- **Deploy => Custom Start Command**: `uv run uvicorn main:app --host 0.0.0.0 --port $PORT`
- **Deploy => Custom pre start shell command**: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- **Main port**: `8000`

## Project Structure

- `main.py` - Main application file with FastHTML routes
- `pyproject.toml` - Project configuration and dependencies
- `uv.lock` - Locked dependency versions

## About

Boilerplate for a Python FastHTML webapp which is easy to deploy to any cloud provider with DollarDeploy.
