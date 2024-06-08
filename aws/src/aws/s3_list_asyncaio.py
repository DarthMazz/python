import asyncio
import functools
import os

import boto3

BUCKET_NAME = 'ma2moto-bucket'

s3 = boto3.client('s3')

async def get_list():
    loop = asyncio.get_running_loop()
    bucket_contents = s3.list_objects_v2(Bucket=BUCKET_NAME)

    objects = await asyncio.gather(
        *[
            loop.run_in_executor(None, functools.partial(content_entry.get, Bucket=BUCKET_NAME, Key=content_entry['Key']))
            for content_entry in bucket_contents['Contents']
        ]
    )
    print(objects)

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_list())

if __name__ == '__main__':
    main()