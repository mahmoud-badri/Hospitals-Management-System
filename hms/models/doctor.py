from odoo import models, fields, api


class Doctor(models.Model):
    _name = "hms.doctor"
    _description = "Doctor"
    _rec_name = "f_name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    f_name = fields.Char("First name", required=True)
    l_name = fields.Char("Last name", required=True)
    ref = fields.Char(default="New", readonly=1)
    image = fields.Binary()
    department_id = fields.Many2one('hms.department', string='Department', tracing=1)
    patient_ids = fields.One2many("hms.patient", "doctor_id")


    @api.model
    def create(self, vals):
        res = super(Doctor, self).create(vals)
        if res.ref == 'New':
            res.ref = self.env['ir.sequence'].next_by_code("doctor_seq")
        return res