FROM postgres:16

COPY ./6-api/schema.sql /docker-entrypoint-initdb.d/

EXPOSE 5432