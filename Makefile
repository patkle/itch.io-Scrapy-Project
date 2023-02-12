.PHONY: deploy
deploy:
	python3 -m shub deploy

.PHONY: test
test:
	python3 -m scrapy crawl game_jams -O game_jams.csv -a pages=1

.PHONY: black
black:
	python3 -m black .

.PHONY: sort
sort:
	python3 -m isort .

.PHONY: pretty
pretty: sort black

.PHONY: clean
clean:
	find . -type d -name __pycache__ | xargs rm -fr
	find . -type d -name .scrapy | xargs rm -fr
	find . -type d -name build | xargs rm -fr
	find . -type d -name project.egg-info | xargs rm -fr
	find . -type f -name "*.pyc" | xargs rm -fr
	find . -type f -name "*.log" | xargs rm -fr
	find . -type f -name "*.csv" | xargs rm -fr
