import redis
import json
from flask import current_app
from .models import Transaction

def get_transactions(user_id):
    r = redis.from_url(current_app.config["REDIS_URL"])
    cache_key = f"user:{user_id}"

    cached = r.get(cache_key)
    if cached:
        return json.loads(cached)

    transactions = Transaction.query.filter_by(user_id=user_id).all()

    result = [
        {"id": t.id, "amount": t.amount, "status": t.status}
        for t in transactions
    ]

    r.setex(cache_key, 300, json.dumps(result))
    return result
