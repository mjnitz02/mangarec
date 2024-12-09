from mangarec.database.base_db import BaseEntityDB
from mangarec.database.metadata_entity import MetadataEntity


class MetadataEntityDB(BaseEntityDB):
    entity_class = MetadataEntity
