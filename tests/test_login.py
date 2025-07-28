import pytest
import os
from dotenv import load_dotenv
from config.request_handler import Service
from config import routes


# Load environment variables
load_dotenv()
base_url = os.getenv("BASE_URL")

# @pytest.mark.parametrize("request_body")
def test_login_api():
    login_service = Service(
        url=base_url + routes.LOGIN_API,
        method="POST",
        body={
            "username": os.getenv("USER_NAME"),
            "password": os.getenv("PASSWORD")
        }
    )
    response = login_service.post_request()
    print("Response JSON:", response.json())

    assert response.status_code == 200, f"Failed with status {response.status_code}"


