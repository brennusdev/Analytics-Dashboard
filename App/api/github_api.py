"""
github_api.py

Responsável exclusivamente pela comunicação com a API do GitHub.

Este módulo NÃO calcula estatísticas.
Ele apenas faz requisições HTTP e retorna os dados.
"""

from typing import Any, Dict, List, Optional
import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

class GitHubAPI:
    BASE_URL = "https://api.github.com"

    def __init__(self, token: Optional[str] = None):
        self.token = token

    def _get_headers(self) -> Dict[str, str]:
        headers = {
            "Accept": "application/vnd.github.v3+json",
        }
        if self.token:
            headers["Authorization"] = f"token {self.token}"
        return headers

    def _request(self, url: str) -> Any:
        request = Request(url, headers=self._get_headers())
        try:
            with urlopen(request) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as error:
            raise RuntimeError(f"HTTP error {error.code}: {error.reason}") from error
        except URLError as error:
            raise RuntimeError(f"URL error: {error.reason}") from error

    def get_user_repositories(self, username: str) -> List[Dict[str, Any]]:
        url = f"{self.BASE_URL}/users/{username}/repos"
        return self._request(url)

    def get_user(self, username: str) -> Dict[str, Any]:
        url = f"{self.BASE_URL}/users/{username}"
        return self._request(url)

    def get_repository_commits(self, owner: str, repo: str) -> List[Dict[str, Any]]:
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/commits"
        return self._request(url)

    def get_repository_contributors(self, owner: str, repo: str) -> List[Dict[str, Any]]:
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/contributors"
        return self._request(url)