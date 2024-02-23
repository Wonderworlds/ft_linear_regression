SRC :="./src/"
VENV_NAME :=.
PYTHON := python3
NAME := app
BONUS := bonus
DATA_CSV := https://cdn.intra.42.fr/document/document/23381/data.csv

$(NAME):
	python3 $(SRC)app.py

$(BONUS):
	python3 $(SRC)app.py bonus=true

all: install
	python3 $(SRC)app.py

install:
	@echo "Creating virtual environment..."
	( \
		mkdir -p data; \
		wget $(DATA_CSV) -O ./data/data.csv; \
	 	$(PYTHON) -m venv $(VENV_NAME); \
		source $(VENV_NAME)bin/activate; \
		pip install -r requirements.txt; \
	)

uninstall:
	rm -rf bin/ include/ lib/ lib64 pyvenv.cfg share/

fclean: uninstall
	rm -rf __pycache__/ src/__pycache__/ src/*.pyc src/*/__pycache__/ src/*/*.pyc data

re: fclean all

.PHONY: all install uninstall fclean re $(NAME)