import pytest


@pytest.fixture
def manga_name():
    return "Kanojyo to Himitsu to Koimoyou"


@pytest.fixture
def manga_request_response():
    # Abbreviated response for Kanojyo to Himitsu to Koimoyou
    return {
        "result": "ok",
        "response": "collection",
        "data": [
            {
                "id": "831b12b8-2d0e-4397-8719-1efee4c32f40",
                "type": "manga",
                "attributes": {
                    "title": {"en": "Oshimai"},
                    "altTitles": [
                        {"en": "4 Page Stories"},
                        {"en": "Oshi-Mai: Four Page Stories"},
                        {"en": "The 4 Pages"},
                        {"ja": "おしまい"},
                        {"ja": "お四枚"},
                        {"en": "Oshi-Mai: Four Page Storys"},
                    ],
                    "description": {"en": "A collection of twitter published manga by Kawasaki Tadataka..."},
                    "isLocked": False,
                    "links": {
                        "al": "119448",
                        "kt": "56601",
                        "mu": "176587",
                        "amz": "https://www.amazon.co.jp/gp/product/B084JRQCL3",
                    },
                    "originalLanguage": "ja",
                    "lastVolume": "",
                    "lastChapter": "",
                    "publicationDemographic": "seinen",
                    "status": "ongoing",
                    "year": 2020,
                    "contentRating": "suggestive",
                    "tags": [
                        {
                            "id": "423e2eae-a7a2-4a8b-ac03-a8351462d71d",
                            "type": "tag",
                            "attributes": {
                                "name": {"en": "Romance"},
                                "description": {},
                                "group": "genre",
                                "version": 1,
                            },
                            "relationships": [],
                        },
                        {
                            "id": "4d32cc48-9f00-4cca-9b5a-a839f0764984",
                            "type": "tag",
                            "attributes": {"name": {"en": "Comedy"}, "description": {}, "group": "genre", "version": 1},
                            "relationships": [],
                        },
                        {
                            "id": "51d83883-4103-437c-b4b1-731cb73d786c",
                            "type": "tag",
                            "attributes": {
                                "name": {"en": "Anthology"},
                                "description": {},
                                "group": "format",
                                "version": 1,
                            },
                            "relationships": [],
                        },
                        {
                            "id": "caaa44eb-cd40-4177-b930-79d3ef2afe87",
                            "type": "tag",
                            "attributes": {
                                "name": {"en": "School Life"},
                                "description": {},
                                "group": "theme",
                                "version": 1,
                            },
                            "relationships": [],
                        },
                        {
                            "id": "e5301a23-ebd9-49dd-a0cb-2add944c7fe9",
                            "type": "tag",
                            "attributes": {
                                "name": {"en": "Slice of Life"},
                                "description": {},
                                "group": "genre",
                                "version": 1,
                            },
                            "relationships": [],
                        },
                    ],
                    "state": "published",
                    "chapterNumbersResetOnNewVolume": False,
                    "createdAt": "2020-07-23T14:50:37+00:00",
                    "updatedAt": "2022-12-31T11:57:41+00:00",
                    "version": 15,
                    "availableTranslatedLanguages": ["en", "vi", "fr", "zh", "pt-br", "es-la", "id"],
                    "latestUploadedChapter": "9a8a1c1d-5b8f-4ad2-af34-f7d61200ef6d",
                },
                "relationships": [
                    {"id": "88259f42-5a70-4eff-b5f0-8687ab8844b9", "type": "author"},
                    {"id": "88259f42-5a70-4eff-b5f0-8687ab8844b9", "type": "artist"},
                    {"id": "be31ba9c-3490-41ea-b1bd-7f31cad7322f", "type": "cover_art"},
                ],
            },
            {
                "id": "f98660a1-d2e2-461c-960d-7bd13df8b76d",
                "type": "manga",
                "attributes": {
                    "title": {"en": "Kanojo to Himitsu to Koimoyou"},
                    "altTitles": [
                        {"en": "Let's Love Girlfriends and Secrets"},
                        {"ja": "カノジョと秘密と恋もよう"},
                        {"zh": "女朋友与秘密与恋爱模样"},
                        {"en": "Girlfriends and Secrets and Matters of the Heart"},
                        {"ja-ro": "Kanojyo to Himitsu to Koimoyou"},
                    ],
                    "description": {"en": "A yuri comedy between two girls who seem different but are ..."},
                    "isLocked": False,
                    "links": {
                        "al": "116918",
                        "ap": "kanojo-to-himitsu-to-koi-moyou",
                        "mu": "158719",
                        "amz": "https://www.amazon.co.jp",
                        "mal": "133320",
                    },
                    "originalLanguage": "ja",
                    "lastVolume": "2",
                    "lastChapter": "19",
                    "publicationDemographic": "seinen",
                    "status": "completed",
                    "year": 2019,
                    "contentRating": "safe",
                    "tags": [
                        {
                            "id": "4d32cc48-9f00-4cca-9b5a-a839f0764984",
                            "type": "tag",
                            "attributes": {"name": {"en": "Comedy"}, "description": {}, "group": "genre", "version": 1},
                            "relationships": [],
                        },
                        {
                            "id": "a3c67850-4684-404e-9b7f-c69850ee5da6",
                            "type": "tag",
                            "attributes": {
                                "name": {"en": "Girls' Love"},
                                "description": {},
                                "group": "genre",
                                "version": 1,
                            },
                            "relationships": [],
                        },
                        {
                            "id": "e5301a23-ebd9-49dd-a0cb-2add944c7fe9",
                            "type": "tag",
                            "attributes": {
                                "name": {"en": "Slice of Life"},
                                "description": {},
                                "group": "genre",
                                "version": 1,
                            },
                            "relationships": [],
                        },
                        {
                            "id": "eabc5b4c-6aff-42f3-b657-3e90cbd00b75",
                            "type": "tag",
                            "attributes": {
                                "name": {"en": "Supernatural"},
                                "description": {},
                                "group": "theme",
                                "version": 1,
                            },
                            "relationships": [],
                        },
                    ],
                    "state": "published",
                    "chapterNumbersResetOnNewVolume": False,
                    "createdAt": "2021-02-02T08:15:25+00:00",
                    "updatedAt": "2023-05-01T03:47:11+00:00",
                    "version": 30,
                    "availableTranslatedLanguages": ["en"],
                    "latestUploadedChapter": "b902c44d-cb34-4077-9501-c90b1216f2fb",
                },
                "relationships": [
                    {"id": "62b03b76-6565-4dab-b7d7-d38bce56808f", "type": "author"},
                    {"id": "62b03b76-6565-4dab-b7d7-d38bce56808f", "type": "artist"},
                    {"id": "af191279-8217-4f1b-a543-943b34af31d4", "type": "cover_art"},
                ],
            },
        ],
        "limit": 10,
        "offset": 0,
        "total": 2,
    }


@pytest.fixture
def manga_request_response_single(manga_request_response):
    return {
        "result": "ok",
        "response": "collection",
        "data": [manga_request_response["data"][0]],
        "limit": 10,
        "offset": 0,
        "total": 1,
    }


@pytest.fixture
def manga_request_content(manga_request_response):
    return manga_request_response["data"][0]


@pytest.fixture
def manga_request_id(manga_request_content):
    return manga_request_content["id"]


@pytest.fixture
def check_entity_for_save_and_load():
    def _check_entity_for_save_and_load(entity):
        json_str = entity.to_json()
        new_entity = entity.from_json(json_str)
        assert entity.content == new_entity.content

        new_json_str = new_entity.to_json()
        assert json_str == new_json_str

    return _check_entity_for_save_and_load
