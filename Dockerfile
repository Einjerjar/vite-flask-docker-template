FROM node:17-slim AS front

WORKDIR /usr/src/front
COPY ./front/package.json .
RUN npm install

COPY ./front .

RUN npm run build

FROM python:3.10-slim AS back

WORKDIR /usr/src/back
COPY ./back/requirements.txt .
RUN pip install -r requirements.txt

COPY ./back .

COPY --from=front /usr/src/front/dist /usr/src/back/dist

EXPOSE 80

CMD ["gunicorn", "app:app"]