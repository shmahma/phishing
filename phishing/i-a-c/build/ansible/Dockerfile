FROM williamyeh/ansible:debian9
WORKDIR /root/playbooks
COPY ./hosts /etc/ansible/
COPY ./ansible.cfg /etc/ansible/
COPY ./playbooks/ /root/playbooks
CMD ["tail","-f","/dev/null"]
