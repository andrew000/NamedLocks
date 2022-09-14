ifeq ($(OS),Windows_NT)
    RM = powershell -Command "Remove-Item -Force"
    RRM = powershell -Command "Remove-Item -Force -Recurse"
else
    RM = rm -f
    RRM = rm -rf
endif

build:
	make clean
	python -m build

test:
	tox

clean:
	$(RRM) dist
