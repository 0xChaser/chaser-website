import uuid

from sqlachemy import UUID ,String
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from project.models.base import Base

class Project(Base):
    __tablename__ = "projects"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, nullable=False, unique=True
    )
    project_name: Mapped[str] = mapped_column(String(), nullable=False)
    image_path: Mapped[str] = mapped_column(String(), nullable=False)
    description: Mapped[List[str]] = mapped_column(String(), nullable=True)
    technologies: Mapped[List[str]] = mapped_column(String(), nullable=True)
    url: Mapped[str] = mapped_column(String(), nullable=True)
