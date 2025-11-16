# SonarCloud Python Demo

This is a minimal Python project to demonstrate **SonarCloud** analysis running from **GitHub Actions**.

## What it does
- Runs unit tests with **pytest**
- Generates code coverage with **coverage.py**
- Uploads analysis results to **SonarCloud**

## One-time setup
1. Create a new GitHub repository (e.g., **sonar-demo**).
2. In the repo, go to **Settings → Secrets and variables → Actions → New repository secret** and add:
   - `SONAR_TOKEN` = your token from https://sonarcloud.io (My Account → Security → Generate token)
3. Push this project to your GitHub repo on the `main` branch.

## Files
- `mylib/` — simple library code
- `tests/` — tests for the library
- `sonar-project.properties` — SonarCloud configuration
- `.github/workflows/sonar-analysis.yml` — CI that runs tests + analysis

## SonarCloud configuration in this demo
- Organization: **hemanth**
- Project key: **hemanthkumarg0808-dotcom**

> If your SonarCloud project uses a different organization or key, update them in:
> - `sonar-project.properties`
> - `.github/workflows/sonar-analysis.yml`

## Run locally (optional)
```bash
python -m pip install -r requirements.txt
coverage run -m pytest
coverage xml
```

Then commit and push — the Action will kick off automatically.
