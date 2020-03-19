FROM python:3.7
RUN mkdir /code
WORKDIR /code

RUN apt-get update \
    && apt-get -y install gettext libgettextpo-dev \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y locales \
    && sed -i -e 's/# es_MX.UTF-8 UTF-8/es_MX.UTF-8 UTF-8/' /etc/locale.gen \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=es_MX.UTF-8
ENV LANG es_MX.UTF-8
ENV LANGUAGE es_MX.UTF-8
ENV LC_ALL es_MX.UTF-8

COPY ./src/requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

COPY ./src/entrypoint.sh /code/entrypoint.sh
CMD ["sh entrypoint.sh"]
