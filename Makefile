default: image startapp 

.PHONY: image

image:
	docker build --tag sample:latest .

startapp: image

	docker run -it --rm -p 5000:5000 sample:latest
