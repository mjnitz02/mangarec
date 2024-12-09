.PHONY : black lint test

black:
	python -m isort --sl --line-length 120 mangarec tests
	python -m black --line-length 120 mangarec tests

lint:
	python -m isort --sl --line-length 120 mangarec tests
	python -m black --line-length 120 mangarec tests
	python -m pylint mangarec tests

test:
	python -m pytest tests/

clean-git:
	git fetch -p
	# for branch in $(git for-each-ref --format '%(refname) %(upstream:track)' refs/heads | awk '$2 == "[gone]" {sub("refs/heads/", "", $1); print $1}'); do git branch -D $branch; done
