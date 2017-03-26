package encrypter;

import sun.misc.BASE64Decoder;
import sun.misc.BASE64Encoder;

/**
 * @author Filip Scopulovic
 * @version 1.0
 */
public class Encrypter {
    private final static String DEFAULT_ENCODING = "UTF-8";
    private BASE64Encoder enc;
    private BASE64Decoder dec;

    /**
     * Constructor of the Encrypter class
     * It initializes both enc and dec
     * enc is a type of BASE64Encoder, this is used for encrypting
     * dec is a type of BASE64Decoder, this is used for decrypting
     */
    public Encrypter() {
        this.enc = new BASE64Encoder();
        this.dec = new BASE64Decoder();
    }

    /**
     * This method is encrypts the String that is given as a parameter
     * This method was copied from: http://stackoverflow.com/questions/1205135/how-to-encrypt-string-in-java
     *
     * @param text String that will be encrypted
     * @return It returns the text that was encrypted, if there is an Exception, then it will return null
     */
    public String base64encode(String text) {
        try {
            return enc.encode(text.getBytes(DEFAULT_ENCODING));
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }//base64encode

    /**
     * This method is decrypts the String that is given as a parameter
     * This method was copied from: http://stackoverflow.com/questions/1205135/how-to-encrypt-string-in-java
     *
     * @param text String that will be encrypted
     * @return It returns the text that was decrypted, if there is an Exception, then it will return null
     */
    public String base64decode(String text) {
        try {
            return new String(dec.decodeBuffer(text), DEFAULT_ENCODING);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }//base64decode
}
