# 🚀 CI/CD Python Web App (Jenkins → SonarQube → Trivy → Docker → Argo CD)

This repository contains a Python sample web application plus a Jenkins pipeline that:
1) builds and tests the app with Docker,
2) runs **SonarQube** (code quality) and **Trivy** (image vulnerability) scans,
3) pushes the image to **Docker Hub**, and
4) updates a separate **manifests repo** so **Argo CD** can roll out the new version to Kubernetes.

> **GitOps flow:** App repo (this) → build & scan → push image → **commit image tag** to manifests repo → Argo CD syncs to the cluster.

## 🧰 Tech Stack
Python (sample webapp) • Jenkins • Docker • SonarQube • Trivy • Docker Hub • Argo CD • Kubernetes

## 📂 Repo Structure

