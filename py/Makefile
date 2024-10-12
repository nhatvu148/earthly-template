VENV_BIN_DIR = venv/bin
PIP = "$(VENV_BIN_DIR)/pip"
PYTHON = "$(VENV_BIN_DIR)/python"

define create-venv
python3 -m venv venv
endef

all: run

.PHONY: venv
venv:
	@$(create-venv)
	@$(PIP) install -r requirements.txt

run:
	@$(PYTHON) src/oauth_session.py

upload:
	docker run --rm upload-gdrive-image:latest python3 upload_gdrive.py > output.log 2>&1