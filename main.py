#!/usr/bin/env python3

from string import Template

import random
import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1000)))
   p = math.pow(1000, i)
   s = round(size_bytes / p, 2)
   return f"{int(s)}{size_name[i]}"


def generate_users_number(size=None):
  """
  Takes parameter 'size'
  Tiny: Used for questions where instead of users we have producers.
  Small: Returns users in the range of 1 and 20 million
  Large: Returns users in the range of 100 to 500 million
  """

  tiny = int(round(math.ceil(random.randint(100, 1000) / 100) * 100))
  small = int(round(math.ceil(random.randint(1, 20) / 10) * 10) * 1E6)
  big = int(round(random.randint(100, 500),-2) * 1E6)

  if size == "big":
    return big
  elif size == "small":
    return small
  elif size == "tiny":
    return tiny

  return random.choice([small, big])

def generate_requests_per_day():
  # Returns a random number of requests per user
  return random.randint(1,10)

def generate_data_retention():
  # Returns a random choice in years
  return random.choice([1, 3, 5])

def generate_qps_size():
  # Returns a random number of QPS
  return int(random.randint(1, 20) * 1E6)


def generate_data_size(size=None):
  # Returns a tuple with a value in int and bytes
  tiny = int(round(math.ceil(random.randint(100, 5000) / 1000) * 100))
  small = int(round(math.ceil(random.randint(1, 20) / 10) * 10) * 1E6)
  big = int(round(random.randint(100, 500),-2) * 1E6)

  if size == "big":
    return tuple([big, convert_size(big)])
  elif size == "small":
    return tuple([small, convert_size(small)])
  elif size == "tiny":
    return tuple([tiny, convert_size(tiny)])

  if size is None:
    select = random.choice([small, big])
    return tuple([select, convert_size(select)])

def generate_question(question=None):

  if question is None:
    select = random.choice(list(questions.keys()))
    ask = questions.get(select)
    print(ask["template"].substitute(**ask))

    return ask
  
  if question:
    ask = questions.get(question)
    print(ask["template"].substitute(**ask))

  return questions.get(question)

questions = {
  1: {
    "ask": "Calculate the approximate QPS and throughput",
    "template": Template("Ask: $ask \nUsers: $users \nRequests: $requests \nData: $data"),
    "users": generate_users_number("small"),
    "requests": generate_requests_per_day(),
    "data": generate_data_size(),
    },
  2: {
    "ask": "Caculate the throughput required",
    "template": Template("Ask: $ask \nUsers: $users \nRequests: $requests \nData: $data"),
    "users": generate_users_number("big"),
    "requests": generate_requests_per_day(),
    "data": generate_data_size(size="tiny"),
  },
  3: {
    "ask": "Calculate the storage requirements",
    "template": Template("Ask: $ask \nUsers: $users \nRequests: $requests \nData: $data"),
    "users": generate_users_number(),
    "requests": generate_requests_per_day(),
    "data": generate_data_size("tiny"),
    "retention": generate_data_retention(),
  }

}

if __name__ == '__main__':
  generate_question()