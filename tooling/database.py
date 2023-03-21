import redis
from django.conf import settings


conn = redis.Redis(host=settings.REDIS_HOST, port=6379, db=0)
