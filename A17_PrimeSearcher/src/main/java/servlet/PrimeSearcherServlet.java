package servlet;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class PrimeSearcherServlet extends HttpServlet 
{

	private static final long serialVersionUID = 1L;
	
	private DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
	private Date startDate = new Date();
	private String foundOn;
	private long primenumber;
	
	private PrimeSearcherWorker psw;
	
	/**
	 * This method needs to be override and it is from the HttpServlet class
	 * First the method checks if the worker thread is one with the checkWorkerThread()-method
	 * Then it gets the PrintWriter for the HTML for the site
	 * It overwrites the worker
	 */
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException 
	{
		this.workerThreadInit();
		this.newPrimeNumberFound();
		
		PrintWriter out = resp.getWriter();	
		
		String output = "<html>"
				+ "<head>"
				+ "<title>PrimeSearcher</title>"
				+ "<style>" + this.getCSS() + "</style>"
				+ "</head>"
				+ "<body>"
				+ "<h1>Prime number searcher!</h1>"
				+ "<div>"
				+ "<h2>Servlet started:</h2>" 
				+ "<p>" + this.dateFormat.format(this.startDate) + "</p>"
				+ "</div>"
				+ "<div>"
				+ "<h2>Prime number:</h2>" 
				+ "<p>" + Long.toString(this.primenumber) + "</p>"
				+ "</div>"
				+ "<div>"
				+ "<h2>Found at:</h2>" 
				+ "<p>" + this.foundOn + "</p>"
				+ "</div>"
				+ "<div>"
				+ "<h2>Running time:</h2>" 
				+ "<p>" + this.psw.getFormatedRunTime() + "</p>" 
				+ "</div>"
				+ "</body>"
				+ "</html>";
		out.println(output);
	}
	
	/**
	 * Looks if the worker thread is on
	 * The thread needs only one start, that is why the boolean will be set to true after the thread started
	 */
	private void workerThreadInit()
	{
		if (this.psw == null) 
		{
			this.psw = new PrimeSearcherWorker();
			this.psw.start();
			this.foundOn = "So far not found";
		}
	}
	
	/**
	 * Checks if a new prime number is found
	 * If yes, then it sets it to the new value and it also sets the finding date of the prime number
	 * Else it does nothing
	 */
	private void newPrimeNumberFound()
	{
		long check = this.psw.getPrimenumber();
		
		if (!(this.primenumber == check))
		{
			this.primenumber = check;
			this.foundOn = dateFormat.format(new Date());
		}

	}
	
	/**
	 * Gets called when the server shutdowns
	 * And it also calls the shutdown method of the worker thread
	 */
	@Override
	public void destroy() {
		// TODO Auto-generated method stub
		super.destroy();
		this.psw.shutdown();
	}
	
	/**
	 * Reads out a CSS file and returns the content as a String
	 * The read line is copied from 
	 * http://stackoverflow.com/questions/5868369/how-to-read-a-large-text-file-line-by-line-using-java
	 */
	private String getCSS()
	{
		String css = "";
		
		try 
		{
			File f = new File("style.css");

            @SuppressWarnings("resource")
			BufferedReader b = new BufferedReader(new FileReader(f));

            String readLine = "";

            while ((readLine = b.readLine()) != null) 
            {
                css += readLine + "\n";
            }
		}
		catch (Exception e)
		{
			e.printStackTrace();
		}
		return css;
	}
}
