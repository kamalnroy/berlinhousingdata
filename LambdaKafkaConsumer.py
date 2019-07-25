import json
from kafka import KafkaConsumer
from __future__ import print_function
import json
import boto3
import time
import urllib
from pprint import pprint



#
# Extract the relevant data as per Data warehouse model and make entries into the data ware house tables
# TODO: Not completed yet; just need to call some sql library for this and call "SQL INSERT" queries.
#
def parse_apartment_data(apartment_data):

    # Step 1: Extract the city code, name, country and and make entry into the dimension table "dim_city" if the corrsponding entry is  not there
    realEstate_address_city = apartment_data['realEstate_address_city']
    realEstate_address_geoHierarchy_country_name = apartment_data['realEstate_address_geoHierarchy_country_name']

    # Step 2: Extract the region code, region name, city and make entry into the dimension table "dim_region" if the corrsponding entry is  not there
    # Also make sure that there is a refrential integrity with "dim_city"

    # Step 3: Extract the real estate agency details and make entry into the dimension table "dim_agency" if the corrsponding entry is  not there
    # Also Also make sure that there is a refrential integrity with "dim_region"
    contactDetails_id = apartment_data['contactDetails_id']
    contactDetails_address_city = apartment_data['contactDetails_address_city']
    contactDetails_countryCode = apartment_data['contactDetails_countryCode']
    contactDetails_phoneNumber = apartment_data['contactDetails_phoneNumber']
    contactDetails_email = apartment_data['contactDetails_email']
    contactDetails_faxNumber = apartment_data['contactDetails_faxNumber']
    contactDetails_firstname = apartment_data['contactDetails_firstname']

    # Step 4: Extract the apartment details such as apartment_id, address, floor no. and all other details as per the Data warehouse model and make entry
    # into the table "fact_flat";
    # Also make sure that the refernetial integrity is maintained with tables "dim_agency" and "dim_region"
    


#
# TODO: Need to put the Kafka consumer in a consumer group
# TODO: Start reading only from the location where it was left off last time when the function was triggred
#
def consume_kafka_messages():
    print("consume_kafka_topics called")
    parsed_topic_name = 'test'
    # Notify if a recipe has more than 200 calories

    consumer = KafkaConsumer(parsed_topic_name, auto_offset_reset='earliest', enable_auto_commit=True, bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000)
    for msg in consumer:
		# TODO: do some error handling here i.e. if the message is the right one or not.
		#print("loaded json is:", loaded_json)
		loaded_json = json.loads(msg.value)
		#decoded = json.loads(json_input)
		print (json.dumps(loaded_json, sort_keys=True, indent=4))
		#print("loaded json is:", loaded_json)
		print(loaded_json['ok'])
		parse_apartment_data(loaded_json['data'])

    consumer.close()

#
# This function is triggered every hour by "CloudWatch" cron event e.g. Schedule expression: cron(0/1 * 1/1 * ? *)
#
def lambda_handler(event, context):
    # TODO implement
    print("This function gets triggred every minute")
    consume_kafka_topics()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

