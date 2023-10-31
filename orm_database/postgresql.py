from base import BaseDatabase
import asyncpg

class Postgresql(BaseDatabase):
    async def start(self):
        self.db = await asyncpg.connect(host=self.host, user=self.user, password=self.password, database=self.database)

    async def insert_one(self, collection: str, value: dict):
        query = f"INSERT INTO {collection}  ( "
        filed_key = list(value.keys())
        for a in filed_key:
            query = query + " " + a + " " + ","
        query = query[:-1]
        query = query + ")"
        query = query + " VALUES ("
        filed_value = list(value.values())
        for a in filed_value:
            query = query + " '" + str(a) + "' " + ","
        query = query[:-1]
        query = query + ")"
        await self.db.execute(query)
        await self.db.close()

    async def insert_list(self, collection: str, values: list):
        for value in values:
            query = f"INSERT INTO {collection}  ( "
            filed_key = list(value.keys())
            for a in filed_key:
                query = query + " " + a + " " + ","
            query = query[:-1]
            query = query + ")"
            query = query + " VALUES ("

            filed_value = list(value.values())
            for a in filed_value:
                query = query + " '" + str(a) + "' " + ","
            query = query[:-1]
            query = query + ")"
            print(query)
            await self.db.execute(query)
            query = ""
        await self.db.close()

    async def create(self, collection: str, field: dict):
        query = f"CREATE TABLE {collection} ("
        filed_key = list(field.keys()0)
        for a in filed_key:
            query = query + a + " " + field[a] + " ,"
        query = query[:-1]
        query = query + ")"
        await self.db.execute(query)
        await self.db.close()




    # TODO : uncleaned below codes
    
    async def select_all(self, table: str, filed: list, all: bool = False):
        if all == True:
            query = "SELECT * FROM " + table
        if all == False:
            query = "SELECT "
            for a in filed:
                query = query + a + ","
            query = query[:-1]
            query = query + " FROM " + table

        print(query)
        stmt = await self.db.prepare(query)
        # for a in stmt:
        result = list(await stmt.fetch())
        data = {}
        data_row = []
        for a in result:
            conter = 0
            for b in a:
                data[filed[conter]] = b
                conter += 1
            data_row.append(dict(data))
        await self.db.close()
        print(data_row)
        return data_row

    async def select_columns(self, table: str, filed: dict):
        query = "SELECT * "
        query = query + " FROM "
        query = query + table + " WHERE "
        fileds = list(filed.keys())
        query = query + fileds[0]+"="+"$1"
        try:
            row = dict(await self.db.fetchrow(query, filed[fileds[0]]))
            return row
        except:
            return None
