# TeamBoard API Documentation

Base URL: `http://127.0.0.1:8000`

---

## 1. User Registration

**Endpoint**: `POST /auth/register/`

**Description**: Registers a new user and creates their associated company.

**Headers**:
- `Content-Type: application/json`

**Request Body**:
```json
{
  "username": "johndoe",
  "password": "secretpassword123",
  "email": "johndoe@example.com",
  "company_name": "Acme Corp"
}
```

**Success Response** (Status: `201 Created`):
```json
{
  "username": "johndoe",
  "company_name": "Acme Corp",
  "api_key": "generated_api_key_string",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI..."
}
```

**Error Response** (Status: `400 Bad Request`):
```json
{
  "error": "Username already exists"
}
```
*(Validation errors from the serializer may also be returned in a dictionary format)*

---

## 2. User Login

**Endpoint**: `POST /auth/login/`

**Description**: Authenticates an existing user and returns an access token.

**Headers**:
- `Content-Type: application/json`

**Request Body**:
```json
{
  "username": "johndoe",
  "password": "secretpassword123"
}
```

**Success Response** (Status: `200 OK`):
```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI...",
  "company_name": "Acme Corp",
  "api_key": "generated_api_key_string"
}
```

**Error Response** (Status: `401 Unauthorized`):
```json
{
  "error": "Invalid credentials"
}
```

---

## 3. Query Knowledge Base

**Endpoint**: `POST /kb/query/`

**Description**: Search the Knowledge Base for entries containing the keyword in the question or answer. This endpoint logs the query against the company making the request.

**Headers**:
- `Content-Type: application/json`
- `Authorization: Bearer <access_token>`

**Request Body**:
```json
{
  "search": "database"
}
```

**Success Response** (Status: `200 OK`):
```json
{
  "search": "database",
  "count": 1,
  "results": [
    {
      "id": 1,
      "question": "How to configure the PostgreSQL database?",
      "answer": "Update the DATABASES setting in settings.py with your credentials.",
      "category": "database",
      "created_at": "2026-04-27T10:00:00Z"
    }
  ]
}
```

**Error Response** (Status: `400 Bad Request`):
```json
{
  "error": "Search field required"
}
```

---

## 4. Admin Usage Summary

**Endpoint**: `GET /admin/usage-summary/`

**Description**: Retrieves overall usage statistics across all companies. Requires the authenticated user to have an Admin role.

**Headers**:
- `Authorization: Bearer <access_token>`

**Request Body**:
*None*

**Success Response** (Status: `200 OK`):
```json
{
  "total_queries": 152,
  "active_companies": 12,
  "top_search_terms": [
    {
      "search_term": "api",
      "count": 45
    },
    {
      "search_term": "database",
      "count": 30
    },
    {
      "search_term": "deployment",
      "count": 22
    }
  ]
}
```

**Error Response** (Status: `403 Forbidden`):
*Returned if the user does not have Admin privileges.*
