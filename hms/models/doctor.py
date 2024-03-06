from odoo import models, fields


class Doctor(models.Model):
    _name = "hms.doctor"
    _description = "Doctor"
    _rec_name = "f_name"

    f_name = fields.Char("First name")
    l_name = fields.Char("Last name")
    image = fields.Binary()
    department_id = fields.Many2one('hms.department', string='Department')


