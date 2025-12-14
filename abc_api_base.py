from abc import ABC, abstractmethod
import requests


class ApiBase(ABC):
    """
    Abstract Base Class for API interactions
    """

    @abstractmethod
    def build_url(self, user_input: str) -> str:
        pass

    @abstractmethod
    def fetch_data(self, user_input: str) -> dict:
        pass

    @abstractmethod
    def parse_data(self, data: dict) -> str:
        pass

    def get_results(self, user_input: str) -> str:
        """
        Template method that controls the API workflow
        """
        try:
            raw_data = self.fetch_data(user_input)
            return self.parse_data(raw_data)
        except requests.exceptions.RequestException:
            return "❌ Error: Unable to connect to the API."
        except Exception as e:
            return f"❌ Unexpected error: {e}"
