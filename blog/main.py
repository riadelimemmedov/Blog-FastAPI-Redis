#!FastApi
from fastapi import FastAPI

#!Models and Serializers
from models import Author, Blog, Comment

#!Redis Orm
from redis_om.model import NotFoundError

#!Python modules and methods
from datetime import datetime


# create your views here,and run server =>  uvicorn main:app --reload
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
@app.get("/authors") 
async def get_all_author():
    """
    Get all authors
    """
    authors = Author.find((Author.slug == "author")).all()
    return authors


# *create_author
@app.post("/authors") 
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
@app.get("/authors/{pk}")
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
@app.patch("/authors/{pk}") 
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
@app.delete("/authors/{pk}")
async def delete_author(pk: str):
    """
    This view delete single author,according to what the user sent
    """
    Author.delete(pk)
    return {"success": "Author deleted successfully"}


# *delete_all_authors
@app.delete("/authors/")
async def delete_all_authors():
    """
    Delete all authors
    """
    Author.find((Author.slug == "author")).delete()
    return {"success": "Deleted all author successfully"}


#!get_all_blogs
@app.get("/blogs")
async def get_all_blogs():
    """
    Get all blogs
    """
    blogs = Blog.find((Blog.slug == "blog")).all()
    return blogs


#!create_blog
@app.post("/blogs")
async def create_blog(body: dict):
    """
    This view create Blog
    """
    author = Author.get(body["author_id"])
    blog = Blog(title=body["title"], content=body["content"], author=author)
    blog.save()

    return blog


#!get_blog
@app.get("/blogs/{pk}")  
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
@app.patch("/blogs/{pk}")  
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
@app.delete("/blogs/{pk}")  
async def delete_blog(pk: str):
    """
    This view delete single blog,according to what to user sent
    """
    Blog.delete(pk)
    return {"success": "Blog deleted successfully"}


#!delete_all_blog
@app.delete("/blogs/")  
async def delete_all_blogs():
    """
    Delete all blogs
    """
    Blog.find((Blog.slug == "blog")).delete()
    return {"success": "Deleted all blogs successfully"}


# ?get_all_comments
@app.get("/comment/blog/{blog_pk}/")  
async def get_all_comments(blog_pk: str):
    """
    Get all comments for related to specific blog
    """
    comments = Comment.find((Comment.slug == "comment")).all()
    comments_blog = []
    for comment in comments:
        if comment.blog == blog_pk:
            comments_blog.append(
                {
                    "pk": comment.pk,
                    "body": comment.body,
                    "date_commented": comment.date_commented,
                    "slug": comment.slug,
                    "author": comment.author,
                    "blog": comment.blog,
                }
            )
    return comments_blog


# ?create_comment
@app.post("/comment/blog/{blog_pk}/{author_pk}/")  
async def create_comment(blog_pk: str, author_pk: str, body: dict):
    """
    Create comment for each specific blog
    """
    comment = Comment(body=body["body"], blog=blog_pk, author=author_pk)
    comment.save()
    return comment


# ?get_comment
@app.get("/comments/{pk}") 
async def get_comment(pk: str):
    """
    Return single comment,for matching primary comment key value
    """
    try:
        comment = Comment.get(pk)
    except NotFoundError:
        return {"error": "Not found comment"}, 404
    return comment


# ?update_comment
@app.patch("/comments/{blog_pk}/{comment_pk}")  
async def update_comment(blog_pk: str, comment_pk: str, body: dict):
    """
    Update comment for specified blog
    """
    comments = Comment.find((Comment.slug == "comment")).all()
    comments_blog = []
    for comment in comments:
        if comment.blog == blog_pk and comment.pk == comment_pk:
            comment.body = body["body"]
            comment.save()
            comments_blog.append(comment)
    return comments_blog


# ?delete_comment
@app.delete("/comments/{comment_pk}")  
async def delete_comment(comment_pk: str):
    """
    Delete single comment
    """
    Comment.delete(comment_pk)
    return {"success": "Comment deleted successfully"}


# ?delete_blog_comments
@app.delete("/delete/blog/comments/{blog_pk}")  
async def delete_blog_comments(blog_pk: str, comment_pk: str):
    """
    Delete all comments related to specific blog
    """
    comments = Comment.find((Comment.slug == "comment")).all()
    for comment in comments:
        if comment.blog == blog_pk:
            print("Comment ", comment)
            Comment.delete(comment.pk)
    return {"success": "Deleted all comments related to specific blog"}


# ?delete_all_comments
@app.delete("/comments/")  
async def delete_all_comments():
    """
    Delete all comments
    """
    Comment.find((Comment.slug == "comment")).delete()
    return {"success": "Deleted all comments successfully"}
