from fastapi import APIRouter
from app.api.model.bring_models import BringOrder
from app.api.worker.bring_celery_worker import create_bring_label

bring = APIRouter()


@bring.post('/label')
async def create_label(bring_order: BringOrder):
    create_bring_label.delay(bring_order.order_id)
    return {"message": "Order received"}
