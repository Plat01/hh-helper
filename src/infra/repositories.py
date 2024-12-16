from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from src.domain.entities import User


T = TypeVar("T")

class AbstractRepository(ABC, Generic[T]):
    
    @abstractmethod
    async def get_by_id(self, id: int) -> T | None:
        """Fetch a single record by its ID."""
        ...

    @abstractmethod
    async def get_all(self) -> list[T]:
        """Fetch all records."""
        ...

    @abstractmethod
    async def add(self, item: T) -> T:
        """Add a new record."""
        ...

    @abstractmethod
    async def update(self, item: T) -> T:
        """Update an existing record."""
        ...
    
    @abstractmethod
    async def delete(self, id: int) -> None:
        """Delete a record by its ID."""
        ...

class UserRepository(AbstractRepository[User]):

    @staticmethod
    async def get_by_id(session: AsyncSession, user_id: int) -> User:
        """Get user by id from database

        Args:
            user_id (int): _description_

        Returns:
            User: _description_
        """
        result = await session.db_session.execute(select(User).where(User.id == id))
        return result.scalar_one_or_none()
    
    async def add(session: AsyncSession, entity: User) -> User:
        """Add a new user to the database."""
        session.db_session.add(entity)
        await session.db_session.commit()
        await session.db_session.refresh(entity)
        return entity
    
    async def update(session: AsyncSession, entity: User) -> User:
        """Update an existing user."""
        await session.db_session.merge(entity)
        await session.db_session.commit()
        return entity

    async def delete(session: AsyncSession, id: int) -> None:
        """Delete a user by its ID."""
        user = await session.get_by_id(id)
        if user:
            await session.db_session.delete(user)
            await session.db_session.commit()