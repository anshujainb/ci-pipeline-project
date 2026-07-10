import os


USERNAME = os.getenv(
    "TEST_USERNAME",
    "standard_user"
)

PASSWORD = os.getenv(
    "TEST_PASSWORD",
    "wrong_secret_sauce"
)

BASE_URL = os.getenv(
    "BASE_URL",
    "https://www.saucedemo.com"
)