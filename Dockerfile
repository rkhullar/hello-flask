FROM rkhullar/openssh:python-3.8.9-slim
USER root

RUN  adduser --disabled-password --gecos '' ubuntu \
  && pip install -U pip setuptools                 \
  && pip install flask

USER ubuntu
WORKDIR /home/ubuntu
COPY --chown=ubuntu app.py .

USER ssh-user
ENV TARGET_USER=ubuntu
CMD ["python", "app.py"]
