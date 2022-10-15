Docker02
=====
* ### docker build . --tag pyramid
* ### docker run pyramid
* ### docker run pyramid 3
* ### docker build . --tag web-app-backend
* ### docker run -p 4000:5000 web-app-backend
* ### docker build . --tag web-app-frontend
* ### docker run -p 3000:3000 web-app-frontend
* ### docker build . --tag volume-app-frontend
* ### docker run -p 3000:3000 volume-app-frontend
* ### docker run -p 3000:3000 -v /Users/albert/GitLab/main/Docker/Docker02/volume/volume_data:/app/volume_data volume-app-frontend
* ### docker volume create book-data
* ### docker volume inspect book-data
* ### docker volume ls
* ### docker run -p 3000:3000 -v book-data:/app/volume_data volume-app-frontend
* ### docker run -v book-data:/book-data -it ubuntu
***
* ### Bind Mount
* ### Volume
***
* ### image
* ### container
* ### volume
***
* ### Images
    * ### docker build --tag my-app:1.0 .
    * ### docker images # listing images
    * ### docker save -o <path_for_generated_tar_file> <image_name> # Save the image as a tar file
    * ### docker load -i <path_to_tar_file> # Load the image into Docker
    * ### docker rmi my-app:1.0 # Remove a docker image
    * ### docker rmi --force my-app:1.0 
    * ### docker rmi $(docker images -a -q) # Remove all images that are not associated with existing containers
    * ### docker rmi $(docker images -a -q) -f # same as above, but forces the images associated with running containers to be also be removed
* ### Containers
    * ### docker run my-app:1.0
    * ### docker ps # view a list of running containers
    * ### docker ps -a # includes stopped containers
    * ### docker run -p 8000:3000 my-app:1.0 # Exposes port 3000 in a running container, and maps to port 8000 on the host machine
    * ### docker rm $(docker ps -a -q)  # removes all containers
    * ### docker rm $(docker ps -a -q) -f  # same as above, but forces running containers to also be removed
* ### Volumes
    * ### docker run -d --name my-app -v volume-name:/usr/src/app my-app:1.0
    * ### docker run -p 3000:3000 -v <load_absolute_path>:<docker_absolute_path> volume-app-frontend
    * ### docker volume ls 
    * ### docker volume prune # Removes unused volumes
<br />
