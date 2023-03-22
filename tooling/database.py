import logging
import redis

logger = logging.getLogger("[Tooling/database]")

try:
    logger.info("Connecting to Redis...")
    conn = redis.Redis(host="localhost", port=6379, db=0)
    logger.info("Connected to Redis")
except Exception as e:
    logger.error(f"Error connecting to Redis: {e}")
