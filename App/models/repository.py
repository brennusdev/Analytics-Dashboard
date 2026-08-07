"""
Modelo de um repositório.
"""

from dataclasses import dataclass


@dataclass
class Repository:

    name: str

    language: str | None

    description: str | None

    stars: int

    forks: int

    open_issues: int

    created_at: str

    updated_at: str