APP_NAME=$1
if [ "$1" ]
then
  bash -c "mkdir django/main/apps/${APP_NAME}"
  bash -c "docker-compose exec django python manage.py startapp ${APP_NAME} main/apps/${APP_NAME}"
fi