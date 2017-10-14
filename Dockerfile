FROM vimagick/scrapyd

WORKDIR /usr/src/app

COPY portia_projects/requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python" ]
