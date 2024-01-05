# i got this from the tutorial i learned docker from
# im gonna change this later on
FROM hemanhp/djbase:4.2.4


COPY ./requirements /requirements
COPY ./scripts /scripts
COPY ./src /src

WORKDIR src

EXPOSE 8000

RUN /py/bin/pip install -r /requirements/development.txt

# RUN apk add  geos gdal


RUN chmod -R +x /scripts && \
#    might not need static and media files
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    adduser --disabled-password --no-create-home twitter && \
    chown -R twitter:twitter /vol && \
    chmod -R 755 /vol


ENV PATH="/scripts:/py/bin:$PATH"

USER twitter

CMD ["run.sh"]