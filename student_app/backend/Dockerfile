FROM python:3.11-slim
WORKDIR /stu
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY stu.py .
EXPOSE 5000
CMD ["python", "stu.py"]