# plotly-figure-tester

This library contains a Python structure that acts as a wrapper for testing Plotly figure configurations. It's built using Plotly Express, Plotly Graph Objects and Dash.

# Setup

All steps listed below are accotrding to Windows using PowerShell. Adapt the commands to your OS and please contribute to the repository with your changes.

1. Create and active a Virtual Environment
```powershell
python -m venv .venv
.venv\Scripts\activate
```

2. Install Poetry package manager and install it
```powershell
pip install poetry
poetry install
```

# Running the service

To start the service...
> TBD

# Running via Docker

Install Docker and un the following command to build the docker image:

1. Build the docker image:
```powershell

```

2. Start the docker container:
```powershell

```

3. To tail the logs:
```powershell
docker logs -f plotly_figure_tester
```

# Development Workflow

### Adding new dependencies

To add a new dependency, use the `poetry add` command:
```powershell
poetry add <package-name>
```

This will update the `pyproject.toml` and `poetry.lock` files automatically. Do not change them manually.

### Removing dependencies

To remove a dependency, use:
```powershell
poetry remove <package-name>
```

### Exporting requirements

If you need a requirements.txt file (e.g., for compatibility with other tools), you can generate one by:

```powershell
poetry export -f requirements.txt --output requirements.txt
```

# Mantainers

- [Rodrigo Vanzelotti](https://www.linkedin.com/in/rodrigovanzelotti/?locale=en_US)
