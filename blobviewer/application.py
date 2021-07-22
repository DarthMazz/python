from bottle import Bottle, template
from azure.storage.blob import BlobServiceClient
from azure.storage.blob import ResourceTypes, AccountSasPermissions, generate_account_sas
from datetime import datetime, timedelta

app = Bottle()


@app.route("/")
def root():
    connect_str = 'DefaultEndpointsProtocol=https;AccountName=ma2moto;AccountKey=wK9QsxpEqSPs/ZWUIRwM2/CzcjP7Nz6/B7V9IwWRCl5/BDc1DLMGt76vBcrSEEVeDuNuiWEifYLOHwU0f5Mbmw==;EndpointSuffix=core.windows.net'
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client("ma2container")
    blob_list = container_client.list_blobs()

    sas_url = generate_account_sas(
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
        blob_prop['url'] = f'https://ma2moto.blob.core.windows.net/ma2container/{blob_prop["name"]}?{sas_url}'
        blobs.append(blob_prop)

    return template('main', blobs=blobs)



def main():
    app.run(host="0.0.0.0", port=5000, reloader=True, debug=True)


if __name__ == '__main__':
    main()