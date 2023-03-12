git pull

docker-compose -f docker/docker-compose.yml up -d --build
docker-compose -f docker/docker-compose.yml exec web python3 manage.py migrate --noinput
docker-compose -f docker/docker-compose.yml exec web python3 manage.py collectstatic --noinput
docker-compose -f docker/docker-compose.yml restart nginx  # Sometimes the connection between nginx and web fails
