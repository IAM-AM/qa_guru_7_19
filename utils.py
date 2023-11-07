import json
import os.path


def load_schema(name):
    path = os.path.join("json_schemas", name)
    with open(path) as file:
        json_schemas = json.loads(file.read())

    return json_schemas
