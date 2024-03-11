from odoo import models, fields, api
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta


class ResPartner(models.Model):
    _inherit = "res.partner"


    vat = fields.Char(required=True, readonly=0)

    related_patient_id = fields.Many2one("hms.patient")



    @api.constrains('email')
    def _check_unique_email_customer(self):
        for rec in self:
            if rec.email:
                existing_patient = self.env['hms.patient'].search([('email', '=', rec.email)])
                if existing_patient:
                    raise ValidationError("This email is already linked to a patient.")



    def unlink(self):
        for rec in self:
            if rec.related_patient_id:
                raise ValidationError("Cannot delete a customer linked to a patient.")
        return super(ResPartner, self).unlink()