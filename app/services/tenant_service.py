"""Tenant and bot CRUD operations."""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.tenant import Tenant
from app.models.bot import Bot


async def create_tenant(
    session: AsyncSession,
    slack_team_id: str,
    slack_team_name: str,
) -> Tenant:
    """Create a new tenant."""
    tenant = Tenant(
        slack_team_id=slack_team_id,
        slack_team_name=slack_team_name,
    )
    session.add(tenant)
    await session.commit()
    return tenant


async def get_tenant(
    session: AsyncSession,
    slack_team_id: str,
) -> Tenant:
    """Get tenant by Slack team ID."""
    result = await session.execute(
        select(Tenant).where(Tenant.slack_team_id == slack_team_id)
    )
    return result.scalars().first()


async def create_bot(
    session: AsyncSession,
    tenant_id: int,
    slug: str,
    token: str,
    signing_secret: str,
) -> Bot:
    """Create a new bot for a tenant."""
    bot = Bot(
        tenant_id=tenant_id,
        slug=slug,
        token=token,
        signing_secret=signing_secret,
    )
    session.add(bot)
    await session.commit()
    return bot
