from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class Patient(models.Model):
    _name = "hms.patient"
    _description = "Patient"
    _rec_name = "f_name"

    f_name = fields.Char("First name", required=True)
    l_name = fields.Char("Last name", required=True)
    email = fields.Char(required=True)
    birth_day = fields.Date("Birth date")
    history = fields.Html(attrs={'invisible': [('age', '<', 50)]})
    cr_ratio = fields.Float("CR Ratio")
    blood = fields.Selection([
        ("type_a", "Type A"),
        ("type_b", "Type B"),
        ("type_ab", "Type AB"),
        ("type_o", "Type O"),
    ])
    pcr = fields.Boolean('PCR')
    image = fields.Binary()
    address = fields.Text()
    age = fields.Integer(readonly=1, compute="_compute_age")
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ], default='undetermined')
    department_id = fields.Many2one("hms.department", string="Department")
    doctor_id = fields.Many2one("hms.doctor", string="Doctor")
    log_history_ids = fields.One2many("log.history", "patient_id")



    _sql_constraints = [('unique_email', 'UNIQUE(email)', 'This Email is Already Exist')]
    @api.onchange('age')
    def _onchange_age(self):
        if self.age and self.age < 30:
            self.pcr = True
            return {'warning': {'title': 'Warning', 'message': 'PCR has been checked due to age below 30.'}}


    @api.onchange('department_id')
    def _onchange_department(self):
        if self.department_id and not self.department_id.is_opened:
            warning_msg = {
                'title': 'Warning',
                'message': 'Selected department is closed. Please choose another department.'
            }
            raise ValidationError(warning_msg['message'])



    @api.onchange("pcr")
    def _onchange_pcr(self):
        if self.pcr and self.cr_ratio == 0.00:
            warning_msg = {
                'title': 'Warning',
                'message': 'CR Ratio is mandatory when PCR is checked..'
            }
            raise ValidationError(warning_msg['message'])


    @api.onchange('age')
    def _onchange_age_hide_history(self):
        for rec in self:
            if rec.age < 50:
                rec.update({'history': False})



    @api.depends('birth_day')
    def _compute_age(self):
        for rec in self:
            if rec.birth_day:
                rec.age = relativedelta(fields.Date.today(), rec.birth_day).years
            else:
                rec.age = False
class LogHistory(models.Model):
    _name = "log.history"
    _description = "Log History"

    created_by = fields.Char()
    date = fields.Datetime(default=lambda self: fields.Datetime.now())
    description = fields.Text()
    patient_id = fields.Many2one("hms.patient")
