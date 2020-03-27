.PHONY: server serve frontend install-frontend install-requirements migration reset-db test

server:
	@python manage.py runserver

serve:
	@cd frontend && npm run build && serve dist

frontend:
	@cd frontend && npm run dev

install-frontend:
	@cd frontend/landing && npm install
	@cd frontend && npm install && npm install -g serve && npm run build

install-requirements:
	@pip install -r requirements.txt

migration:
	@python manage.py migrate

reset-db:
	@sudo -iu postgres bash -c "psql -c 'DROP DATABASE IF EXISTS coobs;'"
	@sudo -iu postgres bash -c "psql -c 'CREATE DATABASE coobs;'"
	@sudo -iu postgres bash -c "psql -c 'GRANT ALL PRIVILEGES ON DATABASE coobs TO coobs;'"
	@echo "\033[0;32mDB reset done! => Running migrations.."
	@$(MAKE) -s migration
	@echo "\033[0;32mMigrations done! => Creating superuser.."
	@python manage.py createsuperuser

test:
	@echo "\033[0;31m@TODO Add some tests!\033[0m"
