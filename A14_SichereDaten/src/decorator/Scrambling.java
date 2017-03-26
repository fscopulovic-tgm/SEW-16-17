package decorator;

import core.TextReader;
import encrypter.Encrypter;

/**
 * @author Filip Scopulovic
 * @version 1.0
 */
public class Scrambling extends TextReaderDecorator {
    private TextReader textReader;
    private Encrypter crypt;

    /**
     * Constructor for the Scrambling class
     * It initializes the TextReader textReader with the Parameter
     * Also it initializes the Encrypter-class
     *
     * @param tr TextReader that is used for initializing this.textReader
     */
    public Scrambling(TextReader tr) {
        this.textReader = tr;
        this.crypt = new Encrypter();
    }

    /**
     * Before it encrypts the String array given as a parameter it calls the write()-method from this.textReader with
     * the String array s as a parameter
     * Encrypts the String array given that is as a parameter
     * It encrypts with the object this.crypt
     *
     * @param s String array that will be encrypted
     */
    public void write(String[] s) {
        this.textReader.write(s);
        System.out.println("encrypt:");
        try {
            s[0] = this.crypt.base64encode(s[0]);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * Decrypts the String array that is given as a parameter
     * It decrypts with the object this.crypt
     * After decrypting the String, it calls the read()-method from this.textReader with the String array s as the
     * parameter
     *
     * @param s String array that will be decrypted
     */
    public void read(String[] s) {
        System.out.println("decrypt:");
        try {
            s[0] = this.crypt.base64decode(s[0]);
        } catch (Exception e) {
            e.printStackTrace();
        }
        this.textReader.read(s);
    }
}
