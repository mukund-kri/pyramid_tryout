import colander


class TaskSchema(colander.MappingSchema):
    task = colander.SchemaNode(colander.String())
