from odoo import models, fields


class Department(models.Model):
    _name = "hms.department"
    _description = "Department"


    name = fields.Char(required=True)
    capacity = fields.Integer(required=True)
    is_opened = fields.Boolean(default=True)
    patients_ids = fields.One2many("hms.patient", "department_id", string="Patients")
    doctors_ids = fields.One2many('hms.doctor', 'department_id', string='Doctors')
