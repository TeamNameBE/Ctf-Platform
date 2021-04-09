git pull

docker-compose up -d --build
docker-compose exec web python3 manage.py migrate --noinput
docker-compose exec web python3 manage.py collectstatic --noinput
docker-compose restart nginx  # Sometimes the connection between nginx and web fails
