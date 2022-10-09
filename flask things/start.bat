docker build -t "hack2022" .
docker run -d -p 5000:80 --name="hack2022" -v :/app "hack2022"