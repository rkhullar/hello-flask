## Hello Flask

This repository provides an example flask service meant to be used as an initial deployment in the field. The service 
listens for common http methods and responds with a json representation of the request metadata. The image is based on a
python variant of [ecs-fargate-base][base-docker] so that we have a specific version of python along with the ability to 
ssh into the container as the main web service is running.

## Example Usage
```sh
docker build -t hello-flask .
docker run -p 22:22 -p 8000:8000 -e AUTHORIZED_KEYS="`cat ~/.ssh/{keypair}.pub`" hello-flask
curl -X GET localhost:8000
# "method":"GET","path":"/","service_name":"hello world","service_port":8000}
ssh -i ~/.ssh/{keypair} ssh-user@localhost
```

[base-docker]: https://hub.docker.com/r/rkhullar/openssh
[base-github]: https://github.com/rkhullar/ecs-fargate-base
