from colander import MappingSchema, SchemaNode
from colander import String, Length

from deform import widget

class LoginSchema(MappingSchema):
    email = SchemaNode(String(),
                      description = 'Email Address')
    password = SchemaNode(String(),
                          widget = widget.PasswordWidget(),
                          validator = Length(min=5))
