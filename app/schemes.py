from marshmallow import Schema, fields


class CurrencySchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)


class RecordSchema(Schema):
    user_id = fields.Integer(required=True)
    category_id = fields.Integer(required=True)
    user_category = fields.Integer()
    amount = fields.Float(required=True)
    currency_id = fields.Integer()


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    default_currency_id = fields.Integer(required=True)


class CategorySchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    is_custom = fields.Boolean()
    user_id = fields.Integer()
