SRC :="./src/"
VENV_NAME :=.
PYTHON := python3
NAME := app
DATA_CSV := https://cdn.intra.42.fr/document/document/23381/data.csv
ENV_VAR_INSTALL := INSTALL_FMAUGUIN_FT_LINEAR_REGRESSION


$(NAME):
	@if [ ! -d $(VENV_NAME)/bin ]; then \
		make install; \
	fi
	python3 $(SRC)app.py

all: install
	python3 $(SRC)app.py

install:
	@echo "Creating virtual environment..."
	( \
	 	$(PYTHON) -m venv $(VENV_NAME); \
		. $(VENV_NAME)/bin/activate; \
		pip install -r requirements.txt; \
		mkdir -p data; \
		wget $(DATA_CSV) -O ./data/data.csv; \
	)

uninstall:
	rm -rf bin/ include/ lib/ lib64 pyvenv.cfg share/

fclean: uninstall
	rm -rf __pycache__/ src/__pycache__/ src/*.pyc src/*/__pycache__/ src/*/*.pyc data

re: fclean all

.PHONY: all install uninstall fclean re $(NAME)