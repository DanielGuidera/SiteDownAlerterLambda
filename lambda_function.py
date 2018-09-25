import boto3
import requests
import os

def lambda_handler(event, context):
   websiteList = ["http://n4g.com/","https://www.youtube.com/","https://pages.github.com/", "http://down.pogo.com/"]
   for site in websiteList:
      response = requests.get(site)
      if response.status_code != 200:
         pushAlert(str(response.status_code), site)
   
def pushAlert(responseCode, siteUrl):
   print("Url: " + siteUrl + " has returned a status code of " + responseCode)
   client = boto3.client("sns", aws_access_key_id=os.environ["access_key"], aws_secret_access_key=os.environ["secret_access_key"], region_name=os.environ["region"])
   client.publish(Message="Url: " + siteUrl + " has returned a status code of " + responseCode, TopicArn=os.environ["topicArn"])
