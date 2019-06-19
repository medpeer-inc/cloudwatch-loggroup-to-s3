import boto3
import datetime
import os
import time

s3_bucket_name = os.environ['S3_BUCKET_NAME']


def get_from_timestamp():
    today = datetime.date.today()
    yesterday = datetime.datetime.combine(today - datetime.timedelta(days=1),
                                          datetime.time(0, 0, 0))
    timestamp = time.mktime(yesterday.timetuple())
    return int(timestamp)


def get_to_timestamp(from_ts):
    return from_ts + (60 * 60 * 24) - 1


def trigger(event, context):
    from_ts = get_from_timestamp()
    to_ts = get_to_timestamp(from_ts)
    print('Timestamp: from_ts %s, to_ts %s' % (from_ts, to_ts))

    client = boto3.client('logs')

    log_group = os.environ['LOG_GROUP']
    s3_prefix = '%s/%s' % (log_group,
                           datetime.date.today() - datetime.timedelta(days=1))

    r = client.create_export_task(
        logGroupName=log_group,
        fromTime=from_ts * 1000,
        to=to_ts * 1000,
        destination=s3_bucket_name,
        destinationPrefix=s3_prefix
    )
    return r
