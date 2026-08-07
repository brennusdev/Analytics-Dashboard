from fastapi import APIRouter

from controller.controller import DashboardController

router = APIRouter()

controller = DashboardController()


@router.get("/github/{username}")

def get_dashboard(username: str):

    return controller.generate_dashboard(username)