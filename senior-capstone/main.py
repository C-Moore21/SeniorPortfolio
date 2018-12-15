from flask import Flask, render_template, Response, request, redirect, url_for, jsonify, g
from boto3.dynamodb.conditions import Key
from dynamodb_json import json_util as dynamodb_json
import json
import boto3


# initializing app
app = Flask(__name__)


def session():
    """
    Get a boto3 session.
    Returns:
        (object) boto3 session
    """
    # uncomment session below for custom confurting your own AWS boto3 session
    # session = boto3.Session(aws_access_key_id="n/a",
    #                             aws_secret_access_key="n/a", region_name="us-east-2")
    session = boto3.Session()
    return session


def generate_url(s3, bucket_name, key_name):
    """
    Generate URL for s3 bucket hosting geojson data.
    Args:
        s3: (object) A s3 client session.
        bucket_name: (string) Name of the bucket containing the desired data.
        key_name: (string) Name of the object you want a presigned url for
    Returns:
        (object) s3 url
    """
    url = s3.generate_presigned_url('get_object', Params={
                                    'Bucket': bucket_name, 'Key': key_name}, ExpiresIn=600)
    return url


def get_newest_object(s3, bucket_name):
    """
    Obtain latest object in specified s3 bucket.
    Args:
        s3: (object) A s3 client session.
        bucket_name: (string) Name of the bucket containing the desired data.
    Returns:
        (object) s3 url
    """
    def get_last_modified(obj): return int(obj['LastModified'].strftime('%s'))
    objs = s3.list_objects_v2(Bucket=bucket_name)['Contents']
    last_added = [obj['Key'] for obj in sorted(objs, key=get_last_modified)][0]
    return last_added


def s3_scan(account_session):
    """
    Scans S3 for corresponding bucket.
    Args:
        account_session: (string) boto3 session of the AWS Account containing desired data.
    Returns:
        (object) s3 url
    """
    s3 = account_session.client('s3')
    bucket_name = 'senior-project-geo-json'
    url = generate_url(s3, bucket_name, get_newest_object(
        s3, bucket_name))
    return url


@app.route('/')
def home():
    """
    Render the index page.
    Returns:
        object template
    """
    geo_json = get_geojosn()
    return render_template('index.html', data=geo_json)


@app.route('/_get_geojson', methods=['POST', 'GET'])
def get_geojosn():
    """
    Obtain most up to date geojson for representation on the map.
    Returns:
        object JSON
    """
    return_list = []
    account_session = session()
    url = s3_scan(account_session)
    return json.dumps(url)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)
