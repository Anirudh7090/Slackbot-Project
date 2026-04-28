"""Slack event payload schemas."""
from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class SlackEvent(BaseModel):
    """Base Slack event."""

    type: str
    challenge: Optional[str] = None


class SlackMessage(BaseModel):
    """Slack message event."""

    type: str
    user: Optional[str]
    channel: str
    text: str
    ts: str


class SlackSlashCommand(BaseModel):
    """Slack slash command payload."""

    token: str
    team_id: str
    team_domain: str
    channel_id: str
    channel_name: str
    user_id: str
    user_name: str
    command: str
    text: str
    response_url: str
    trigger_id: str
