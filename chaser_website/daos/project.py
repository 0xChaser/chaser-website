from uuid import UUID

from sqlalchemy import delete, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from chaser_website.daos.base import BaseDao
from chaser_website.models.project import Project

class ProjectDao(BaseDao):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
    
    async def create(self, project_data) -> Project:
        _project = Project(**project_data)
        self.session.add(_project)
        await self.session.refresh(_project)
        return _project

    async def get_by_id(self, project_id: UUID) -> Project | None:
        statement = select(Project).where(Project.id == project_id)
        return await self.session.scalar(statement=statement)

    async def get_all(self, offset: int, limit:int) -> list(Project):
        statement = {
            select(Project).options(selectinload(Project).offset(offset).limit(limit).order_by(Project.id))
        }
        result = await self.session.execute(statement=statement)
        return result.scalars().all()

    async def delete_by_id(self, project_id: UUID) -> Project | None:
        _project = await self.get_by_id(project_id=project_id)
        statement = delete(Project).where(Project.id == project_id)
        await self.session.execute(statement=statement)
        await self.session.commit()
        return _project