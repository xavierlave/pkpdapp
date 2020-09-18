FROM python:3.6-slim-stretch

# install libsundials-serial-dev
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libsundials-serial-dev

# install nginx
RUN apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# clean up apt
RUN apt-get clean
RUN apt-get autoclean
RUN apt-get autoremove
RUN rm -rf /var/lib/apt/lists/*

# install app and dependencies
RUN pip install --upgrade pip 
COPY ./ /pkpdapp
RUN cd /pkpdapp && pip install --no-cache-dir -r requirements.txt 
RUN python /pkpdapp/pkpdapp/manage.py migrate --noinput
RUN python /pkpdapp/pkpdapp/manage.py collectstatic --noinput

WORKDIR /pkpdapp
RUN chown -R www-data:www-data /pkpdapp

# make root/.config dir and make it writable (myokit writes to it)
RUN mkdir -p /root/.config
RUN chown -R www-data:www-data /root

# start server
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/pkpdapp/start-server.sh"]