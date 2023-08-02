FROM python:3.9
WORKDIR /app
VOLUME /app
EXPOSE 5000
ENV FLASK_ENV=development
COPY . .
RUN pip install -r requirements.txt
# RUN pip install python-dotenv

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "-p 5000"]