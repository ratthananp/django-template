DATABASE_SERVICE_NAME=$1

until docker-compose exec "${DATABASE_SERVICE_NAME}" sh -c "pg_isready -h localhost -p 5432 -U postgres"
do
  echo "Waiting for postgres at: $DATABASE_SERVICE_NAME"
  sleep 2;
done
