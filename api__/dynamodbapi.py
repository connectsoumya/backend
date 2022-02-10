import boto3
from botocore.config import Config

proxy_definitions = {
    'http': 'http://proxy.amazon.com:6502',
    'https': 'https://proxy.amazon.org:2010'
}

my_config = Config(
    region_name='us-east-2',
    signature_version='v4',
    proxies=proxy_definitions
)

client = boto3.client('dynamodb', config=my_config)

def get_item(tablename, key):
    pass

