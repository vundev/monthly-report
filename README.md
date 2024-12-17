`
curl -X GET http://localhost:8000/customer/me \
-H "Content-Type: application/json"
`

`
curl -X POST http://localhost:8000/customer/register \
-H "Content-Type: application/json" \
-d '{"username": "avasilev", "password": "short"}'
`