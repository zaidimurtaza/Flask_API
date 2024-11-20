## POST /posts

### Description:
Creates a new post with the provided title and content in the database.

This endpoint allows users to submit a post with a title and content. The post will be saved to the database. If successful, it returns a confirmation message with a `201 Created` status.

### Request URL:
- **URL**: `/api/posts`
- **Method**: POST
- **Content-Type**: `application/json`

### Request Body:
The request should include a JSON object containing the title and content of the post.

```json
{
    "title": "My First Post",  // The title of the post (string)
    "content": "This is the content of my first post." // The content of the post (string)
}




## GET /Get data from database

### Description:
Fetches all the posts stored in the database.

This endpoint allows users to retrieve all the posts that have been stored in the database. It will return the details of each post, including the title and content. If successful, it returns a list of posts with a 200 OK status.

### Request URL:
- **URL**: `api/table_detail`
- **Method**: GET
- **Content-Type**: `application/json`

### Response Body:
The response will include a JSON array of posts. Each post contains an id, title, and content.
```json
[
    {
        "id": 1,          // The unique identifier of the post (integer)
        "title": "My First Post",  // The title of the post (string)
        "content": "This is the content of my first post."  // The content of the post (string)
    },
    {
        "id": 2,
        "title": "Another Post",
        "content": "This is the content of another post."
    }
]
