
# Blog-FastAPI-Redis

Blog-FastAPI-Redis is a Python-based web application designed for building a RESTful API for a blogging platform. It uses the FastAPI web framework and Redis as a database. The API allows users to create, read, update, and delete blog posts. Users can also add comments to posts and view comments on a specific post.

###
### Installation
    
    - Clone the repository using the command :  git clone https://github.com/riadelimemmedov/BlogApi-FastAPI-Redis.git.
    
    - Install the required packages using the command pip install -r requirements.txt.

    - Run the application using the command uvicorn main:app --reload.

####

### Endpoints
    * Blog
    /blogs (HTTP GET) => Returns a list of all blog posts.
    /blogs (HTTP POST)=> Creates a new blog post.
    /blogs/{blog_id} (HTTP GET) => Returns a specific blog post with the given blog_id.
    /blog/{blog_id} (HTTP PUT) => Updates an existing blog post with the given blog_id.
    /blog/{blog_id} (HTTP DELETE) => Deletes an existing blog post with the given blog_id.
    /blogs/(HTTP DELETE) => Deletes all existing blog post

    * Comments
    /comment/blog/{blog_id} (HTTP GET) => Returns a list of comments on the specific blog post with the given blog_id. 
    /comment/blog/{blog_id}/{author_id} (HTTP POST) => Creates a new comment on the specific blog post with the given blog_id and author_pk.
    /comments/{comment_id} (HTTP GET) => Return specific comment match to sended comment id value
    /comments/{blog_id}/{comment_id} (HTTP PUT) => Updates an existing comment with the given blog_id and comment_id.
    /comments/{comment_id} (HTTP DELETE) => Delete specific comment
    /delete/blog/comments/{blog_id} (HTTP DELETE) => Deletes an existing comment on the specific blog post with the given blog_id and comment_id.
    /comments/ (HTTP DELETE) => Deletes all existing comments	


    * Authors
    /authors (HTTP GET) => Returns a list of authors
    /authors (HTTP POST)=> Creates a authors for given specific credentials
    /authors/{author_id} (HTTP GET) => Return specific author match to sended author id value
    /authors/{author_id} (HTTP UPDATE) => Updates an existing author with given the author_id value
    /authors/{author_id} (HTTP DELETE) => Delete specific author match to sended author id value
    /authors/ (HTTP DELETE) => Deletes all existing authors

####

### Redis Configuration
    By default, the application uses a local Redis server running 
    on the default port (6379). If you want to use a different 
    Redis server, you can change the redis_host and redis_port 
    variables in the main.py file.

####

### License
    This project is licensed under the MIT License








