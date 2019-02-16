build-docker:
	docker build -t treehacks-project .

run-docker:
	docker rm -f $(docker ps -aq)
	docker run -it -p 3000:22 -p 4000:80 -p 5000:3000 -p 6000:8000 --name running treehacks-project