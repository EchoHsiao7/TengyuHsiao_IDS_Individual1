setup:
	pip install -r requirements.txt

lint:
	ruff check .

format:	
	black *.py 


test:
	pytest --nbval main.ipynb
	pytest test_script.py test_lib.py


clean:
	find . -type f -name "*.pyc" -delete
