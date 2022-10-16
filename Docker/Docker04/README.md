Docker04
=====
* ### docker run -d -p 5000:5000 --name registry registry:2
* ### docker ps # List containers.
* ### docker pull ubuntu
* ### docker tag ubuntu localhost:5000/my-ubuntu
* ### docker push localhost:5000/my-ubuntu
* ### docker image remove ubuntu
* ### docker image remove localhost:5000/my-ubuntu
* ### docker pull localhost:5000/my-ubuntu
* ### docker run -it localhost:5000/my-ubuntu
* ### docker container stop registry
* ### docker container rm -v registry
***
* ### docker tag localhost:5000/my-ubuntu xxx/xxx
* ### docker push xxx/xxx
* ### docker pull xxx/xxx
<br />
