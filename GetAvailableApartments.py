from __future__ import division

def lambda_handler(event, context):
   # Step 1 - read the query strings provided by the user
   # Following are some of the possible filters that may be provided by the end-user
   # TODO: error checks; also check if the uqery strings are provided or not.
   post_code = event['queryStringParameters']['post_code']
   city = event['queryStringParameters']['city']
   min_rent = event['queryStringParameters']['min_rent']
   max_rent = event['queryStringParameters']['max_rent']
   # TODO: more filters
   
   # Step 2: depending upon the above filters, form a SQL query and fetch the data from the redshift cluster
   # Make sure that only "required dimensions" values are returned to the end-user
   
   # Step 3: Form a json string of the results received in Step 2 and return to the user.
   
  