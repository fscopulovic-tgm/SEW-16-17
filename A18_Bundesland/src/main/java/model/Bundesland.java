package model;

import java.io.Serializable;

public class Bundesland implements Serializable
{
	
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	private String bundesland;
	private String hauptstadt;
	
	/**
	 * This constructor only calls the second constructor with the parameters set to null
	 */
	public Bundesland()
	{
		this(null, null);
	}
	
	/**
	 * Second constructor with parameters that sets the parameters to the attributes
	 * 
	 * @param bundesland The federal state
	 * @param hauptstadt The capital of the federal state
	 */
	public Bundesland(String bundesland, String hauptstadt)
	{
		this.bundesland = bundesland;
		this.hauptstadt = hauptstadt;
	}
	
	/**
	 * @return The name of the federal state
	 */
	public String getBundesland()
	{
		return this.bundesland;
	}
	
	/**
	 * @return The capital of an federal state
	 */
	public String getHauptstadt()
	{
		return this.hauptstadt;
	}
}
