
FROM python:3.8-alpine
 
COPY ./requirements.txt /app/requirements.txt
 

WORKDIR /app
 

RUN pip install -r requirements.txt
 

COPY ./app/ /app
 
RUN apk update && apk add openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:ansible' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

ENV NOTVISIBLE "dans le profil des utilisateurs"
RUN echo "export VISIBLE=now" >> /etc/profile
RUN ssh-keygen -A 
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

