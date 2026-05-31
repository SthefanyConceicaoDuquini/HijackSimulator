FROM alpine:latest
RUN apk add --no-cache bird iproute2 tcpdump bash
RUN mkdir -p /run/bird
CMD ["bird", "-f", "-u", "root", "-g", "root"]
