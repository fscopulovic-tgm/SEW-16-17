package verlag;

import zeitung.Zeitung;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

/**
 * @author Filip Scopulovic
 * @date 14.03.2017
 * @use Constructor-class for the Verlag
 */
public class VerlagConstructor {
    private VerlagModel vm;
    private VerlagGUI vg;

    /**
     * Constructor of the VerlagConstructor-class
     *
     * @param a: ArrayList that contains the Zeitung
     */
    public VerlagConstructor(ArrayList<Zeitung> a) {
        this.vm = new VerlagModel(a);
        this.vg = new VerlagGUI(this.vm);
    }
}
