from enum import Enum


class TicketType(str, Enum):
    CALL = "call"
    CHAT = "chat"
    EMAIL = "email"
    FB_MESSENGER = "fb_messenger"
    INSTAGRAM_DM = "instagram_dm"
    PHONE = "phone"
    SMS = "sms"
    TWITTER = "twitter"
    TWITTER_DM = "twitter_dm"
    WEB = "web"
    WHATSAPP = "whatsapp"

    def __str__(self) -> str:
        return str(self.value)
