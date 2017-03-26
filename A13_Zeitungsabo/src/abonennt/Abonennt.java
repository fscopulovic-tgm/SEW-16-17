package abonennt;

import zeitung.Zeitung;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;
import java.util.Observable;
import java.util.Observer;

/**
 * @author Filip Scopulovic
 * @date 14.03.2017
 * @use This class is used for the subscriber
 */

public class Abonennt implements Observer {
    Observable observer;
    private String artikel;
    private List<Zeitung> zeitungen;

    /**
     * Constructor for the Abonennt-class
     */
    public Abonennt(ArrayList<Zeitung> a) {
        this.zeitungen = a;
    }

    /**
     * Subscribe will get called if the client presses the Button "Abonnieren"
     * in his GUI
     *
     * @param o: the observable object in this case class Zeitung
     */
    public void subscribe(Observable o) {
        this.observer = o;
        this.observer.addObserver(this);
    }

    /**
     * Unsubscribe will get called if the client presses the JButton "Deabonieren" in his GUI
     *
     * @param o: the observable object in this case class Zeitung
     */
    public void unsubscribe(Observable o) {
        this.observer = o;
        this.observer.deleteObserver(this);
    }

    /**
     * This comment was copied from the API
     * Link: https://docs.oracle.com/javase/7/docs/api/java/util/Observer.html
     *
     * This method is called whenever the observed object is changed.
     * An application calls an Observable object's notify
     * Observers method to have all the object's observers notified of the change
     *
     * @param o: the observable object in this case class Zeitung
     * @param arg: an argument passed to the notifyObservers method.
     */
    @Override
    public void update(Observable o, Object arg) {
        if (o instanceof Zeitung) {
            Zeitung news = (Zeitung) o;
            this.artikel = news.getArtikel();
            this.display();
        }
    }

    /**
     * Creates a JOptionPane message dialog where the article is shown
     */
    public void display() {
        JOptionPane.showMessageDialog(null, this.artikel);
    }

    public List<Zeitung> getZeitungen() {
        return zeitungen;
    }
}
