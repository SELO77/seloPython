import asyncio
import traceback
import timeit

import boto3

from datetime import *

start_time = timeit.default_timer()


def read_mailcontent():
  pass
  # with open() as f:

def read_clientlist():
  pass

def make_mailcontent():
  bodyhtml = u"""
  """
  return bodyhtml

def send_email():
  try:
    client = boto3.client('ses')
    bodyhtml = make_mailcontent()
    response = client.send_email(
      Source='noreply@traport.com',
      Destination={
        'ToAddresses': ['rochan87@gmail.com',]
      },
      Message={
        'Subject': {
          'Data': '트래포트 → 트래블하우 회원전환 적립금 안내',
          'Charset': 'UTF-8'
        },
        'Body': {
          'Html': {
            'Data': bodyhtml,
            'Charset': 'UTF-8'
          }
        }
      },
    )
    print("response:\n%s\n"%response)
  except:
    print(traceback.format_exc())


def write_result():
  pass


send_email()

duration = start_time - timeit.default_timer()
print("duration:%s"%duration)
