from typing import AsyncGenerator, TYPE_CHECKING

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from config import settings

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncEngine


class DBHelper:
    def __init__(
        self,
        url: bool,
        echo: bool,
    ) -> None:
        self.engine: "AsyncEngine" = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


db_helper = DBHelper(
    url=settings.db.db_url,
    echo=settings.db.echo,
)
