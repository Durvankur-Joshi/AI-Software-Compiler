# AI Software Compiler

An AI-powered multi-stage software generation system that transforms natural language prompts into structured, validated, executable application blueprints.

This project was built for the AI Platform Engineer (Founding Intern) demo task.

---

# Objective

Convert:

Natural Language → Structured Config → Validation → Repair → Runtime Execution

The system behaves like a compiler pipeline for software generation.

---

# Features

- Multi-stage generation pipeline
- Intent extraction
- Architecture generation
- Database schema generation
- API schema generation
- UI schema generation
- Auth + role generation
- Business logic generation
- Validation engine
- JSON repair engine
- Targeted regeneration
- Retry handling
- Clarification system
- SQLite runtime execution
- FastAPI backend generation
- Downloadable generated backend
- Evaluation framework with metrics

---

# System Architecture

```text
User Prompt
     │
     ▼
Compiler Agent
(Intent + Architecture + Schemas)
     │
     ▼
JSON Repair Layer
(Fixes invalid JSON)
     │
     ▼
Schema Validator
(Checks consistency)
     │
     ▼
Repair Engine
(Fixes hallucinated/missing fields)
     │
     ▼
Regeneration Engine
(Regenerates only failing layers)
     │
     ▼
SQLite Runtime
(Creates executable DB)
     │
     ▼
Backend Generator
(Generates FastAPI backend)
     │
     ▼
ZIP Export System
(Downloadable backend project)
```

---

# Pipeline Stages

## 1. Intent Extraction
Extracts:
- app type
- features
- user roles
- permissions

---

## 2. Architecture Design
Generates:
- entities
- modules
- pages
- roles

---

## 3. Schema Generation
Creates:
- database schema
- API schema
- UI schema
- auth schema
- business logic rules

---

## 4. Validation Layer
Checks:
- valid JSON
- required fields
- API ↔ DB consistency
- UI ↔ API consistency
- auth correctness

---

## 5. Repair + Regeneration
Handles:
- hallucinated fields
- missing keys
- invalid JSON
- schema mismatches

Uses:
- targeted regeneration
- automatic repair

instead of blind retries.

---

# Runtime Execution

The system generates executable FastAPI backend projects including:
- routes
- models
- database
- runtime app

Generated projects can be downloaded as ZIP files.

---

# Evaluation Framework

The system includes:
- 10 real-world prompts
- 10 edge-case prompts

Metrics tracked:
- success rate
- failures
- latency
- repair frequency
- clarification frequency

---

# Tech Stack

## Backend
- FastAPI
- Python
- SQLite
- Supabase

## AI
- Gemini API

## Frontend
- React
- TailwindCSS

---

# Project Structure

```text
app/
│
├── pipeline/
│   ├── compiler_agent.py
│   ├── validator.py
│   ├── repair_engine.py
│   ├── regeneration_engine.py
│   ├── retry_handler.py
│   └── clarification_engine.py
│
├── runtime/
│   └── sqlite_runtime.py
│
├── generators/
│   └── backend_generator.py
│
├── exporters/
│   └── project_exporter.py
│
├── evaluation/
│   ├── test_dataset.py
│   └── evaluator.py
│
└── monitoring/
    └── metrics.py
```

---

# Running The Project

## Backend

```bash
uvicorn app.main:app --reload
```

---

## Frontend

```bash
npm install
npm run dev
```

---

# Evaluation Runner

```bash
python -m app.evaluation.evaluator
```

---

# Key Engineering Decisions

## Why Multi-Stage Pipeline?
Improves:
- reliability
- modularity
- controllability

---

## Why Repair Instead of Full Retry?
Targeted repair reduces:
- latency
- token cost
- instability

---

## Why Runtime Execution?
Ensures generated outputs are executable and not just theoretical JSON.

---

# Future Improvements

- Full frontend code generation
- Dockerized runtime
- Multi-language backend generation
- Live deployment pipeline
- Visual workflow editor

---

# Author

Built by Durvankur Joshi