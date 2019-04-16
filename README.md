# Serverless AWS Custom Authorizer Python Lambda

An example implementation of an AWS custom authorizer. Written in python, deployed with the Serverless Framework.

A very simple example to demonstrate the principle and to build off of. Typically you would replace the hardcoded api key check with a database lookup, for example.

### Deploy
`$ serverless deploy`

### Test
Un-authenticated request
```
$ curl <foo_endpoint_url> -H "Authorization:Bearer wrong"

{"Message":"User is not authorized to access this resource with an explicit deny"}
```

Authenticated request
```
$ curl <foo_endpoint_url> -H "Authorization:Bearer 123abc"

{"it": "worked!"}
```
