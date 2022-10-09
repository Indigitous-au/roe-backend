docker stop hack2022
docker rm hack2022
docker rmi hack2022
docker build -t "hack2022" .
docker run -d -p 5000:80 --name="hack2022" "hack2022"