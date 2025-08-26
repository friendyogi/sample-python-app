# 🚀 GitOps Demo App

A simple Flask-based web app designed to demonstrate GitOps workflows using:

- 🐳 Docker
- 🖼️ Amazon ECR
- ☸️ Kubernetes on EKS
- 📁 GitHub for manifest storage
- 🧪 Versioned app content via `APP_VERSION`

---

## 🌐 App Features

- Serves a clean HTML page on `/`
- Shows current app version using `APP_VERSION` environment variable
- Content updates clearly reflect version changes for visual GitOps demos

---

## 🛠️ Tech Stack

- Python 3.11 + Flask
- Docker (multi-arch builds supported)
- Amazon ECR (container registry)
- EKS (Kubernetes deployment target)
- GitHub (YAML manifests)

---

## 📁 File Structure
```
.
├── main.py          # Flask app
├── Dockerfile       # Docker build definition
├── deployment.yaml  # Kubernetes Deployment (in GitOps repo)
└── service.yaml     # Kubernetes ClusterIP Service (in GitOps repo)
```

---

## 🧪 Local Test

### Run Locally

```bash
export APP_VERSION=<git-commit-id>
python3 main.py
```

Visit http://localhost:80

---

## Build locally for testing
```
docker build -t gitops-demo:v1 .
```

## Build & Push for ECR (example)
```
# Login
aws ecr get-login-password | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com

# Tag & Push
docker tag gitops-demo:v1 <account-id>.dkr.ecr.<region>.amazonaws.com/gitops-yogesh-operator:<git-commit-id>
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/gitops-yogesh-operator:<git-commit-id>
```

---

## ☸️ Deploy to Kubernetes (EKS)
```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

---

## 📦 Access the App (ClusterIP)

Use an internal curl pod or kubectl exec to access:
```
kubectl run curlpod -n gitops-yogesh --rm -it --image=alpine -- sh
# Then inside pod:
apk add curl
curl http://gitops-demo-service
```
---

## 🔁 Update Workflow (New Version)
	1.	Change APP_VERSION in main.py
	2.	Rebuild and push Docker image with new tag (v2, etc.)
	3.	Update deployment.yaml to use new image tag
	4.	Commit + push YAML to GitHub
	5.	Reapply YAML or let GitOps tool (like ArgoCD) sync

