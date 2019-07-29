# MVP solution

### Limitation(s):
- This is not a full working solution and just a blueprint of the solution. There is a lot of scope for improvement, which I can explain during the interview.
- I have executed the entire pipeline (other than the python code. The python code was very simple, but quite time consuming, hence I just added added alogorithmic steps.)
### Assumptions:
1. We already have a component called producer(s) that publishes "berlin housing data" json objects into a Kafka Topic.

### Description of components:
**1. A Kafka cluster:**
- A kafka cluster is running that has a topic into which the berlin housing data would be published by the producer(s).  
- I have chosen this solution because persistence is offered out of the box.
- We could also have chosen AWS S3 or Managed Streaming Kafka(MSK) or Kinesis offered by AWS.

**2. Time-triggered Lambda consumer**
- This is a lambda function (written in python) that would be triggered every hour (configurable via Schedule expression: cron(0/1 * 1/1 * ? *)). 
- This function will read data from Kafka topic, parse the messages and push the data into the Redshift cluster. (Definion Filename: [LambdaKafkaConsumer.py](https://github.com/kamalnroy/berlinhousingdata/blob/master/LambdaKafkaConsumer.py "LambdaKafkaConsumer.py"))
- Limitations: The code file just contains a blue print of the solution in the form of algorithm

**3. AWS redshift cluster **
- This is a managed datawarehouse solution offered by AWS. 
- (Other options: Snowflake; we can also design a datawarehouse inside an RDMBS such as PostGreSQL or MySQL)

**4. GetApartments Lambda function **
- This function will serve the analysts by querying data from the datawarehouse, depending on the user queries. (Definiton file name: [GetAvailableApartments.py](https://github.com/kamalnroy/berlinhousingdata/blob/master/GetAvailableApartments.py "GetAvailableApartments.py") )
- The code file just contains a blue print of the solution in the form of algorithm.

**5. Lambda Proxy API**
- This is a proxy API for the lambda function "GetApartments", as mentioned in (4.). This API can be called via HTTP get/post requests.

##DataWarehouse schema
- I designed this using MySQL Workebench. Filename is [https://github.com/kamalnroy/berlinhousingdata/blob/master/berlin_housing_dw_model.mwb](https://github.com/kamalnroy/berlinhousingdata/blob/master/berlin_housing_dw_model.mwb)
- A pictorial format is there too https://github.com/kamalnroy/berlinhousingdata/blob/master/berlin_housing_dw_model.png
- This is a hybrid schema (mix of star and snowflake)
- Limitations: All the fields and their types are not there in the schema yet, but gives an idea of the solution

