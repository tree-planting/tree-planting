FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*


# timezone to Asia/Taipei
RUN ln -sf /usr/share/zoneinfo/Asia/Taipei /etc/localtime
RUN echo "Asia/Taipei" > /etc/timezone
ENV TZ=Asia/Taipei


# install python package
RUN pip install --upgrade pip
RUN pip install --no-cache-dir pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --dev --ignore-pipfile --system


#COPY ./compose/production/django/entrypoint /srv/entrypoint
#RUN sed -i 's/\r$//g' /srv/entrypoint
#RUN chmod +x /srv/entrypoint

COPY ./compose/local/django/start /srv/start
RUN sed -i 's/\r$//g' /srv/start
RUN chmod +x /srv/start

WORKDIR /srv/app

#ENTRYPOINT ["/srv/entrypoint"]