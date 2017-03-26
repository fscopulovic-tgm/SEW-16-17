package verlag;

import zeitung.Zeitung;

import java.util.ArrayList;
import java.util.List;

/**
 * @author Filip Scopulovic
 * @date 14.03.2017
 * @use Model-class for the Verlag
 */
public class VerlagModel {
    private List<Zeitung> zeitungen;

    /**
     * Constructor for the VerlagModel-class
     * It initialises the List to an ArrayList
     * and adds three new Zeitung-classes
     */
    public VerlagModel(ArrayList<Zeitung> a) {
        this.zeitungen = a;
    }

    /**
     * Returns the ArrayList that contains the Zeitung-classes
     *
     * @return ArrayList zeitungen
     */
    public ArrayList<Zeitung> getZeitungen() {
        return (ArrayList<Zeitung>) this.zeitungen;
    }
}
