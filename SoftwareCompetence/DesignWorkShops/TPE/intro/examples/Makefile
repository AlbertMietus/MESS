default: run

run: run_python run_java

run_python: TPE_demo_1.py
	python $<

run_java: TPE_demo_2.class Task.class
	java TPE_demo_2 Task

TPE_demo_2.class Task.class: TPE_demo_2.java
	javac $<

clean:
	rm *.class
