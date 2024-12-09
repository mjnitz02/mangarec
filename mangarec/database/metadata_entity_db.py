import json
from typing import Dict

from mangarec.database.base_entity import BaseEntityObject
from mangarec.database.metadata_entity import MetadataEntity


class MetadataEntityDB(BaseEntityObject):
    entity_class = MetadataEntity
    database: Dict[str, entity_class]
    query_param_field = "ids[]"

    def __init__(self, database=None):
        self.version = 2
        self.database = {} if database is None else database

    def __getitem__(self, entity_id) -> entity_class:
        return self.database.get(entity_id)

    def __len__(self):
        return len(self.database)

    def keys(self):
        return self.database.keys()

    def to_json(self):
        content = {}
        for key, value in self.database.items():
            if isinstance(value, list):
                content[key] = [v.to_json() for v in value]
            else:
                content[key] = value.to_json()
        return json.dumps(content)

    @classmethod
    def from_json(cls, json_str):
        database_contents = json.loads(json_str)
        database = {}
        for key, value in database_contents.items():
            database[key] = cls.entity_class.from_json(value)
        return cls(database=database)

    def update(self):
        responses = self.entity_class.unpaginate_request(self.entity_class.entity_url, {})
        for response in responses:
            entity = self.entity_class(response)
            self.database[entity.entity_id] = entity
