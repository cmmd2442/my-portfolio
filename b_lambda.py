import boto3
from botocore.client import Config
import io
import zipfile
import mimetypes


def lambda_handler(event, context):
    
    #print("printing event from line 8 event = " + str(event))

    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-1:462554666803:deployPortfolioTopic')



    job = event.get("CodePipeline.job") 


    print("line 20 job = " + str(job["data"]["inputArtifacts"][0]["name"]))
    print("line 46 job = " + str(job["data"]["inputArtifacts"][0]["location"]["s3Location"]))
    print("line 47 job = " + str(job["data"]["inputArtifacts"][0]["location"]["s3Location"]['bucketName'])) 
    print("line 48 job = " + str(job["data"]["inputArtifacts"][0]["location"]["s3Location"]['objectKey']))

    name = job["data"]["inputArtifacts"][0]["name"]
    bucketName = job["data"]["inputArtifacts"][0]["location"]["s3Location"]['bucketName']
    objectKey = job["data"]["inputArtifacts"][0]["location"]["s3Location"]['objectKey']
   
    try:
        
        if job:
            print ("if job line 32")
            for artifact in job["data"]["inputArtifacts"]:
                if job["data"]["inputArtifacts"][0]["name"] == "myApp":
                    #location = job["data"]["inputArtifacts"]["name"]["location"]["s3Location"]
                    bucketName = job["data"]["inputArtifacts"][0]["location"]["s3Location"]['bucketName']
                    objectKey = job["data"]["inputArtifacts"][0]["location"]["s3Location"]['objectKey']
                    print("objectKey from line 38 = " + str(objectKey))

        """
        job = event.get("CodePipeline.job")
        print ("Building portfolio from " + str(job))
        
        if job:
            #print (job)
            for artifact in job["data"]["inputArtifacts"]:
                if artifact["name"] == "MyApp":
                    location = artifact["location"]["s3Location"]
                    print("location from line 31 = " + str(location))
        """
        s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))

        portfolio_bucket = s3.Bucket('portfolio.lehighcampusrentals.com')
        #build_bucket = s3.Bucket(location["bucketName"])
        build_bucket = s3.Bucket(bucketName)
        portfolio_zip = io.BytesIO()
        print("build_bucket is == " + str(build_bucket))
        #build_bucket.download_fileobj(location["objectKey"], portfolio_zip)
        build_bucket.download_fileobj(objectKey, portfolio_zip)
#         build_bucket.download_fileobj(location["objectKey"], ())
#         portfolio_zip = io.StringIO(location[objectKey"])

        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm, ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')

        print ("Job done!")
        topic.publish(Subject="Portfolio Deployed", Message="Portfolio deployed successfully!")
        if job:
            codepipeline = boto3.client('codepipeline')
            codepipeline.put_job_success_result(jobId=job['id'])
    except:
        topic.publish(Subject="Portfolio Deploy Failed", Message="The Portfolio was not deployed successfully")
        raise

    return 'Hello from Lambda'

