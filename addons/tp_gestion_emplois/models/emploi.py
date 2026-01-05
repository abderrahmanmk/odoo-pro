from odoo import models, fields

class Emploi(models.Model):
    _name = 'tp.emploi'
    _description = 'Gestion Emploi du Temps'

    name = fields.Char(string='Matière', required=True)
    professeur = fields.Char(string='Professeur')
    salle = fields.Char(string='Salle')
    date = fields.Date(string='Date du cours')
    heure_debut = fields.Float(string='Heure de début')
    statut = fields.Selection([
        ('programmé', 'Programmé'),
        ('réalisé', 'Réalisé'),
        ('annulé', 'Annulé'),
    ], string='Statut', default='programmé')
    description = fields.Text(string='Remarques')
