## Hello Flask

This repository provides an example flask service meant to be used as an initial deployment in the field. The service 
listens for common http methods and responds with a json representation of the request metadata. The image is based on a
python variant of [ecs-fargate-base][base-docker] so that we have a specific version of python along with the ability to 
ssh into the container as the main web service is running.

[base-docker]: https://hub.docker.com/r/rkhullar/openssh
[base-github]: https://github.com/rkhullar/ecs-fargate-base
