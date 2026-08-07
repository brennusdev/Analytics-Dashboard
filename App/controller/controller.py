"""
controller.py

Responsável por controlar o fluxo da aplicação.
"""
from api.github_api import GitHubAPI
from services.statistics import StatisticsService

class DashboardFormatter:

    @staticmethod
    def _resolve_user_name(user):
        if user is None:
            return "Usuário desconhecido"
        if hasattr(user, "name"):
            return user.name
        if hasattr(user, "login"):
            return user.login
        if isinstance(user, type):
            return user.__name__
        return str(user)

    @staticmethod
    def _format_languages(languages):
        if not languages:
            return "Nenhum idioma detectado."
        if isinstance(languages, dict):
            return "\n".join(f"- {language}: {count}" for language, count in languages.items())
        if isinstance(languages, list):
            return "\n".join(f"- {language}" for language in languages)
        return str(languages)

    @staticmethod
    def _format_repository(repository):
        if not repository:
            return "Nenhum repositório disponível."
        name = repository.get("name", getattr(repository, "name", None)) or "Desconhecido"
        stars = repository.get("stargazers_count", repository.get("stargazers", getattr(repository, "stargazers_count", 0)))
        forks = repository.get("forks_count", repository.get("forks", getattr(repository, "forks_count", 0)))
        updated_at = repository.get("updated_at", getattr(repository, "updated_at", ""))
        url = repository.get("html_url", getattr(repository, "html_url", ""))
        details = [
            f"Nome: {name}",
            f"Estrelas: {stars}",
            f"Forks: {forks}",
        ]
        if updated_at:
            details.append(f"Última atualização: {updated_at}")
        if url:
            details.append(f"URL: {url}")
        return " | ".join(details)

    @classmethod
    def show_dashboard(cls,
                       user,
                       repositories,
                       stars,
                       forks,
                       main_language,
                       languages,
                       popular_repository,
                       fork_repository,
                       newest_repository,
                       updated_repository):
        user_name = cls._resolve_user_name(user)
        dashboard_lines = [
            f"Dashboard de {user_name}",
            "=" * (12 + len(user_name)),
            f"Total de repositórios: {repositories}",
            f"Total de estrelas: {stars}",
            f"Total de forks: {forks}",
            f"Principal linguagem: {main_language or 'Nenhuma'}",
            "Idiomas usados:",
            cls._format_languages(languages),
            "Repositório mais popular:",
            cls._format_repository(popular_repository),
            "Repositório mais forkado:",
            cls._format_repository(fork_repository),
            "Repositório mais novo:",
            cls._format_repository(newest_repository),
            "Repositório mais recentemente atualizado:",
            cls._format_repository(updated_repository),
        ]
        dashboard = "\n".join(dashboard_lines)
        print(dashboard)
        return dashboard

class DashboardController:

    def __init__(self):

        self.github = GitHubAPI()

    def _calculate_total_forks(self, repositories):
        total_forks = 0
        for repository in repositories or []:
            if isinstance(repository, dict):
                total_forks += repository.get("forks", repository.get("forks_count", 0))
            else:
                total_forks += getattr(repository, "forks", getattr(repository, "forks_count", 0))
        return total_forks

    def generate_dashboard(self, username: str):

        # Obtém todos os repositórios
        repositories = self.github.get_user_repositories(username)

        # Estatísticas
        total_repositories = StatisticsService.total_repositories(repositories)

        total_stars = StatisticsService.total_stars(repositories)

        total_forks = self._calculate_total_forks(repositories)

        main_language = StatisticsService.most_used_language(repositories)

        languages = StatisticsService.languages(repositories)

        popular_repository = StatisticsService.most_starred_repository(
            repositories
        )

        fork_repository = StatisticsService.most_forked_repository(
            repositories
        )

        newest_repository = StatisticsService.newest_repository(
            repositories
        )

        updated_repository = StatisticsService.last_updated_repository(
            repositories
        )

        # Monta Dashboard
        user = self.github.get_user(username)
        
        DashboardFormatter.show_dashboard(

            user=user,

            repositories=total_repositories,

            stars=total_stars,

            forks=total_forks,

            main_language=main_language,

            languages=languages,

            popular_repository=popular_repository,

            fork_repository=fork_repository,

            newest_repository=newest_repository,

            updated_repository=updated_repository

        )