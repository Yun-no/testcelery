from pydantic import BaseModel


class BringOrder(BaseModel):
    order_id: str | None = None
    order_name: str | None = None
