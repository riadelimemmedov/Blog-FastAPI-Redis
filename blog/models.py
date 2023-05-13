
#!Python modules and function
import datetime
import random

#!Redis Orm
from redis_om import get_redis_connection
from redis_om import get_redis_connection, EmbeddedJsonModel, JsonModel, Field, Migrator


#!Third party packages
from decouple import config


#!Helpers Method
from helpers import random_code


#Create your models here.

#*RedisModel
class RedisModel:
    def __init__(self,host=config('REDIS_HOST'),port=config('REDIS_PORT',cast=int),password=config('REDIS_DATABASE_PASSWORD'),decode_responses=config('DECODE_RESPONSE',default=True)):
        self.redis = get_redis_connection(host=host,port=port,password=password,decode_responses=decode_responses)
        
    def get(self):
        return self.redis
redis = RedisModel().get()

################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

#!Author
class Author(EmbeddedJsonModel):
    first_name: str = Field(index=True, full_text_search=True)
    last_name: str
    email: str
    bio: str
    slug:str = Field(default=f"author")
    date_joined: datetime.date = Field(
        default=datetime.datetime.today().strftime("%Y-%m-%d")
    )  # We have define any country timezone and return current date

    class Meta:
        database = redis


#!Blog
class Blog(EmbeddedJsonModel):
    title: str = Field(index=True, full_text_search=True)
    content: str
    slug = Field(default=f"blog")
    author: Author
    date_posted: datetime.date = Field(
        default=datetime.datetime.today().strftime("%Y-%m-%d")
    )  # But today return local current timezone,according to where you are, Year,Month,Day

    class Meta:
        database = redis


#!Comment
class Comment(JsonModel):
    body : str
    blog = Blog
    author = Author
    date_commented: datetime.date = Field(
        default=datetime.datetime.today().strftime("%Y-%m-%d")
    )  
    
    class Meta:
        database = redis

#?Migrate table to redis cloud database
Migrator().run()
