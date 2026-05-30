"""Tenant = a Slack workspace we serve."""

from app.models.bot import Bot
from sqlalchemy import Boolean, String, false
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class Tenant(Base, TimestampMixin):
    __tablename__ = "tenants"

    id: Mapped[int] = mapped_column(primary_key=True)

    # Human-friendly slug like 'prj-sk' — used in logs and URLs
    slug: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)

    # Display name like 'PRJ-SK'
    name: Mapped[str] = mapped_column(String(128), nullable=False)

    # Slack workspace id, e.g. 'T0ASYAWBD3Q'. This is what Slack sends in
    # every event payload — we use it to look up which tenant the request
    # belongs to.
    slack_team_id: Mapped[str] = mapped_column(
        String(32), unique=True, index=True, nullable=False
    )

    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)

    access_control_enabled: Mapped[bool] = mapped_column(
        Boolean, default=False, server_default=false(), nullable=False
    )

    # Children
    bots: Mapped[list["Bot"]] = relationship(  # noqa: F821
        back_populates="tenant", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Tenant {self.slug} ({self.slack_team_id})>"