import boto3


def logging_info(message:str):
    print(message)


def s3_download(s3_object):
        logging_info(f'downloading {s3_object.bucket_name}, {s3_object.key}')
        body = s3_object.get()['Body'].read()
        logging_info(f'downloaded {s3_object.bucket_name}, {s3_object.key}, {len(body)} byte')


def main():
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(f'ma2moto-bucket')

    s3_objects = list(bucket.objects.all())

    for s3_object in s3_objects:
        s3_download(s3_object)



if __name__ == '__main__':
    main()