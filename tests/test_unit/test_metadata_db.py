from unittest.mock import patch

from mangarec.database.metadata_entity import MetadataEntity
from mangarec.database.metadata_entity_db import MetadataEntityDB


def test_base_entity_db():
    entity_db = MetadataEntityDB()
    assert entity_db.query_param_field == "ids[]"
    assert entity_db.version == 2
    assert entity_db.database == {}


@patch("mangarec.database.base_entity.sleep")
def test_metadata_entity_db_update(mock_sleep, manga_server_response, requests_mock):
    _ = mock_sleep
    requests_mock.get(MetadataEntity.entity_url, json=manga_server_response)
    entity_db = MetadataEntityDB()
    entity_db.update()
    assert len(entity_db) == 10


@patch("mangarec.database.base_entity.sleep")
def test_metadata_entity_db_can_store_and_load(mock_sleep, manga_server_response, requests_mock):
    _ = mock_sleep
    requests_mock.get(MetadataEntity.entity_url, json=manga_server_response)
    entity_db = MetadataEntityDB()
    entity_db.update()

    json_str = entity_db.to_json()

    new_entity_db = MetadataEntityDB.from_json(json_str)
    assert len(entity_db) == len(new_entity_db)

    new_json_str = new_entity_db.to_json()
    assert json_str == new_json_str
