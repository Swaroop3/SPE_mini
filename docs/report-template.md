# Scientific Calculator Mini-Project Report Template

> Replace bracketed text with project-specific details and include annotated screenshots for each DevOps step.

## 1. Introduction
- Project title and author (Roll Number)
- Brief objective of the scientific calculator and summary of delivered features

## 2. What and Why of DevOps
- Concise explanation of DevOps principles used in this project
- Benefits achieved (speed, reliability, reproducibility)

## 3. Toolchain Overview
| Step | Tool(s) | Purpose |
|------|---------|---------|
| Source Control | Git / GitHub | Version history and collaboration |
| Testing | Pytest | Automated unit coverage |
| Build | `python -m build` | Produce distributable wheel/sdist |
| Continuous Integration | Jenkins | Automate pipeline stages |
| Containerization | Docker | Package API + CLI |
| Registry | Docker Hub | Store deployable image |
| Configuration & Deployment | Ansible | Orchestrate container rollout |

## 4. Implementation Details
### 4.1 Source Control Management
- Repository URL: `[https://github.com/Swaroop3/SPE_mini]`
- Key branches, commit naming, and screenshots of commits/pull requests

### 4.2 Testing
- Command: ``pytest``
- Evidence of test runs (terminal output / Jenkins JUnit report screenshot)
- Coverage highlights or gaps

### 4.3 Build
- Command: ``python -m build``
- Artifacts produced (wheel/sdist) with file names and paths

### 4.4 Continuous Integration (Jenkins)
- Screenshot(s) of job configuration and successful pipeline run
- Jenkinsfile snippet highlighting critical stages

### 4.5 Containerization (Docker)
- Command: ``docker build -t <username>/spe-calculator:<tag> .``
- Runtime command: ``docker run -p 8000:8000 <username>/spe-calculator:<tag>``
- Screenshot showing the API responding (e.g., `/sqrt?value=9`)

### 4.6 Registry (Docker Hub)
- Repository URL and push command
- Screenshot of pushed image tags

### 4.7 Deployment (Ansible)
- Command: ``scripts/deploy_with_ansible.sh --extra-vars "calculator_image=<username>/spe-calculator:<tag>"``
- Inventory used and summary of task output
- Screenshot of running container on target host

## 5. Application Evidence
- CLI transcript demonstrating each calculator operation
- API samples (curl/Postman) for all endpoints with responses

## 6. Challenges & Learnings
- Obstacles faced and solutions
- Improvements or future enhancements

## 7. References
- External resources, documentation, or tutorials consulted

## 8. Appendix
- Links to GitHub repository, Jenkins pipeline, Docker Hub image, and Ansible playbooks
- Embed additional screenshots if necessary
