.PHONY: migrate
migrate:
	@echo "Migrating database..."
	python manage.py migrate --noinput

.PHONY: collectstatic
collectstatic:
	@echo "Copying collectstatic files..."
	python manage.py collectstatic --noinput

.PHONY: clean
clean:
	@echo -n "Clear temp files..."
	find . -name '__pycache__' -exec rm -rf {} +
	find . -type f -name '*.py[co]' -exec rm -f {} +
	find . -type f \( -name '*~' -o -name '.*~' -o -name '@*' -o -name '#*#' -o -name '*.orig' -o -name '*.rej' \) -exec rm -f {} +
	rm -rf .coverage coverage.html coverage.xml htmlcov build cover .install-deps *.egg-info .pytest_cache dist

.PHONY: run
run: migrate collectstatic clean
	@echo "Running server..."
	uvicorn backend.config.asgi:application --workers  4 --host  0.0.0.0 --port  8000 --reload

.PHONY: help
help:
	@echo -n "Common make targets"
	@echo ":"
	@cat Makefile | sed -n '/^\.PHONY: / h; /\(^\t@*echo\|^\t:\)/ {H; x; /PHONY/ s/.PHONY: \(.*\)\n.*"\(.*\)"/  make \1\t\2/p; d; x}'| sort -k2,2 |expand -t  20