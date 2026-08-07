"""Testes do StatisticsService"""

# Ajusta sys.path para permitir importações locais quando executado pelos testes
import sys
from pathlib import Path
from importlib import import_module

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

StatisticsService = import_module("app.services.statistics").StatisticsService


repositories = [

    {
        "name": "Projeto A",
        "language": "Python",
        "stargazers_count": 10,
        "forks_count": 3,
        "created_at": "2024-01-01T12:00:00Z",
        "updated_at": "2024-01-20T12:00:00Z",
    },

    {
        "name": "Projeto B",
        "language": "Python",
        "stargazers_count": 25,
        "forks_count": 6,
        "created_at": "2024-02-01T12:00:00Z",
        "updated_at": "2024-02-10T12:00:00Z",
    },

    {
        "name": "Projeto C",
        "language": "JavaScript",
        "stargazers_count": 5,
        "forks_count": 1,
        "created_at": "2024-03-01T12:00:00Z",
        "updated_at": "2024-03-15T12:00:00Z",
    },

]