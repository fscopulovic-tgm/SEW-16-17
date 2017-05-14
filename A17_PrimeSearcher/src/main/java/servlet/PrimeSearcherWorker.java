package servlet;

import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;

public class PrimeSearcherWorker extends Thread 
{
	
	private AtomicInteger numbers;
	private CopyOnWriteArrayList<Integer> primenumbers;
	private long startTime;
	
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
		this.numbers.set(1000000);
		this.primenumbers = new CopyOnWriteArrayList<>();
	}
	
	/**
	 * Run method for the worker class
	 * It is used because this class inheritance from the Thread class 
	 */
	@Override
	public void run()
	{
		
		this.startTime = System.currentTimeMillis();
		while (true)
		{
			if (this.isPrime(this.numbers.get()))
			{
				this.primenumbers.add(this.numbers.get());
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
	 */
	boolean isPrime(int n) 
	{
	    //check if n is a multiple of 2
	    if ((n % 2) == 0) return false;
	    //if not, then just check the odds
	    for(int i = 3; (i * i) <= n; i += 2) 
	    {
	        if((n % i) == 0)
	            return false;
	    }
	    return true;
	}
	
	/**
	 * @return Last Integer from the CopyOnWriteArrayList
	 */
	public Integer getLastPrimenumber() 
	{
		return this.primenumbers.get(this.primenumbers.size());
	}
	
	/**
	 * @return The current runtime of the worker
	 */
	private long getRunningTime()
	{
		return this.startTime - System.currentTimeMillis();
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
}
