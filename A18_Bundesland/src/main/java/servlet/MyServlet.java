package servlet;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import model.Bundesland;


public class MyServlet extends HttpServlet 
{

	/**
	 * Default serial number
	 */
	private static final long serialVersionUID = 1L;
	
	private List<Bundesland> bl;
	
	/**
	 * The doPost method is used when the client posts something
	 */
	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException
	{
		System.out.println("YEAH1");
	}
	
	/**
	 * The doGet method is the main connection between the server and client
	 * It gets called when the server can get some information from the client
	 */
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException
	{
		this.checkBundesland();
		this.checkSelection(request, response);
	}
	
	/**
	 * Checks which option is selected and calls a method to redirect the client to the new site
	 * @param so The request parameter
	 */
	private void checkSelection(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException
	{
		String wish = request.getParameter("wishSelected");
		String wishState = request.getParameter("wishState");
		RequestDispatcher disp;
		
		if (wish != null) 
		{
			switch (wish)
			{
			case "allCaptials":
				request.setAttribute("typeOfOutput", "all capitals");
				request.setAttribute("output", this.getCaptialsArray());
				disp = request.getRequestDispatcher("/output.jsp");
				disp.forward(request, response);
				break;
			case "federalStates":
				request.setAttribute("typeOfOutput", "all federal states");
				request.setAttribute("output", this.getFederalStatesArray());
				disp = request.getRequestDispatcher("/output.jsp");
				disp.forward(request, response);
				break;
			case "oneCapital":
				String[] outputFederalState1 = this.getFederalStatesArray();
				request.setAttribute("output", outputFederalState1);
				disp = request.getRequestDispatcher("/index2.jsp");
				disp.forward(request, response);
				break;
			default:
				break;
			}
		}
		
		if (wishState != null)
		{
			request.setAttribute("typeOfOutput", "capital");
			
			for (Bundesland item : this.bl) 
			{
				if(item.getBundesland().equals(wishState))
				{
					String[] output = {"Die Haupstadt von "+ wishState + " ist " + item.getHauptstadt()};
					request.setAttribute("output", output);
				}
			}
			
			disp = request.getRequestDispatcher("/output.jsp");
			disp.forward(request, response);
		}
	}
	
	/**
	 * Checks if the attribute this.bl is null
	 * If yes it creates a new ArrayList and adds the federal cities and their capitals
	 * If not it does nothing
	 */
	private void checkBundesland()
	{
		if (this.bl == null)
		{
			this.bl = new ArrayList<>();
			
			this.bl.add(new Bundesland("Oberoesterreich", "Linz"));
			this.bl.add(new Bundesland("Wien", "Wien"));
			this.bl.add(new Bundesland("Niederoesterreich", "St. Poelten"));
			this.bl.add(new Bundesland("Steiermark", "Graz"));
			this.bl.add(new Bundesland("Vorarlberg", "Bregenz"));
			this.bl.add(new Bundesland("Salzburg", "Salzburg"));
			this.bl.add(new Bundesland("Kaernten", "Klagenfurt"));
			this.bl.add(new Bundesland("Tirol", "Innsbruck"));
			this.bl.add(new Bundesland("Burgenland", "Eisenstadt"));
		}
	}
	
	/**
	 * @return An array with all the capitals of the federal states in it
	 */
	private String[] getCaptialsArray()
	{
		String[] captials = new String[this.bl.size()];
		for (int i = 0; i < captials.length; i++)
		{
			captials[i] = this.bl.get(i).getHauptstadt();
		}
		return captials;
	}
	
	/**
	 * @return An array with all the federal states in it
	 */
	private String[] getFederalStatesArray()
	{
		String[] federalStates = new String[this.bl.size()];
		for (int i = 0; i < federalStates.length; i++)
		{
			federalStates[i] = this.bl.get(i).getBundesland();
		}
		return federalStates;
	}
}
