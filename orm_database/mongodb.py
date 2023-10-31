from base import BaseDatabase
import motor.motor_asyncio

class Mongodb(BaseDatabase):
    async def start(self):
        self.clint = motor.motor_asyncio.AsyncIOMotorClient(self.url)
        self.database = self.clint[str(self.name)]

    async def insert_one(self, collection: str, value: dict,):
        coll = self.database[collection]
        await coll.insert_one(data)
        return data

    async def insert_list(self, collection: str, values: list):
        for value in values:
            await self.insert_one(collection, value)

    async def create(self, collection: str, field: dict):
        pass

   async def find_one(self, data: dict, collection: str):
        coll = self.database[collection]
        result = await coll.find_one(data)
        if (result == None):
            return result
        else:
            result['_id'] = str(result["_id"])
            return result

    # TODO : uncleaned below codes

    async def find(self, data: dict, collection: str):
        coll = self.database[collection]
        result = coll.find(data)
        arraydata = []
        async for a in result:
            a['_id'] = str(a['_id'])
            arraydata.append(a)
        return arraydata

    async def read_collection(self, collection: str):
        coll = self.database[collection]
        data = coll.find({})
        arraydata = []
        async for a in data:
            a['_id'] = str(a['_id'])
            arraydata.append(a)
        return arraydata

    async def replace_one(self, find_data: dict, replace_data: dict, collection: str):
        coll = self.database[collection]
        data = await coll.replace_one(find_data, replace_data)
        if data == None:
            return None
        else:
            return data

    async def update_one(self, find_data: dict, replace_data: dict, collection: str):
        coll = self.database[collection]
        data = await coll.update_one(find_data, {'$set': replace_data})
        if data == None:
            return None
        else:
            return data

    async def edit_one(self,find_data:dict,edit_data:dict,collection:str):
        coll = self.database[collection]
        result = await coll.find_one(find_data)
        if (result == None):
            return False
        else:
            result['_id'] = str(result["_id"])
            result.update(edit_data)
            data = await coll.replace_one(find_data, edit_data)
            return True
            
    async def delete_one(self, find: dict, collection: str):
        coll = self.database[collection]
        result = coll.delete_one(find)
        print(result)