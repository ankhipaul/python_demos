""" 
This is a demo to parse xml file, and convert it
to parquet file.
Databricks has a library just for that. Spark-xml is a
very cool library that makes parsing XML data so much easier using
spark SQL.
Spark-xml library : https://github.com/databricks/spark-xml

Loads Comments.xml XML as Parquet in HDFS

Downloaded the Stack Exchange Data Dump for this exercise. 
Placed the data of Comments.xml in HDFS and generated the parquet in HDFS.

Start pyspark with the command below and can test from the REPL -
  pyspark --packages com.databricks:spark-xml_2.10:0.4.1
Or run using
  spark2-submit --packages com.databricks:spark-xml_2.10:0.4.1 comments_xml_to_parquet.py

Written By: ANKHI PAUL
"""
import pyspark
import pyspark.sql
from pyspark.sql import SparkSession
import xml.etree.ElementTree as ET
import datetime


# extract the values in each xml row
def xmlfields(string):
    elements = ET.fromstring(string.encode('utf-8')).attrib
    
    comment_id = elements.get("Id")
    post_id = elements.get("PostId")
    score = elements.get("Score")
    creation_date = elements.get("CreationDate")
    user_id = elements.get("UserId")
    
    if comment_id is not None: 
        comment_id = int(comment_id)
    if post_id is not None: 
        post_id = int(post_id)        
    if score is not None: 
        score = int(score)        
    creation_date = datetime.datetime.strptime(creation_date[0:creation_date.find('.')],'%Y-%m-%dT%H:%M:%S')
    if user_id is not None: 
        user_id = int(user_id)    
    
    return (comment_id, post_id, score, creation_date, user_id)

def main():
    spark = SparkSession.builder.appName("CreateXMLtoParquet").getOrCreate() 
     
    xml_posts = spark.sparkContext.newAPIHadoopFile("/user/apaul/stackexchange/Comments.xml", 'com.databricks.spark.xml.XmlInputFormat', 'org.apache.hadoop.io.Text', 'org.apache.hadoop.io.Text', conf={'xmlinput.start': '<row', 'xmlinput.end': '/>'})
    each_comment = xml_posts.map(lambda x: x[1])
    comments_fields = each_comment.map(xmlfields)

    from pyspark.sql.types import *
    commentsSchema = \
    StructType([
    StructField("Id",IntegerType()),
    StructField("PostId",IntegerType()),
    StructField("Score",IntegerType()),
    StructField("CreationDate",TimestampType()),
    StructField("UserId",IntegerType())])

    postDF = spark.createDataFrame(comments_fields, schema=commentsSchema)

    postDF.write.save('/user/apaul/comments_parquet')

if __name__ == "__main__":
    main()
