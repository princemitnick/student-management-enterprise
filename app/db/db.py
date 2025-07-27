from motor.motor_asyncio import AsyncIOMotorClient

def get_mongo_client() -> AsyncIOMotorClient:
    return AsyncIOMotorClient()