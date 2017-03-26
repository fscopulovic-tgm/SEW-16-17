package client;

import abonennt.Abonennt;
import zeitung.Zeitung;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

/**
 * @author Filip Scopulovic
 * @date 14.03.2017
 * @use Constructor-class for the client
 */
public class ClientConstructor {
    private Abonennt a;
    private ClientGUI cg;

    /**
     * Constructor for the ClientConstructor-class
     *
     * @param a: ArrayList that contains the Zeitung
     */
    public ClientConstructor(ArrayList<Zeitung> a) {
        this.a = new Abonennt(a);
        this.cg = new ClientGUI(this.a);
    }
}
