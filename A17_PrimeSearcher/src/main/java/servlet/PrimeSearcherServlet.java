package servlet;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class PrimeSearcherServlet extends HttpServlet 
{

	private static final long serialVersionUID = 1L;

	private PrimeSearcherWorker psw;
	private boolean workerOn;
	
	/**
	 * This method needs to be override and it is from the HttpServlet class
	 * First the method checks if the worker thread is one with the checkWorkerThread()-method
	 * Then it gets the PrintWriter for the HTML for the site
	 * It overwrites the worker
	 */
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException 
	{
		this.checkWorkerThread();
		PrintWriter out = resp.getWriter();
		String output = "<html>"
				+ "<head><title>PrimeSearcher</title></head>"
				+ "<body><h1>Prime number searcher!</h1>"
				+ "<br><a>Last found prime number: " + this.psw.getLastPrimenumber().toString() + "</a>"
				+ "<br><a>Time running: " + this.psw.getFormatedRunTime() + "</a>" 
				+ "</body>"
				+ "</html>";
		out.println(output);
	}
	
	/**
	 * Looks if the worker thread is on
	 * The thread needs only one start, that is why the boolean will be set to true after the thread started
	 */
	private void checkWorkerThread()
	{
		this.workerOn = false;
		if (!(this.workerOn)) {
			this.psw = new PrimeSearcherWorker();
			this.psw.start();
			this.workerOn = true;
		}
	}
}
