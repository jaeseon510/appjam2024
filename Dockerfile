FROM python:3.13
WORKDIR /PyunIt
COPY /app /PyunIt/
EXPOSE 8000
CMD ["uvicorn","main:app","--host","0.0.0.0", "--port", "8000" ]