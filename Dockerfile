
FROM python:3.9-alpine3.13
LABEL maintainer="luizsolda"

ENV PYTHONUNBUFFERED 1 

# Requirements que serão copiados para o docker.
COPY ./requirements.txt /tmp/requirements.txt

# Garantir que tudo que há no diretório do serviço principal seja copiado para o container.
COPY ./norktown /norktown

# Diretório padrão no Docker
WORKDIR /norktown

# Porta
EXPOSE 8080

# Roda python em uma máquina virtual dentro do container (não é necessário mas pode evitar futuros erros de dependência)
# Altera o pip para a máquina virtual
# Somente vai instalar o que for solicitado no requirements.dev.txt quando a tag DEV estiver ativa,
# ou seja, somente vai instalar estas quando a imagem for instanciada pelo docker-compose.
# Remove /tmp depois de seu conteúdo ser instalado. Boas práticas do Docker, manter mais otimizado possível.
# adduser é para que o django-user seja utilizado após o RUN, para que o docker não fique ativo com o root.

# Adiciona pacote postgresql 'apk add --update --no-cache postgresql-client'
# Instala pacotep postgresql 'build-base postgresql-dev musl-dev && \'
# O pacote postgresql somente é utilizado par ainstalar psycopg2 nos requirements, e pode ser removido 'apk del .tmp-build-deps && \'.
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \ 
    apk add --update --no-cache postgresql-client && \       
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \    
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        solda-user

# Atualiza o PATH para a máquina virtual do python.
ENV PATH="/py/bin:$PATH"

CMD  flask run --host=0.0.0.0 --port=8080

# Define o usuário do Linux. É bom definir um usuário sem privilégios sudo para utilizar o sistema no container.
USER solda-user