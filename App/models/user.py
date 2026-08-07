"""
Modelo do usuário.
"""

from dataclasses import dataclass


@dataclass
class User:

    login: str

    name: str

    bio: str | None

    company: str | None

    location: str | None

    followers: int

    following: int

    public_repos: int

    created_at: str