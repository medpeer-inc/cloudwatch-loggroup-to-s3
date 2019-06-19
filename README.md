# cloudwatch-loggroup-to-s3

## What's this project

This project provides an AWS Lambda application that created and deployed by Serverless Framework for the following purpose:

- Daily Exporting of AWS CloudWatch Logs to S3


The [Serverless framework](https://serverless.com/) simplifies the process of building and maintaining Lambda applications.


## Project Components

* An AWS Lambda function
* A S3 Bucket for saving CloudWatch Logs


## Step by step

### Install Serverless framework

```bash
$ npm install -g serverless
```


### Configure AWS profile


```bash
$ aws configure --profile <profile>
```


## Deploy

* hoge
```bash
$ AWS_PROFILE=hoge sls deploy --stage app
$ AWS_PROFILE=hoge sls deploy --stage admin
```

* moge
```bash
$ AWS_PROFILE=moge sls deploy --stage app
$ AWS_PROFILE=moge sls deploy --stage api
```


## How to add new AWS Account

```
custom:
  environemnt:
    ...
    new_profile:
      stage_name:
        S3_BUCKET_NAME: example.bucket.name
        LOG_GROUP: example/log/group
```


## How to export multiple LogGroups just by using a single lambda function ?

No. You only can specify to export 1 CloudWatch Logs per a Lambda function because of Lambda restrictions.


## S3 Bucket Policy

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "",
            "Effect": "Allow",
            "Principal": {
                "Service": "logs.<region>.amazonaws.com"
            },
            "Action": "s3:GetBucketAcl",
            "Resource": "arn:aws:s3:::<bucket name>"
        },
        {
            "Sid": "",
            "Effect": "Allow",
            "Principal": {
                "Service": "logs.<region>.amazonaws.com"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::<bucket name>/*",
            "Condition": {
                "StringEquals": {
                    "s3:x-amz-acl": "bucket-owner-full-control"
                }
            }
        }
    ]
}
```

## Reference

https://serverless.com/framework/docs/providers/aws/guide/installation/
https://serverless.com/framework/docs/providers/aws/guide/quick-start/

## In the production
- [cloudwatch-loggroup-to-s3](https://github.com/medpeer-dev/cloudwatch-loggroup-to-s3) is using this tool in many productions.

## License

MIT License

Copyright (c) 2019~ MedPeer, Inc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
