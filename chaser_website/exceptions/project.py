from chaser_website.exceptions.base import NotFound


class ProjectNotFound(NotFound):
    def __init__(self) -> None:
        detail = "Project not found with this id"
        super().__init__(detail)
