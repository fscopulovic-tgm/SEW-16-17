package servlet;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicLong;


public class PrimeSearcherWorker extends Thread 
{
	
	private AtomicLong numbers;
	private AtomicLong primenumber;
	private long startTime;
	private volatile boolean running;
	
	/**
	 * Constructor of the PrimeSearcherWorker
	 * Calls the Constructor of the Thread class
	 * It sets the AtomicInteger to a million
	 * It also initializes a CopyOnWriteArrayList for the found prime numbers
	 * The CopyOnWriteArrayList is thread safe and I got the tip from Kevin Waldock
	 */
	public PrimeSearcherWorker()
	{
		super();
		this.running = true;
		this.numbers = new AtomicLong(1000000000000001L);
		this.primenumber = new AtomicLong(0);
	}
	
	/**
	 * Run method for the worker class
	 * It is used because this class inheritance from the Thread class 
	 */
	@Override
	public void run()
	{
		this.startTime = System.currentTimeMillis();
		while (running)
		{
			if (this.isPrime(this.numbers.get()))
			{
				this.primenumber = new AtomicLong(this.numbers.get());
				this.numbers.incrementAndGet();
			} else {
				this.numbers.incrementAndGet();
			}
		}
	}
	
	/**
	 * This method is copied from this site:
	 * https://www.mkyong.com/java/how-to-determine-a-prime-number-in-java/
	 * 
	 * It checks if the given int value is a prime number
	 * It is optimize to perform better
	 * 
	 * The one line comments were inherited from the author
	 * 
	 * @param n The int value that will be checked
	 * @return Returns a true if the number is a prime number and a false if not
	 **/
	private boolean isPrime(long n) 
	{
	    //check if n is a multiple of 2
	    if ((n % 2) == 0) return false;
	    //if not, then just check the odds
	    for (long i = 3; (i * i) <= n; i += 2) 
	    {
	        if ((n % i) == 0)
	            return false;
	    }
	    return true;
	}
	
	/**
	 * @return Last Integer from the CopyOnWriteArrayList
	 */
	public long getPrimenumber() 
	{
		return this.primenumber.get();
	}
	
	/**
	 * @return The current runtime of the worker
	 */
	private long getRunningTime()
	{
		return System.currentTimeMillis() - this.startTime;
	}
	
	/**
	 * Makes a current runtime variable and a help string that gets returned
	 * It checks how long the work thread is running and converts it to a string with the correct unit
	 * The string gets returned
	 * 
	 * @return The current time as a string with the correct unit
	 */
	public String getFormatedRunTime()
	{
		long runTime = this.getRunningTime();
		String formatedTime = "";
		
		if (TimeUnit.MILLISECONDS.toMinutes(runTime) > 90)
		{
			formatedTime = String.valueOf(TimeUnit.MILLISECONDS.toHours(runTime)) + " hours";
		}
		else if (TimeUnit.MILLISECONDS.toSeconds(runTime) > 180)
		{
			formatedTime = String.valueOf(TimeUnit.MILLISECONDS.toMinutes(runTime)) + " minutes";
		}
		else
		{
			formatedTime = String.valueOf(TimeUnit.MILLISECONDS.toSeconds(runTime)) + " seconds";
		}
		
		return formatedTime;
	}
	
	/**
	 * Sets the attribute running to false
	 * Calls the join method of this thread so it ends safe
	 */
	public void shutdown() 
	{
		this.running = false;
		try {
			this.join();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
