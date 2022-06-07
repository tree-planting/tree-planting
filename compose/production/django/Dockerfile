FROM python:3.10-slim-buster

#ENV PYTHONDONTWRITEBYTECODE 1
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


#RUN addgroup --system django \
#    && adduser --system --ingroup django django


############ NPM ############
#RUN curl https://www.npmjs.com/install.sh -o npm-install.sh
#RUN sh npm-install.sh
#RUN rm npm-install.sh
# install frontend packages
#COPY package.json package-lock.json ./
#RUN npm install npm@latest -g
#RUN npm install
# build frontend code
#RUN npm run build && npm run build-dev
#COPY . .


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

COPY ./compose/production/django/start /srv/start
RUN sed -i 's/\r$//g' /srv/start
RUN chmod +x /srv/start

#COPY --chown=django:django . /app

#USER django

WORKDIR /srv/app

#ENTRYPOINT ["/srv/entrypoint"]
