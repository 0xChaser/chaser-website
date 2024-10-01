from uuid import UUID

from pydantic import BaseModel, ConfigDict, HttpUrl
from typing import List
from chaser_website.utils import optional



class Description(BaseModel):
    en: str
    fr: str


class Technologies(BaseModel):
    frontend: List[str] | None
    backend: List[str]| None
    services: List[str] | None
    

class ProjectBase(BaseModel):
    project_name: str
    image_path: str
    description: Description
    technologies: Technologies
    url: HttpUrl | None

    model_config = ConfigDict(from_attributes=True)

class ProjectIn(ProjectBase):
    pass
    
class ProjectOut(ProjectIn):
    id: UUID

@optional
class ProjectPatch(ProjectIn):
    pass