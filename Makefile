APP = restapi

test: 
	@flake8 . --exclude .venv
	@pytest -v --disable-warnings

compose:
	@docker-compose build
	@docker-compose up

heroku:
	@heroku container:login
	@heroku container:push -a restapi-studying web
	@heroku container:release -a restapi-studying web