import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.Future;
import java.util.concurrent.ExecutionException;

public class TPE_demo_2 {

    private static final int TRIES     = 10;
    private static final int WORKERS   = 4;

    public static void main(String[] args) {
        demo();
    }

    private static void demo() {
        ThreadPoolExecutor workers = (ThreadPoolExecutor) Executors.newFixedThreadPool(WORKERS); //* (1)
        List<Future<Long>> resultList = new ArrayList<>();

        //* (2) Sumbit all task, with a random input
        for (int i = 1; i <= TRIES; i++) {
            Future<Long> future = workers.submit(new DemoTask((long) (Math.random() * 10)));
            resultList.add(future); // And save future result
        }

        //* (3) Now print all results; wait on the when needed [.get() does]
        for(Future<Long> f : resultList) {
            try {
                System.out.println("Future done (Y/N)? :" + f.isDone() + ".\tResult is: " + f.get());
            } catch (InterruptedException | ExecutionException e) {
                e.printStackTrace();
            }
        }

        //* Stop the workers
        workers.shutdown();
    }
}


class DemoTask implements Callable {
    Long number;

    public DemoTask(Long number) {
        this.number = number;                      // JAVA: save the input of this "function
    }


    public Long call() {
        try {
            TimeUnit.SECONDS.sleep(number/4);  // Simulate a complicated calculations ...
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return number * number;           //  ... returning the square
    }
}

