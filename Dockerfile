# ===== Stage 1: Build =====
FROM python:3.11-slim AS builder

WORKDIR /app

# Install dependencies
COPY webapp/requirements.txt .
RUN pip install --upgrade pip && pip install --target=/app/python_deps -r requirements.txt

# Copy source code
COPY webapp/ .

# ===== Stage 2: Run (Distroless) =====
FROM gcr.io/distroless/python3-debian11

WORKDIR /app

COPY --from=builder /app /app

# Set environment to find our dependencies
ENV PYTHONPATH=/app/python_deps

# Expose port
EXPOSE 5000

# Run app
CMD ["app.py"]


