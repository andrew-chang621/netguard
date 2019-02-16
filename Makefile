build-docker:
	docker build -t treehacks-project .

run-docker:
	docker run --privileged -p 80:80 -p 80-9000:80-9000 -v $(pwd)/device-daemon:/device-daemon --name iot-security-container treehacks-project