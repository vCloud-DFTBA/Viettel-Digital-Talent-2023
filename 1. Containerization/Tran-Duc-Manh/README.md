### Student attention Backend application

Base on FastAPI, the application build on asynchronously mechanism that offer higher performance I/O operations.

- Server host in: https://api.viettelcloud.site/ 

- Visited Swagger site: https://api.viettelcloud.site/docs

![viettelcloud](images/lab1.jpg)

### Base components
The application is 3-tier components:
 - FastAPI
 - MongoDB
 - Nginx

I also offer to use Jaeger for tracing and distributed logging with EFK(not implemented yet).

### What we're doing

- Buy a domain from tenten.vn
- Rend a server from FPT Cloud
- Connect DNS from Cloudflare
- Seft host 3-tier application on FPT server
- Configure SSL certificate to secure connection

### How to use

Configuration the enviroment on `.env` file

Start the application: 

```
docker-compose run -d
```

Please use the following URL: `http://localhost:8080\docs`

### Contribute

Feel free to contribute with me!!!