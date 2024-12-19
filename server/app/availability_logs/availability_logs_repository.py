from server.database.dependency import SessionDep
from .availability_logs_schema import AvailabilityLogs
from datetime import datetime
from .availability_logs_model import AvailabilityLevel


class AvailabilityLogsRepository:
    def __init__(self, session: SessionDep):
        self.session = session

    async def crete_log_message(self, tenant_id: int, level: AvailabilityLevel):
        log_message = AvailabilityLogs(
            tenant_id=tenant_id,
            availability_level=level,
            log_date=datetime.now())

        self.session.add(log_message)
        await self.session.commit()
        await self.session.refresh(log_message)
        return log_message
