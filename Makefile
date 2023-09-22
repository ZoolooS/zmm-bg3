install:
	poetry install

build:
	poetry build

package-install:
	# python3 -m pip install --user dist/*.whl
	# python -m pip install --user dist/*.whl
	# python -m pip install dist/*.whl

zmm-bg3:
	poetry run zmm-bg3

make lint:
	poetry run flake8 zmm-bg3
