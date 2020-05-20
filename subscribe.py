import asyncio
from datetime import datetime
from graphene import ObjectType, String, Schema, Field


# All schema require a query.
class Query(ObjectType):
    hello = String()

    def resolve_hello(root, info):
        return 'Hello, world!'


class Subscription(ObjectType):
    time_of_day = Field(String)

    async def subscribe_time_of_day(root, info):
        try:
            count = 0
            while count < 10:
                yield {'time_of_day': datetime.now().isoformat()}
                await asyncio.sleep(1)
                count += 1
        except Exception as error:
            print(error)


SCHEMA = Schema(query=Query, subscription=Subscription)


async def subscribe(schema):
    subscription = 'subscription { timeOfDay }'
    result = await schema.subscribe(subscription)
    async for item in result:
        print(item.data['timeOfDay'])

asyncio.run(subscribe(SCHEMA))
