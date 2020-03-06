
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

public class SortAsync {

    private static final int TRIES = 10;
    private static final int MAX_WORKERS = 4;

    public static void main(String[] args) {
        demo();
    }

    private static void demo() {
        ThreadPoolExecutor executor = (ThreadPoolExecutor) Executors.newFixedThreadPool(MAX_WORKERS);

        for (int i = 1; i <= TRIES; i++)
            {
                Task task = new Task("Task " + i);
                System.out.println("Created : " + task.getName());
                executor.execute(task);
            }
        executor.shutdown();
    }

}

class Task implements Runnable {

    String name;

    public Task(String name) {
        this.name = name;
    }

    public void run() {
        try {
            Long duration = (long) (Math.random() * 10);
            System.out.println("Executing : " + name);
            TimeUnit.SECONDS.sleep(duration);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    String getName() {
        return name;
    }
}
