FROM scrapinghub/portia

RUN set -xe \
    && apt-get update \
    && sudo dpkg --configure -a \
    && apt-get install -f -y gcc \
                          python3-dev python-dev \
                          curl bash \
                          make build-essential libffi-dev \
                          python-software-properties software-properties-common


COPY portia_projects/requirements.txt .
COPY portia_projects/hoaxlyPortia /app/data/projects/hoaxlyPortia/


RUN pip install --no-cache-dir -r requirements.txt


COPY ./scrapyd.conf /etc/scrapyd/
VOLUME /etc/scrapyd/ /var/lib/scrapyd/
EXPOSE 6800
ENTRYPOINT ["scrapyd", "--pidfile="]
