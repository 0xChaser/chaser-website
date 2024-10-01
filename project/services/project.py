from uuid import UUID

from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from project.daos import project
from project.exceptions.project import ProjectNotFound
from project.schemas.project import (ProjectIn, ProjectOut, ProjectPatch)
from project.schemas.page import Page


class ProjectService:
    @staticmethod
    async def add_project(project_data: ProjectIn, session: AsyncSession):
        new_project = await project.ProjectDao(session).create(project_data.model_dump())
        logger.info(f"New project created successfully: {new_project}")
        return new_project

    @staticmethod
    async def get_all_projects(offset: int, limit: int, session: AsyncSession) -> Page[ProjectOut]:
        all_projects = await project.ProjectDao(session).get_all(offset=offset, limit=limit)
        return Page(
            total=await project.ProjectDao(session).count(),
            items=[ProjectOut.model_validate(_project) for _project in all_projects],
            offset=offset,
            limit=limit
        )

    @staticmethod
    async def get_project_by_id(project_id: UUID, session: AsyncSession) -> ProjectOut:
        _project = await project.ProjectDao(session).get_by_id(project_id)
        if not _project:
            raise ProjectNotFound
        return _project

    @staticmethod
    async def update_by_id(project_id: UUID, project_patch: ProjectPatch, session: AsyncSession) -> ProjectOut:
        _project = await project.ProjectDao(session).get_by_id(project_id)
        if not _project:
            raise ProjectNotFound
        for key, value in project_patch.model_dump(exclude_unset=True).items():
            setattr(_project, key, value)
        await session.commit()
        return _project

    @staticmethod
    async def delete_by_id(project_id: UUID, session: AsyncSession):
        _project = await project.ProjectDao(session).delete_by_id(project_id)
        if not _project:
            raise ProjectNotFound
        return _project
