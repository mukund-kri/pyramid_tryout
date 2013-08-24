import colander


class TaskSchema(colander.MappingSchema):
    title = colander.SchemaNode(colander.String())
