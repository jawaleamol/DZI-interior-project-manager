# BuildFlow Interior Project Manager Specification

This document summarizes the project requirements for the **BuildFlow** system as provided previously. The system manages interior design projects by connecting project managers, customers, and agency teams.

## Tech Stack
- Django 5.x with Django REST Framework
- PostgreSQL 15+
- Django templates + Bootstrap 5 + Alpine.js
- Custom user model with role field
- Celery + Redis for tasks
- AWS S3 via django-storages
- WeasyPrint for PDF generation
- Django Channels for real-time features

## Core Modules
1. **Project Management** – Projects, memberships, and timelines with unique portal URLs and role-based dashboards.
2. **Query Management** – Track project issues with assignment logic, permissioned status changes, and SLA alerts.
3. **Billing & Invoices** – Itemized bill creation, approvals, PDF invoices, and payment integration.
4. **Document Management** – Category-based file storage with version control and permissions.
5. **Dashboards** – Separate dashboard views for admins, project managers, customers, and agencies.

## Advanced Features
- Real-time chat system
- Daily logbook for progress summaries
- Material tracker for orders and installations

## API Endpoints
Endpoints follow a RESTful style under `/api/` with authentication, project management, query management, billing, and documents routes.

## Development Phases
1. **Phase 1** – Authentication, role system, and basic project management (weeks 1-3).
2. **Phase 2** – Query system and dashboards (weeks 4-6).
3. **Phase 3** – Billing, documents, and permissions (weeks 7-9).
4. **Phase 4** – Real-time features, payments, testing, and deployment (weeks 10-12).

