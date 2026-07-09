# Task 0 - Basics of HTTP/HTTPS

## HTTP vs HTTPS

| HTTP | HTTPS |
|------|--------|
| HyperText Transfer Protocol | HyperText Transfer Protocol Secure |
| No encryption | SSL/TLS encrypted |
| Uses port 80 | Uses port 443 |
| Less secure | More secure |
| Suitable for public information | Suitable for sensitive information |

## HTTP Request Structure

Request Line:
GET /index.html HTTP/1.1

Headers:
Host: example.com
User-Agent: Browser
Accept: */*

Body:
(Optional)

## HTTP Response Structure

Status Line:
HTTP/1.1 200 OK

Headers:
Content-Type: text/html

Body:
Returned resource or requested data.

## Common HTTP Methods

### GET
Retrieves data from a server.
Use case: Viewing a webpage or fetching API data.

### POST
Creates a new resource.
Use case: Registering a new user.

### PUT
Updates an existing resource.
Use case: Editing profile information.

### DELETE
Deletes a resource.
Use case: Removing a user account.

## Common HTTP Status Codes

### 200 OK
The request completed successfully.

### 201 Created
A new resource was successfully created.

### 400 Bad Request
The request contains invalid data.

### 404 Not Found
The requested resource does not exist.

### 500 Internal Server Error
The server encountered an unexpected error.
