
#!FastApi
from fastapi import FastAPI

#!Models and Serializers
from models import Author, Blog

#!Redis Orm
from redis_om.model import NotFoundError

#!Python modules and methods
from datetime import datetime


#create your views here,and run server =>  uvicorn main:app --reload
app = FastAPI()

# root
@app.get("/")
async def root():
    """
    This view return message object
    """
    return {"message": "Hello world"}


################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################


# *get_all_author
@app.get("/authors")  # +
async def get_all_author():
    """
    Get all authors
    """
    authors = Author.find((Author.slug == "author")).all()
    return authors


# *create_author
@app.post("/authors")  # +
async def create_author(body: Author):
    """
    This view create Author
    """
    author = Author(
        first_name=body.first_name,
        last_name=body.last_name,
        email=body.email,
        bio=body.bio,
    )
    author.save()

    return author


# *get_author
@app.get("/authors/{pk}")  # +
async def get_author(pk: str):
    """
    Return specific author,match to sended pk value
    """
    try:
        author = Author.get(pk)
    except NotFoundError:
        return {"error": "Not found author"}, 404
    return author


# *update_author
@app.patch("/authors/{pk}")  # +
async def update_author(pk: str, body: dict):
    """
    Update author,according to what to user send
    """
    author = Author.get(pk=pk)

    author.first_name = body["first_name"]
    author.last_name = body["last_name"]
    author.email = body["email"]
    author.bio = body["bio"]

    author.save()
    return author


# *delete_author
@app.delete("/authors/{pk}")  # +
async def delete_author(pk: str):
    """
    This view delete single author,according to what the user sent
    """
    Author.delete(pk)
    return {"success": "Author deleted successfully"}


# *delete_all_authors
@app.delete("/authors/")  # +
async def delete_all_authors():
    """
    Delete all authors
    """
    Author.find((Author.slug == "author")).delete()
    return {"success": "Deleted all author successfully"}


#!get_all_blogs
@app.get("/blogs")  # +
async def get_all_blogs():
    """
    Get all blogs
    """
    blogs = Blog.find((Blog.slug == "blog")).all()
    return blogs


#!create_blog
@app.post("/blogs")  # +
async def create_blog(body: dict):
    """
    This view create Blog
    """
    author = Author.get(body["author_id"])
    blog = Blog(title=body["title"], content=body["content"], author=author)
    blog.save()

    return blog


#!get_blog
@app.get("/blogs/{pk}")  # +
async def get_blog(pk: str):
    """
    Return specific blog,match to sended pk value
    """
    try:
        blog = Blog.get(pk)
    except NotFoundError:
        return {"error": "Not blog found"}, 404
    return blog


#!update_blog
@app.patch("/blogs/{pk}")  # +
async def update_blog(pk: str, body: dict):
    """
    Update blog,according to what to user sent
    """
    blog = Blog.get(pk)

    blog.title = body["title"]
    blog.content = body["content"]

    blog.save()
    return blog


#!delete_blog
@app.delete("/blogs/{pk}")  # +
async def delete_blog(pk: str):
    """
    This view delete single blog,according to what to user sent
    """
    Blog.delete(pk)
    return {"success": "Blog deleted successfully"}


#!delete_all_blog
@app.delete("/blogs/")  # +
async def delete_all_blogs():
    """
    Delete all blogs
    """
    Blog.find((Blog.slug == "blog")).delete()
    return {"success": "Deleted all blogs successfully"}
