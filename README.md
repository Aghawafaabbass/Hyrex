# ✦ Hyrex

### Full Stack Job Portal — Django + DRF + PostgreSQL + JWT + React + Docker + CI/CD + Postman

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.x-092E20?style=flat&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-3.17+-red?style=flat&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/Auth-JWT-000000?style=flat&logo=jsonwebtokens&logoColor=white)
![React](https://img.shields.io/badge/Frontend-React-61DAFB?style=flat&logo=react&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat&logo=docker&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-Redis-37814A?style=flat&logo=celery&logoColor=white)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white)
![Postman](https://img.shields.io/badge/API_Testing-Postman-FF6C37?style=flat&logo=postman&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Aghawafaabbass-181717?style=flat&logo=github&logoColor=white)

> A production-grade, full stack job portal that connects **Recruiters** with **Candidates** through a structured, role-driven hiring workflow. Built with Django REST Framework as the backend API, React as the frontend (localhost:3000), JWT for stateless authentication, Celery + Redis for async task processing, PostgreSQL as the production database, Docker for containerisation, GitHub Actions for CI/CD, and Postman for API testing and documentation.

---

## 🚀 Live Demo

👉 **Coming Soon — Deployment in progress**

---

## 📸 Screenshots

### Login Page
![Login](https://raw.githubusercontent.com/Aghawafaabbass/Hyrex/main/screenshots/01_Login_Page.PNG)

### Register — Create Account (Candidate / Recruiter)
![Register](https://raw.githubusercontent.com/Aghawafaabbass/Hyrex/main/screenshots/02_register.PNG)

### Recruiter Dashboard — My Job Postings
![Recruiter Dashboard](https://raw.githubusercontent.com/Aghawafaabbass/Hyrex/main/screenshots/03_Recruiter_Dashboard.PNG)

### Recruiter — Browse Jobs
![Recruiter Browse Jobs](https://raw.githubusercontent.com/Aghawafaabbass/Hyrex/main/screenshots/04_Recruiter_Browse_Jobs.PNG)

### Candidate Login
![Candidate Login](https://raw.githubusercontent.com/Aghawafaabbass/Hyrex/main/screenshots/05_Candidate_Login.PNG)

### Candidate Dashboard — My Applications
![Candidate Applications](https://raw.githubusercontent.com/Aghawafaabbass/Hyrex/main/screenshots/06_Candidate_My_Applications.PNG)

### Candidate — Browse Jobs
![Candidate Browse Jobs](https://raw.githubusercontent.com/Aghawafaabbass/Hyrex/main/screenshots/07_Candidate_Browse_Jobs.PNG)

### Candidate — Applied Successfully
![Applied Now](https://raw.githubusercontent.com/Aghawafaabbass/Hyrex/main/screenshots/08_Candidate_jobs_Applied_Now.PNG)

### Django Administration Panel
![Admin Panel](https://raw.githubusercontent.com/Aghawafaabbass/Hyrex/main/screenshots/09_Django_Administration.PNG)

---

## 👨‍💻 Developer

**Agha Wafa Abbas**
**Full Stack Developer | Lecturer, School of Computing**

| Institution | Location | Email |
|---|---|---|
| University of Portsmouth | Winston Churchill Ave, Southsea, Portsmouth PO1 2UP, UK | agha.wafa@port.ac.uk |
| Arden University | Coventry, United Kingdom | awabbas@arden.ac.uk |
| Pearson | London, United Kingdom | — |
| IVY College of Management Sciences | Lahore, Pakistan | wafa.abbas.lhr@rootsivy.edu.pk |

---

## 🎯 Purpose & Real-World Use Cases

Hyrex is a **production-ready job portal platform** that solves the core hiring problem: reliably moving a job posting from creation through candidate discovery, application, and review — with full role-based control and async task processing.

**Where Hyrex can be used:**

| Sector | Use Case |
|---|---|
| **Recruitment Agencies** | White-label job board for managing client hiring campaigns |
| **Corporate HR Departments** | Internal job posting and applicant tracking system |
| **University Career Portals** | Graduate job boards with role-specific Candidate/Recruiter access |
| **Tech Startups** | Ready-to-deploy MVP hiring platform |
| **Staffing Platforms** | Multi-recruiter, multi-candidate job marketplace |
| **Government & Public Sector** | Transparent vacancy management with audit trail via Django Admin |
| **Remote Work Platforms** | Location-based job matching with search and salary filters |
| **University Teaching** | Real-world Django REST Framework + React + Docker reference project |

---

## 👥 User Roles

| Role | Portal | Core Workflow |
|---|---|---|
| **Admin** | Django Admin — `127.0.0.1:8000/admin/` | Manage all users, jobs, categories, applications; monitor Celery task and group results |
| **Recruiter** | React Frontend — `localhost:3000` | Register with Recruiter role, post jobs, view own listings with ACTIVE status, browse all jobs |
| **Candidate** | React Frontend — `localhost:3000` | Register with Candidate role, browse published jobs, apply with one click, track applications in dashboard |

---

## ✨ Features

- 🔐 JWT-based authentication — stateless, secure, access + refresh token flow
- 📝 Role selection at registration — Candidate or Recruiter chosen at sign-up with phone and location
- 👤 Role-scoped dashboards — Recruiter sees "My Job Postings"; Candidate sees "My Applications"
- 📋 Job listings — title, company, location, salary range, job type (FULL_TIME etc.), experience level (SENIOR etc.)
- 🔍 Real-time job search — search bar across all published listings
- 📩 One-click apply — Candidate hits "Apply Now →" and gets instant "Applied successfully!" confirmation
- 📊 Recruiter job management — own jobs displayed with ACTIVE status badge
- ⚙️ Django Admin — fully configured with Applications, Jobs, Categories, Users sections
- 🌿 Celery Results in Admin — Group results and Task results tracked and visible in admin panel
- 🐳 Docker Compose — single command spins up Django + PostgreSQL + Redis + Celery worker
- 🔄 CI/CD — GitHub Actions pipeline: lint → test → build on every push
- 🧪 API Testing — all endpoints tested and documented with Postman
- 🌑 Dark UI — professional dark-themed React frontend

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.10+ / Django 6.x |
| REST API | Django REST Framework 3.17+ |
| Authentication | JWT — `djangorestframework-simplejwt` |
| Database | PostgreSQL 15 (dev: SQLite) |
| Task Queue | Celery 5.x |
| Message Broker | Redis 7 |
| Frontend | React (localhost:3000) |
| Containerisation | Docker + Docker Compose |
| CI/CD | GitHub Actions |
| API Testing | Postman |
| Config Management | `python-decouple` + `.env` |
| Version Control | Git + GitHub |

---

## 🧪 API Testing — Postman

All REST API endpoints are tested and documented using **Postman**.

Postman was used to:
- Test JWT login and verify the access + refresh token response
- Confirm role-based access control — Recruiter endpoints reject Candidate tokens and vice versa
- Test job creation (POST), listing (GET with search), and individual job detail (GET)
- Test application submission by Candidate and verify "Applied successfully" response
- Confirm Django Admin-protected routes return 403 for non-superusers
- Validate Celery task dispatch and result storage

> To run the collection: import `Hyrex.postman_collection.json` from the `docs/` folder into Postman, set the environment variable `base_url = http://127.0.0.1:8000`, and run the Login request first so the JWT token is auto-populated across all subsequent requests.

---

## 🗄️ Figure 1 — Entity Relationship Diagram (ERD)

```
┌──────────────────────┐        ┌──────────────────┐
│         USER         │        │    CATEGORY       │
│──────────────────────│        │──────────────────│
│ id (PK)              │        │ id (PK)          │
│ username             │        │ name             │
│ email                │        │ slug             │
│ password             │        └────────┬─────────┘
│ role                 │                 │ 1
│  (candidate /        │                 │ N
│   recruiter)         │        ┌────────▼──────────────────────────┐
│ phone                │        │               JOB                  │
│ location             │        │───────────────────────────────────│
└──────┬───────────────┘        │ id (PK)                           │
       │                        │ recruiter_id (FK → User)          │
       │ 1 (recruiter)          │ title                             │
       │────────────────────────│ company                           │
       │ N                      │ location                          │
       │                        │ description                       │
       │                        │ category_id (FK)                  │
       │                        │ job_type                          │
       │                        │  (FULL_TIME / PART_TIME /         │
       │                        │   CONTRACT / REMOTE)              │
       │                        │ experience                        │
       │                        │  (JUNIOR / MID / SENIOR)          │
       │                        │ salary_min / salary_max           │
       │                        │ status (ACTIVE / CLOSED)          │
       │                        │ created_at                        │
       │                        └────────────────┬──────────────────┘
       │                                         │ 1
       │                                         │ N
       │ 1 (candidate)           ┌───────────────▼──────────────┐
       │─────────────────────────│         APPLICATION           │
       │ N                       │──────────────────────────────│
                                 │ id (PK)                      │
                                 │ job_id (FK → Job)            │
                                 │ candidate_id (FK → User)     │
                                 │ applied_at                   │
                                 └──────────────────────────────┘
```

---

## 🔄 Figure 2 — Request Sequence Diagram

```
React (localhost:3000)    URL Router    JWT Middleware     DRF View      DB / Celery
         │                    │               │                │               │
         │─POST /api/token/────────────────────►              │               │
         │  {username, password}              │─verify creds──►               │
         │                                   │               │──User.get()────►
         │                                   │               │◄──user─────────│
         │◄──{access_token, refresh_token}─────────────────────│               │
         │                                                    │               │
         │─GET /api/jobs/?search=django────────────────────────►              │
         │  Authorization: Bearer <token>     │─validate token►               │
         │                                   │               │──Job.filter()──►
         │                                   │               │◄──queryset─────│
         │◄──200 JSON [job listings]───────────────────────────│               │
         │                                                    │               │
         │─POST /api/jobs/<id>/apply/──────────────────────────►              │
         │  Authorization: Bearer <token>     │─validate token►               │
         │                                   │─check role────►               │
         │                                   │  (candidate   │               │
         │                                   │   only)       │               │
         │                                   │               │─Application────►
         │                                   │               │  .create()     │
         │                                   │               │─celery.delay()─►──async task──►
         │◄──201 "Applied successfully!"───────────────────────│               │
         │                                                    │               │
         │─GET /api/applications/──────────────────────────────►              │
         │  Authorization: Bearer <token>     │─validate token►               │
         │                                   │─check role────►               │
         │                                   │  (candidate)  │               │
         │                                   │               │─Application────►
         │                                   │               │  .filter()     │
         │◄──200 JSON [my applications]────────────────────────│               │
```

---

## 🏗️ Figure 3 — System Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│                         DEVELOPMENT                                   │
│                                                                       │
│   React Frontend           Django Backend          Data Layer         │
│   localhost:3000     ───►  127.0.0.1:8000   ───►  PostgreSQL :5432   │
│   (Candidate /             (DRF + JWT)             SQLite (fallback)  │
│    Recruiter UI)                │                                     │
│                                 │                  Redis :6379        │
│   Postman            ───►  /api/* endpoints              │            │
│   (API Testing)            /admin/                       │            │
│                                 │               ┌────────▼──────────┐ │
│                                 └──────────────►│  Celery Worker    │ │
│                                                 │  (async tasks,    │ │
│                                                 │   task results    │ │
│                                                 │   visible in      │ │
│                                                 │   Django Admin)   │ │
│                                                 └───────────────────┘ │
└──────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│                    DOCKER COMPOSE SERVICES                            │
│                                                                       │
│  ┌────────────┐  ┌────────────┐  ┌──────────────┐  ┌─────────────┐  │
│  │     db     │  │   redis    │  │     web      │  │   celery    │  │
│  │ postgres15 │  │  redis:7   │  │  Django +    │  │  worker     │  │
│  │  :5432     │  │  -alpine   │  │  Gunicorn    │  │  depends:   │  │
│  └────────────┘  │  :6379     │  │  :8000       │  │  db, redis  │  │
│                  └────────────┘  │  depends:    │  └─────────────┘  │
│                                  │  db, redis   │                    │
│                                  └──────────────┘                    │
└──────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│                    CI/CD — GITHUB ACTIONS                             │
│   Git Push ──► Checkout ──► Install ──► Lint ──► Test ──► Build      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 📊 Figure 4 — Application State Machine

```
                   Candidate clicks
                   "Apply Now →"
                         │
                         ▼
                 ┌────────────────┐
                 │    APPLIED     │◄── "Applied successfully!" browser confirmation
                 └───────┬────────┘     shown; application appears in
                         │              Candidate's "My Applications" dashboard
                         │
                 Visible in Django Admin
                 under Applications panel
                 (Admin can Add / Change)
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
       (future states)       (future states)
       Shortlisted            Rejected

Job Types:    FULL_TIME · PART_TIME · CONTRACT · REMOTE
Experience:   JUNIOR · MID · SENIOR
Job Status:   ACTIVE · CLOSED
```

---

## 🔁 Figure 5 — Job Posting Lifecycle (Recruiter)

```
Recruiter registers / logs in
           │
           ▼
  Dashboard → "My Job Postings"
           │
           │  Post new job via API / Admin
           ▼
   ┌──────────────┐   Goes live    ┌────────────────────────────────┐
   │  (created)   │───────────────►│           ACTIVE               │
   └──────────────┘                │  Visible on Browse Jobs page   │
                                   │  Card shows:                   │
                                   │  · Title (Senior Django Dev)   │
                                   │  · Company (TechCorp Canada)   │
                                   │  · Location (Toronto, Ontario) │
                                   │  · Salary ($90k - $130k)       │
                                   │  · Type badge: FULL_TIME       │
                                   │  · Level badge: SENIOR         │
                                   │  · "Apply Now →" button        │
                                   └──────────────┬─────────────────┘
                                                  │ Recruiter closes
                                                  ▼
                                          ┌───────────────┐
                                          │    CLOSED     │
                                          └───────────────┘
```

---

## ⚡ Figure 6 — REST API Endpoints

```
# AUTH (JWT)
POST   /api/token/                     ──► Login → {access, refresh} tokens
POST   /api/token/refresh/             ──► Refresh access token
POST   /api/register/                  ──► Register {username, email, password,
                                             role: candidate|recruiter, phone, location}

# JOBS
GET    /api/jobs/                      ──► List all ACTIVE jobs (search supported)
POST   /api/jobs/                      ──► Create job (recruiter only)
GET    /api/jobs/<id>/                 ──► Job detail
PATCH  /api/jobs/<id>/                 ──► Update own job (recruiter only)
DELETE /api/jobs/<id>/                 ──► Delete job (recruiter only)

# APPLICATIONS
POST   /api/jobs/<id>/apply/           ──► Apply to job (candidate only)
                                             → triggers Celery async task
                                             → returns "Applied successfully!"
GET    /api/applications/              ──► My applications list (candidate only)

# DJANGO ADMIN  (127.0.0.1:8000/admin/)
Applications  ──► Add / Change
Jobs          ──► Jobs (Add / Change)
              ──► Categorys (Add / Change)
Users         ──► Add / Change
Celery Results──► Group results (Add / Change)
              ──► Task results (Add / Change)

# POSTMAN TESTING
All endpoints above covered in: docs/Hyrex.postman_collection.json
Environment variable: base_url = http://127.0.0.1:8000
```

---

## ⚙️ Figure 7 — CI/CD Pipeline (GitHub Actions)

```
Git Push / Pull Request to main
           │
           ▼
┌──────────────────────────────────────────┐
│            GitHub Actions                │
│                                          │
│  Step 1 → Checkout repository            │
│  Step 2 → Set up Python 3.10             │
│  Step 3 → pip install -r requirements    │
│  Step 4 → Lint with flake8              │
│  Step 5 → python manage.py test          │
│  Step 6 → docker build .                 │
│                                          │
│  ✅ All pass → ready to deploy           │
└──────────────────────────────────────────┘
```

---

## 📦 Quick Setup

### Option A — Docker (Recommended)

```bash
git clone https://github.com/Aghawafaabbass/Hyrex.git
cd Hyrex
cp .env.example .env        # fill in your values
docker-compose up --build
```

Backend API: `http://127.0.0.1:8000/`
Django Admin: `http://127.0.0.1:8000/admin/`

### Option B — Local Development

```bash
git clone https://github.com/Aghawafaabbass/Hyrex.git
cd Hyrex

# Backend
python -m venv env567
env567\Scripts\activate          # Windows
# source env567/bin/activate     # Mac/Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver       # → 127.0.0.1:8000

# Celery worker (separate terminal)
celery -A hyrex worker --loglevel=info

# Frontend (separate terminal)
cd frontend
npm install
npm start                        # → localhost:3000
```

### API Testing with Postman

```
1. Open Postman
2. Import: docs/Hyrex.postman_collection.json
3. Set environment: base_url = http://127.0.0.1:8000
4. Run "POST /api/token/" first → JWT token auto-populated
5. Test recruiter and candidate flows with correct role tokens
```

---

## 📁 Project Structure

```
Hyrex/
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
├── .gitignore
├── README.md
├── screenshots/
│   ├── 01_Login_Page.PNG
│   ├── 02_register.PNG
│   ├── 03_Recruiter_Dashboard.PNG
│   ├── 04_Recruiter_Browse_Jobs.PNG
│   ├── 05_Candidate_Login.PNG
│   ├── 06_Candidate_My_Applications.PNG
│   ├── 07_Candidate_Browse_Jobs.PNG
│   ├── 08_Candidate_jobs_Applied_Now.PNG
│   └── 09_Django_Administration.PNG
├── .github/
│   └── workflows/
│       └── ci.yml
├── hyrex/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── celery.py
├── users/
│   ├── models.py          # User model — role field: candidate / recruiter
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── jobs/
│   ├── models.py          # Job model, Category model
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── applications/
│   ├── models.py          # Application model
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
└── frontend/              # React app (localhost:3000)
```

---

## 🔮 Future Enhancements

- Recruiter view of received applications per job listing
- Application status pipeline (Under Review → Shortlisted → Rejected → Hired)
- Email notifications via Celery when a Candidate applies
- Resume / CV file upload per application
- AI-powered job matching (candidate skills ↔ job requirements)
- Full Postman collection published to Postman Public Workspace
- Candidate and Recruiter public profile pages
- PostgreSQL full-text search on job listings
- Kubernetes production deployment

---

## 📄 License

MIT License

---

**Hyrex** — Built with Django REST Framework + React  
*Full Stack Developer · Agha Wafa Abbas*  
[GitHub](https://github.com/Aghawafaabbass)
