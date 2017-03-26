package zeitung;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Observable;
import java.util.Observer;

/**
 * @author Filip Scopulovic
 * @date 14.03.2017
 * @use This class is used for newspaper
 */

public class Zeitung extends Observable {
    private String artikel;

    /**
     * Constructor
     * It is empty because the class extends from Observable
     */
    public Zeitung() { }

    /**
     * This method calls the methods setChanged() and notifyObservers()
     * setChanged says that there is a change
     * notifyObservers notifies the Observers about the change
     */
    public void artikelChanged() {
        this.setChanged();
        this.notifyObservers();
    }

    /**
     * Gets called when in VerlagGUI the Button "Artikel veröffentlichen" is pressed
     * Changes this.artikel and calls the method arikelChanged()
     *
     * @param a: String that the artikel will be changed to
     */
    public void setArtikel(String a) {
        this.artikel = a;
        this.artikelChanged();
    }

    /**
     * Creates a JOptionPane input dialog where you can write the article
     */
    public void writeArtikel() {
        this.artikel = JOptionPane.showInputDialog(null, "Artikel schreiben");
    }

    /**
     * Returns the arikel
     *
     * @return String artikel
     */
    public String getArtikel() {
        return this.artikel;
    }
}
