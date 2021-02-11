FROM mongo:3.6
COPY seed-data.js /docker-entrypoint-initdb.d/
RUN chmod -R go+w /data/db
RUN chmod -R go+w /tmp
USER 1001