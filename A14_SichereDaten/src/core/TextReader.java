package core;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public interface TextReader {
	/**
	 * TextReader is the base class for the core Worker and the Decorator TextReaderDecorator
	 * Only Worker and TextReaderDecorator implement this interface
	 *
	 * This class has only one attributed that is here for the input
	 */
	BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

	/**
	 * This method needs to be implemented
	 * It writes the input of the user in a String
	 *
	 * @param s String that will be written in
	 */
	void write(String[] s);

	/**
	 * This method needs to be implemented
	 * It reads the given in by the user out
	 *
	 * @param s String that will be read out
	 */
	void read(String[] s);
}