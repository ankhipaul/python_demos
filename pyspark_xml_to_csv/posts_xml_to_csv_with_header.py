"""
This is a demo to parse xml file, and convert it to csv file.

I have used Databricks libraries for that. Spark-xml is a
very cool library that makes parsing XML data so much easier using
spark SQL.
Spark-xml library : https://github.com/databricks/spark-xml
Spark-csv linbrary : https://github.com/databricks/spark-csv

Loads Posts.xml as csv in HDFS.

Downloaded the Stack Exchange Data Dump for this exercise. 

Placed the data of Posts.xml in HDFS and generated the csv ourput file in HDFS.

Start pyspark with the command below and can test from the REPL -
  pyspark --packages com.databricks:spark-xml_2.10:0.4.1,com.databricks:spark-csv_2.10:1.5.0 
Or run using
  spark2-submit --packages com.databricks:spark-xml_2.10:0.4.1,com.databricks:spark-csv_2.10:1.5.0 posts_xml_to_csv_with_header.py

Written By: ANKHI PAUL
"""
import pyspark
import pyspark.sql
from pyspark.sql import SparkSession
import xml.etree.ElementTree as ET
import re



# extract the values in each xml row
def xmlfields(string):
    elements = ET.fromstring(string.encode('utf-8')).attrib
    
    postId = elements.get("Id")
    postType = elements.get("PostTypeId")
    acceptedanswerid = elements.get("AcceptedAnswerId")
    creationdate = elements.get("CreationDate")
    score = elements.get("Score")
    viewCount = elements.get("ViewCount")
    owneruserid = elements.get("OwnerUserId")
    lasteditoruserid = elements.get("LastEditorUserId")
    lasteditdate = elements.get("LastEditDate")
    title = elements.get("Title")
    lastactivitydate = elements.get("LastActivityDate")
    tags = re.findall(r'[\w.-]+', elements.get("Tags", ""))
    answercount = elements.get("AnswerCount")
    commentcount = elements.get("CommentCount")
    favoritecount = elements.get("FavoriteCount")
    
    if lasteditdate == None:
        lasteditdate = creationdate
    
    return (postId, postType, acceptedanswerid, creationdate, score, viewCount, owneruserid, lasteditoruserid, lasteditdate, title, lastactivitydate, tags, answercount, commentcount, favoritecount)

def main():
    spark = SparkSession.builder.appName("CreatePostsCSVWithHeader").getOrCreate() 
     
    xml_posts = spark.sparkContext.newAPIHadoopFile("/user/apaul/stackexchange/Posts.xml", 'com.databricks.spark.xml.XmlInputFormat', 'org.apache.hadoop.io.Text', 'org.apache.hadoop.io.Text', conf={'xmlinput.start': '<row', 'xmlinput.end': '/>'})
    each_post = xml_posts.map(lambda x: x[1])
    post_fields = each_post.map(xmlfields)
    
    from pyspark.sql.types import *
    questionsSchema = \
    StructType([
    StructField("Id",StringType()),
    StructField("PostTypeId",StringType()),
    StructField("AcceptedAnswerId",StringType()),
    StructField("CreationDate",StringType()),
    StructField("Score",StringType()),
    StructField("ViewCount",StringType()),
    StructField("OwnerUserId",StringType()),
    StructField("LastEditorUserId",StringType()),
    StructField("LastEditDate",StringType()),
    StructField("Title",StringType()),
    StructField("LastActivityDate",StringType()),
    StructField("Tags",StringType()),
    StructField("AnswerCount",StringType()),
    StructField("CommentCount",StringType()),
    StructField("FavoriteCount",StringType())])

    postDF = spark.createDataFrame(post_fields, questionsSchema)

    postDF.write.format('com.databricks.spark.csv').options(header=True).save('/user/apaul/stackexchange/posts_all_csv_with_header')

if __name__ == "__main__":
    main()
