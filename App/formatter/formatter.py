"""
formatter.py

Responsável pela apresentação das informações.
"""
from datetime import datetime


class DashboardFormatter:

    @staticmethod
    def line():

        print("=" * 60)

    @staticmethod
    def title():

        DashboardFormatter.line()

        print("         GitHub Analytics Dashboard")

        DashboardFormatter.line()

    @staticmethod
    def show_dashboard(

        user,

        repositories,

        stars,

        forks,

        main_language,

        languages,

        popular_repository,

        fork_repository,

        newest_repository,

        updated_repository

    ):

        DashboardFormatter.title()

        print()

        print(f"Usuário.............: {user['login']}")

        print(f"Nome................: {user['name']}")

        print(f"Bio.................: {user['bio']}")

        print(f"Empresa.............: {user['company']}")

        print(f"Localização.........: {user['location']}")

        print(f"Seguidores..........: {user['followers']}")

        print(f"Seguindo............: {user['following']}")

        print(f"Repositórios........: {repositories}")

        print()

        DashboardFormatter.line()

        print("ESTATÍSTICAS")

        DashboardFormatter.line()

        print(f"Stars...............: {stars}")

        print(f"Forks...............: {forks}")

        print(f"Linguagem Principal.: {main_language}")

        print()

        DashboardFormatter.line()

        print("LINGUAGENS")

        DashboardFormatter.line()

        for language, quantity in languages.items():

            print(f"{language:<20}{quantity}")

        print()

        DashboardFormatter.line()

        print("REPOSITÓRIOS")

        DashboardFormatter.line()

        if popular_repository:

            print(
                f"Mais Popular........: "
                f"{popular_repository['name']} "
                f"({popular_repository['stargazers_count']} ⭐)"
            )

        if fork_repository:

            print(
                f"Mais Forks..........: "
                f"{fork_repository['name']} "
                f"({fork_repository['forks_count']})"
            )

        if newest_repository:

            created = datetime.fromisoformat(
                newest_repository["created_at"].replace("Z", "+00:00")
            )

            print(
                f"Mais Novo...........: "
                f"{newest_repository['name']} "
                f"({created.strftime('%d/%m/%Y')})"
            )

        if updated_repository:

            updated = datetime.fromisoformat(
                updated_repository["updated_at"].replace("Z", "+00:00")
            )

            print(
                f"Última Atualização..: "
                f"{updated_repository['name']} "
                f"({updated.strftime('%d/%m/%Y')})"
            )

        print()

        DashboardFormatter.line()