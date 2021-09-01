APP_NAME=$1
if [ "$1" ]
then
  docker-compose exec django sh -c "python manage.py generate ${APP_NAME} --serializers"
  docker-compose exec django sh -c "python manage.py generate ${APP_NAME} --views --format modelviewset"
fi