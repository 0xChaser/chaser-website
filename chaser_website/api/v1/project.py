from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from chaser_website.db import get_session
from chaser_website.schemas.project import (ProjectIn, ProjectOut,ProjectPatch)
from chaser_website.schemas.page import Page
from chaser_website.services.project import ProjectService

router = APIRouter(prefix="/project", tags=["Project"])


@router.get("/", response_model=Page[ProjectOut])
async def list_projects(offset: int = 0, limit: int = 10, session: AsyncSession = Depends(get_session)):
    return await ProjectService.get_all_projects(session=session, offset=offset, limit=limit)


@router.get("/{id}", response_model=ProjectOut)
async def get_project(id: UUID, session: AsyncSession = Depends(get_session)):
    return await ProjectService.get_project_by_id(id, session)

@router.post("/")
async def add_project(project_data: ProjectIn, session: AsyncSession = Depends(get_session)):
    return await ProjectService.add_project(project_data, session)


@router.patch("/{id}", response_model=ProjectOut)
async def update_project(id: UUID, project: ProjectPatch, session: AsyncSession = Depends(get_session)):
    return await ProjectService.update_by_id(id, project, session)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_project(id: UUID, session: AsyncSession = Depends(get_session)):
    return await ProjectService.delete_by_id(id, session)
