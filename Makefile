.PHONY: test clean install

test:
	python -m pytest tests/ -v --cov=src

install:
	pip install -r requirements.txt

clean:
	rm -rf __pycache__ .pytest_cache
	rm -rf src/**/__pycache__ tests/**/__pycache__
	rm -rf .coverage htmlcov
