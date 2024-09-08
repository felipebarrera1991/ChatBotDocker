# Use a imagem base do Python
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copie os arquivos de requisitos e instale as dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código-fonte da aplicação para o container
COPY . .

# Exponha a porta na qual o Flask estará rodando
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]