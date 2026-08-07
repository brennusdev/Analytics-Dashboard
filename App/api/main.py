"""
Ponto de entrada da aplicação.
"""

from controller.controller import DashboardController


def main():

    print("=" * 60)
    print("GitHub Analytics Dashboard")
    print("=" * 60)

    username = input(
        "\nDigite o usuário do GitHub: "
    ).strip()

    if username == "":
        print("Usuário inválido.")
        return

    controller = DashboardController()

    controller.generate_dashboard(username)


if __name__ == "__main__":
    main()