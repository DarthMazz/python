import asyncio
from io import BytesIO
import aioboto3


async def s3_download(bucket_name:str, key: str) -> bytes:
    session = aioboto3.Session()
    async with session.client("s3") as s3:
        b = BytesIO()
        await s3.download_fileobj(bucket_name, key, b)
        return b.getvalue()


async def s3_list() -> list:
    s3_objects = []
    session = aioboto3.Session()
    async with session.resource("s3") as s3:
        bucket = await s3.Bucket('ma2moto-bucket')
        async for s3_object in bucket.objects.all():
            s3_objects.append(s3_object)
            print(s3_object)
    return s3_objects


async def upload(bucket_name:str, key: str, buf: bytes):
    b = BytesIO(buf)
    session = aioboto3.Session()
    async with session.client("s3") as s3:
        await s3.upload_fileobj(b, bucket_name, key)


async def main():
    s3_list_task = asyncio.create_task(s3_list())
    print(f's3_list_getting')
    res = await s3_list_task
    print(res)

    download_task = asyncio.create_task(s3_download('ma2moto-bucket', 'IMG_3436.jpg'))
    print(f's3_downloading')
    res = await download_task
    print(len(res))
    print(res[0])

    upload_task = asyncio.create_task(upload('ma2moto-bucket', 'IMG_3436.jpg', res))
    print(f's3_uploading')
    await upload_task

    print('finished')
    return 0


if __name__ == '__main__':
    res = asyncio.run(main())
    print(res)
