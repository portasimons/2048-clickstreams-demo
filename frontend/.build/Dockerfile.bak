FROM nginx

COPY nginx/nginx.conf /etc/nginx/nginx.conf

WORKDIR /app

COPY index.html .

COPY js ./js
COPY meta ./meta
COPY style ./style
COPY favicon.ico .
