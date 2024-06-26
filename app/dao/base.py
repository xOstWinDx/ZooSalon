from sqlalchemy import select, insert, update, delete

from app.database import get_async_session


class BaseDAO:
    model = None

    @classmethod
    async def fetch_one_or_none(cls, **filter_by):
        async with get_async_session() as session:
            result = await session.execute(select(cls.model).filter_by(**filter_by))
            result = result.scalar_one_or_none()
        return result

    @classmethod
    async def fetch_all(cls, **filter_by):
        async with get_async_session() as session:
            result = await session.execute(select(cls.model).filter_by(**filter_by))
            result = result.mappings().all()
        return result

    @classmethod
    async def add(cls, **data) -> model:
        async with get_async_session() as session:
            result = await session.execute(
                insert(cls.model).values(**data).returning(cls.model)
            )
            result = result.scalar_one_or_none()
            await session.commit()
        return result

    @classmethod
    async def delete(cls, **filter_by) -> model:
        async with get_async_session() as session:
            result = await session.execute(delete(cls.model).filter_by(**filter_by))
            result = result.rowcount
            await session.commit()
        return result

    @classmethod
    async def update(cls, item_id, **values) -> model:
        async with get_async_session() as session:
            result = await session.execute(
                update(cls.model).values(**values).filter_by(id=item_id)
            )
            result = result.rowcount
            await session.commit()
        return result

    @classmethod
    async def get_all_ids(cls):
        async with get_async_session() as session:
            res = await session.execute(select(cls.model.id))
            res = res.scalars().all()
            return res
