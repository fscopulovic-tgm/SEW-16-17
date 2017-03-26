import client.ClientConstructor;
import verlag.VerlagConstructor;
import zeitung.Zeitung;

import java.util.ArrayList;

/**
 * @author Filip Scopulovic
 * @date 14.03.2017
 * @use Run-class for the application
 */
public class RunClass {

    /**
     * Run class for the whole application
     *
     * @param args
     */
    public static void main(String[] args) {
        ArrayList<Zeitung> zeitungen = new ArrayList<>();

        for(int i = 0; i < 3; i++)
            zeitungen.add(new Zeitung());

        new VerlagConstructor(zeitungen);

        for(int i = 0; i < 3; i++)
            new ClientConstructor(zeitungen);
    }
}
