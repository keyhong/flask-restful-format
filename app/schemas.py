"""TODO"""

from marshmallow import Schema, fields


class FormPlainInputSchema(Schema):
    """TODO: pass"""

    parent_field_1 = fields.Str(required=True)
    parent_field_2 = fields.Integer(required=True)
    parent_field_3 = fields.Float(required=True)


class FormInputSchema(FormPlainInputSchema):
    """TODO: pass"""

    child_field = fields.Str(dump_only=True)

class APIReturnSchema(Schema):
    """TODO: pass"""

    parent_field_1 = fields.Str(required=True)
    parent_field_2 = fields.Integer(required=True)
    parent_field_3 = fields.Float(required=True)
