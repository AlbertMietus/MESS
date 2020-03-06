default: run

run: run_python run_java

run_python: sort_async.py
	python $<

run_java: SortAsync.class Task.class
	java SortAsync Task

SortAsync.class Task.class: SortAsync.java
	javac SortAsync.java

clean:
	rm *.class
