FROM charlesgreen/tensorflow:1.4.0

LABEL maintainer="Charles Green <cg@simplycubed.com>"

WORKDIR /keras-server

COPY ./ /keras-server
COPY ./models /keras-server/models

EXPOSE 7171

CMD ["/bin/bash"]
#CMD ["/bin/bash", "server.py"]