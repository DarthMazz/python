from bottle import Bottle, template
from azure.storage.blob import BlobServiceClient
from azure.storage.blob import ResourceTypes, AccountSasPermissions, generate_account_sas
from datetime import datetime, timedelta
import os


# Reference
# https://docs.microsoft.com/ja-jp/azure/storage/blobs/storage-quickstart-blobs-python
# https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob/samples


app = Bottle()


@app.route("/")
def root():

    # アクセスキー取得（OS環境設定より取得。アクセスキーをコードに記載するとGitHubで警告される）
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    # BLOBクライアント生成（アクセスキー）
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    # コンテナクライアント生成
    container_client = blob_service_client.get_container_client("ma2container")
    # BLOBリスト取得
    blob_list = container_client.list_blobs(name_starts_with='ma2')
    # SASキー生成（アクセスキーより１時間の制限でアクセスキーを生成）
    saskey = generate_account_sas(
            blob_service_client.account_name,
            account_key=blob_service_client.credential.account_key,
            resource_types=ResourceTypes(object=True),
            permission=AccountSasPermissions(read=True),
            expiry=datetime.utcnow() + timedelta(hours=1)
    )
    blobs = list()
    for blob in blob_list:
        blob_prop = dict()
        blob_prop['name'] = blob['name']
        # BLOBにアクセスするためのURLを生成（BLOBのURL＋SASキー）
        blob_prop['url'] = f'https://ma2moto.blob.core.windows.net/ma2container/{blob_prop["name"]}?{saskey}'
        blobs.append(blob_prop)

    return template('main', blobs=blobs)


def main():
    app.run(host="0.0.0.0", port=5000, reloader=True, debug=True)


if __name__ == '__main__':
    main()