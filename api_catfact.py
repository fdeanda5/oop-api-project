import requests
from abc_api_base import ApiBase


class CatFactApi(ApiBase):
    """
    Concrete implementation of ApiBase using the Cat Facts API
    """

    BASE_URL = "https://catfact.ninja/fact"

    def build_url(self, user_input: str) -> str:
        # API does not require user input, but method is required
        return self.BASE_URL

    def fetch_data(self, user_input: str) -> dict:
        url = self.build_url(user_input)
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()

    def parse_data(self, data: dict) -> str:
        fact = data.get("fact", "No fact available.")
        length = data.get("length", 0)

        return (
            "\n=== 🐱 Random Cat Fact 🐱 ===\n"
            f"Fact: {fact}\n"
            f"Length: {length} characters\n"
        )
