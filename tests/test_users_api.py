import pytest

from api.api_client import APIClient
from utils.schema_validator import validate_schema



@pytest.mark.api
@pytest.mark.regression
@pytest.mark.smoke
class TestUsersAPI:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def test_get_users(self):

        client = APIClient(self.BASE_URL)

        response = client.get("/users")

        assert response.status_code == 200

        validate_schema(
            response.json(),
            "schemas/users_schema.json"
        )