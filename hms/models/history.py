from odoo import models, fields


class History(models.Model):
    _name = "hms.history"
    _description = "History"


    user_id = fields.Many2one("res.users")
    patient_id = fields.Many2one("hms.patient")
    old_state = fields.Char()
    new_state = fields.Char()