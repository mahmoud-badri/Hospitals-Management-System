from odoo import models, fields

class Patient(models.Model):
    _name = "hms.patient"
    _description = "Patient"
    _rec_name = "f_name"

    f_name = fields.Char("First name")
    l_name = fields.Char("Last name")
    birth_day = fields.Date("Birth date")
    history = fields.Html()
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
    age = fields.Integer()
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ])
    department_id = fields.Many2one("hms.department", string="Department")
    doctor_id = fields.Many2one("hms.doctor", string="Doctor")
