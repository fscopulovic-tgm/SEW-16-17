package decorator;

import core.TextReader;

/**
 * @author Filip Scopulovic
 * @version 1.0
 */
public class Authentication extends TextReaderDecorator {
    private TextReader textReader;
    private String password;

    /**
     * Constructor for the Authentication class
     * It initializes the TextReader textReader with the Parameter
     *
     * @param tr TextReader that is used for initializing this.textReader
     */
    public Authentication(TextReader tr) {
        this.textReader = tr;
    }

    /**
     * Will set a password, so you secure your text
     * After the password is set it calls the write()-method from this.textReader with the String array s as the
     * parameter
     *
     * @param s String array that is used as the parameter for the write()-method
     */
    public void write(String[] s) {
        System.out.println("PASSWORD:   ");
        try {
            this.password = in.readLine();
            this.textReader.write(s);
        } catch(Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * This method checks for if the password given in from the user is the same as the other password
     * If it's true then it will call the read()-method from this.textReader with the String array s as the
     * parameter
     *
     * @param s String array that is used as the parameter for the read()-method
     */
    public void read(String[] s) {
        System.out.println("Passwort eingeben");
        try {
            if (this.password.equals(in.readLine())) {
                this.textReader.read(s);
            } else {
                System.out.println("Falsches Password");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
