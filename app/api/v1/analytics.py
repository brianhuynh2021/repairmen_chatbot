from fastapi import APIRouter, Depends, Query
from sqlalchemy import func, select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session_async import get_session
from app.models.chat_logs_model import ChatLog
from app.schemas.analytics_schema import AnalyticsSummary, ChatLogItem

router = APIRouter()

@router.get("/analytics/summary", response_model=AnalyticsSummary)
async def summary(db: AsyncSession = Depends(get_session)) -> AnalyticsSummary:
    total = (await db.execute(select(func.count(ChatLog.id)))).scalar() or 0
    users = (await db.execute(select(func.count(func.distinct(ChatLog.user_id))))).scalar() or 0
    avg = (await db.execute(select(func.avg(ChatLog.response_time_ms)))).scalar()
    return AnalyticsSummary(
        total_messages=total,
        distinct_users=users,
        avg_response_time_ms=float(avg) if avg is not None else None,
    )

@router.get("/analytics/recent", response_model=list[ChatLogItem])
async def recent(
    limit: int = Query(50, ge=1, le=200),
        db: AsyncSession = Depends(get_session),
    ) -> list[ChatLogItem]:
        q = select(ChatLog).order_by(desc(ChatLog.timestamp)).limit(limit)
        rows = (await db.execute(q)).scalars().all()
        return rows