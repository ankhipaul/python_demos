"""
This is a demo to parse xml file, and convert it to json file.

I have used Databricks libraries for that. Spark-xml is a
very cool library that makes parsing XML data so much easier using
spark SQL.
Spark-xml library : https://github.com/databricks/spark-xml

Loads Tags.xml as json in HDFS.

Downloaded the Stack Exchange Data Dump for this exercise. 

Placed the data of Tags.xml in HDFS and generated the json ourput file in HDFS.

Start pyspark with the command below and can test from the REPL -
  pyspark --packages com.databricks:spark-xml_2.10:0.4.1
Or run using
  spark2-submit --packages com.databricks:spark-xml_2.10:0.4.1 tags_xml_to_json.py
  
Written By: ANKHI PAUL

"""
import pyspark
import pyspark.sql
from pyspark.sql import SparkSession
from pyspark.sql.types import *
import xml.etree.ElementTree as ET


# extract the values in each xml row
def xmlfields(string):
    elements = ET.fromstring(string.encode('utf-8')).attrib
    
    tag_id = elements.get("Id")
    tag_name = elements.get("TagName")
    count = elements.get("Count")
    excerpt_post_id = elements.get("ExcerptPostId")
    wiki_post_id = elements.get("WikiPostId")
       
    return (tag_id, tag_name, count, excerpt_post_id, wiki_post_id)

def main():
    spark = SparkSession.builder.appName("TagsXMLtoJson").getOrCreate() 
      
    xml_tags = spark.sparkContext.newAPIHadoopFile("/user/apaul/stackexchange/Tags.xml", 'com.databricks.spark.xml.XmlInputFormat', 'org.apache.hadoop.io.Text', 'org.apache.hadoop.io.Text', conf={'xmlinput.start': '<row', 'xmlinput.end': '/>'})
    each_tag = xml_tags.map(lambda x: x[1])
    tag_fields = each_tag.map(xmlfields)
    
    tags_schema = \
    StructType([
    StructField("Id",StringType()),
    StructField("TagName",StringType()),
    StructField("Count",StringType()),
    StructField("ExcerptPostId",StringType()),
    StructField("WikiPostId",StringType())])
    
    tagDF = spark.createDataFrame(tag_fields, tags_schema)
    
    tagDF.write.json('/user/apaul/stackexchange/tags_json')

if __name__ == "__main__":
    main()
