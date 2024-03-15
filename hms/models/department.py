from odoo import models, fields, api


class Department(models.Model):
    _name = "hms.department"
    _description = "Department"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True)
    capacity = fields.Integer(required=True)
    is_opened = fields.Boolean(default=True)
    ref = fields.Char(default="New", readonly=1)
    patients_ids = fields.One2many("hms.patient", "department_id", string="Patients")
    doctors_ids = fields.One2many('hms.doctor', 'department_id', string='Doctors')


    @api.model
    def create(self, vals):
        res = super(Department, self).create(vals)
        if res.ref == "New":
            res.ref = self.env['ir.sequence'].next_by_code('department_seq')

        return res

