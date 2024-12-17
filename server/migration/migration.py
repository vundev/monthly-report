from ..database.database import get_db_session
from ..app.service.service_schema import Service
from sqlalchemy.future import select


async def migrate_db():
    # TODO In the future migrate with alembic.
    async for session in get_db_session():
        result = await session.execute(select(Service))
        existing_services = result.scalars().all()
        if not existing_services:
            services = [
                Service(service_name="Web hosting"),
                Service(service_name="Netflix"),
                Service(service_name="Apple developer memebership")
            ]
            session.add_all(services)
            await session.commit()
