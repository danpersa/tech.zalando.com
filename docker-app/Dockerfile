FROM zalando/nikola

RUN apt-get install -y git supervisor nginx

COPY supervisord.conf /etc/supervisord.conf
COPY update.sh /
COPY default-nginx-site.conf /etc/nginx/sites-available/default

EXPOSE 8000

ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]


