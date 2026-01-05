# Odoo Education Management 📚

A Dockerized Odoo 17 application designed for school timetable management. This project includes a custom module, `tp_gestion_emplois`, to handle the scheduling of educational sessions, professors, and classrooms.

## 📂 Project Structure

\`\`\`text
odoo-docker/
├── addons/
│   └── tp_gestion_emplois/  # Custom module for timetable management
├── config/                  # Odoo configuration files
└── docker-compose.yml       # Container orchestration
\`\`\`

## 🚀 Infrastructure & Setup

The application is containerized using Docker.

### Services
* **Web Service (Odoo)**
    * **Image:** `odoo:17.0`
    * **Port:** `8069`
    * **Volumes:**
        * `addons` mapped to `/mnt/extra-addons`
        * `config` mapped to `/etc/odoo`
* **Database Service (PostgreSQL)**
    * **Image:** `postgres:16`
    * **Database Name:** `odoo_db`
    * **User:** `odoo`
    * **Password:** `odoo`
    * **Persistence:** Uses `odoo-db-data` volume.

### How to Run
1. Ensure you have **Docker** and **Docker Compose** installed.
2. Navigate to the project directory:
   \`\`\`bash
   cd odoo-docker
   \`\`\`
3. Start the containers:
   \`\`\`bash
   docker-compose up -d
   \`\`\`

## 🧩 Custom Module: `tp_gestion_emplois`

**Category:** Education  
**Dependencies:** `base`  
**Description:** Module pour la gestion des emplois du temps scolaire (School timetable management).

### Data Model (`tp.emploi`)
Defined in `models/emploi.py`.

| Field Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| `name` | Char | Matière | **Required** |
| `professeur` | Char | Professeur | |
| `salle` | Char | Salle | |
| `date` | Date | Date du cours | |
| `heure_debut` | Float | Heure de début | |
| `statut` | Selection | État de la séance | Options: *Programmé* (Default), *Réalisé*, *Annulé* |
| `description` | Text | Remarques | |

### User Interface
Defined in `views/emploi_views.xml`.

* **Menus:**
    * **Root:** "Emplois du Temps"
    * **Sub-menu:** "Gestion des Séances"
* **Views:**
    1.  **List View (Tree):** Shows Matière, Professeur, Date, Heure, Salle, and Statut.
    2.  **Form View:** organized with:
        * *Header:* Basic info (Matière, Professeur, Salle)
        * *Details:* Scheduling (Date, Heure, Statut)
        * *Footer:* Description/Remarques

## 📖 Usage Guide

Follow these steps to verify and use the application:

1.  **Access the Interface:**
    Open your browser and navigate to [http://localhost:8069](http://localhost:8069).
2.  **Login:**
    Log in using your admin credentials (default is usually set during the first database creation).
3.  **Install the Module:**
    * Go to the **Apps** menu.
    * Search for `tp_gestion_emplois`.
    * Click **Activate/Install**.
4.  **Manage Schedules:**
    * Click the **"Emplois du Temps"** icon in the main menu grid.
    * Use "Gestion des Séances" to create new course schedules.
