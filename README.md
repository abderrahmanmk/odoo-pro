##Project Report: Odoo Education
##Management
#1. Project Overview
The project is a Dockerized Odoo 17 application with a custom module
named
tp_gestion_emplois designed for school timetable management.
Project Structure
odoo-docker/
├── addons/
│
└── tp_gestion_emplois/
├── config/
└── docker-compose.yml

#2. Infrastructure
The application runs on Docker containers defined in docker-
compose.yml.
• Web Service:
○ Image: odoo:17.0
○ Port: 8069
○ Mounts:
■ addons -> /mnt/extra-addons
■ config -> /etc/odoo
○ Dependencies: db service
• DB Service:
○ Image: postgres:16
○ Database: odoo_db
○ User/Pass: odoo/odoo
○ Volume: odoo-db-data for persistence
#3. Custom Module: tp_gestion_emplois
This module provides functionality to manage educational sessions (Emploi
du Temps).
Module Manifest
• Name: tp_gestion_emplois
• Category: Education
• Description: Module pour la gestion des emplois du temps scolaire.
• Dependencies: base
Data Model (tp.emploi)
Defined in models/emploi.py.
Field NameTypeDescription
name
professeur
salle
date
heure_debut
statutChar
Char
Char
Date
Float
SelectiondescriptionTextMatière (Required)
Professeur
Salle
Date du cours
Heure de début
Programmé, Réalisé,
Annulé (Default:
Programmé)
Remarques
User Interface
Defined in views/emploi_views.xml.
Menus
• Root Menu: "Emplois du Temps"
• Sub Menu: "Gestion des Séances" (Opens the list view of sessions)
Views
1. List View (Tree): Displays the following columns:
• Matière
• Professeur
• Date
• Heure de début
• Salle
• Statut
2. Form View: Allows creating and editing sessions with grouped fields:
• Header: Basic info (Matière, Professeur, Salle)
• Details: Scheduling (Date, Heure, Statut)
• Footer: Description/Remarques
#4. Usage
To verify the application:
1. Navigate to http://localhost:8069.
2. Log in as admin.
3. Install tp_gestion_emplois from the Apps menu.
4. Access "Emplois du Temps" from the main menu grid.
5. Create and manage course schedules.
