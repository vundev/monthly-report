from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from .database import get_db_session

SessionDep = Annotated[AsyncSession, Depends(get_db_session)]
