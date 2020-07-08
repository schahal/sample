default: image startapp 

.PHONY: image startapp pypk

image:
	docker build --tag sample:latest .

startapp: image
	docker run -it --rm -p 5000:5000 sample:latest

pypkg_create:
	python3 -m venv build
	. build/bin/activate; \
	python -m pip install -r requirements_dev.txt; \
	python3 setup.py sdist bdist_wheel; \
	deactivate; \

pypkg_upload:
	python3 -m twine upload --repository-url=https://test.pypi.org/legacy/ dist/*

clean:
	rm -rf dist/ build/ *.egg-info flask_session __pycache__
