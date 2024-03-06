from odoo import models, fields

class Department(models.Model):
    _name = "hms.department"
    _description = "Department"


    name = fields.Char()
    capacity = fields.Integer()
    is_opened = fields.Boolean()
    patients_ids = fields.One2many("hms.patient", "department_id", string="Patients")
    doctors_ids = fields.One2many('hms.doctor', 'department_id', string='Doctors')

