# Python image to use.
FROM python:3.7 as builder

WORKDIR /opt/app
COPY requirements.txt /opt/app
RUN pip install --no-cache-dir -r requirements.txt
COPY . . 
FROM gcr.io/distroless/python3-debian10 as runner
COPY --from=builder /usr/local/lib/python3.7/site-packages /usr/lib/python3.7/site-packages
COPY --from=builder /opt/app /opt/app

ENV PYTHONUNBUFFERED True
ENV PYTHONPATH="$PYTHONPATH:/usr/lib/python3.7/site-packages"
# Set the working directory to /app
WORKDIR /opt/app

EXPOSE 8000

# Run app.py when the container launches
ENTRYPOINT ["./uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
