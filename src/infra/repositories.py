from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from src.domain.entities import User


T = TypeVar("T")

class AbstractRepository(ABC, Generic[T]):
    
    @staticmethod
    @abstractmethod
    async def get_by_id(session: AsyncSession, id: int) -> T | None:
        """Fetch a single record by its ID."""
        ...

    @staticmethod
    @abstractmethod
    async def get_all(session: AsyncSession) -> list[T]:
        """Fetch all records."""
        ...

    @staticmethod
    @abstractmethod
    async def add(session: AsyncSession, item: T) -> T:
        """Add a new record."""
        ...

    @staticmethod
    @abstractmethod
    async def update(session: AsyncSession, item: T) -> T:
        """Update an existing record."""
        ...

    @staticmethod  
    @abstractmethod
    async def delete(session: AsyncSession, id: int) -> None:
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
        result = await session.db_session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()
    
    @staticmethod
    async def add(session: AsyncSession, entity: User) -> User:
        """Add a new user to the database."""
        session.db_session.add(entity)
        await session.db_session.commit()
        await session.db_session.refresh(entity)
        return entity
    
    @staticmethod
    async def update(session: AsyncSession, entity: User) -> User:
        """Update an existing user."""
        await session.db_session.merge(entity)
        await session.db_session.commit()
        return entity

    @staticmethod
    async def delete(session: AsyncSession, id: int) -> None:
        """Delete a user by its ID."""
        user = await session.get_by_id(session, id)
        if user:
            await session.db_session.delete(user)
            await session.db_session.commit()