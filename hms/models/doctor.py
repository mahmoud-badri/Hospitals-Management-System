from odoo import models, fields


class Doctor(models.Model):
    _name = "hms.doctor"
    _description = "Doctor"
    _rec_name = "f_name"

    f_name = fields.Char("First name", required=True)
    l_name = fields.Char("Last name", required=True)
    image = fields.Binary()
    department_id = fields.Many2one('hms.department', string='Department')
    patient_ids = fields.One2many("hms.patient", "doctor_id")


