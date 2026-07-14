FROM ubuntu:22.04

RUN apt update && \
    apt install -y procps iproute2 net-tools && \
    apt clean

COPY system_info.sh /system_info.sh

RUN chmod +x /system_info.sh

CMD ["/system_info.sh"]

