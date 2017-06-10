package model;

import java.io.Serializable;

public class TemperatureConverter implements Serializable {

    private static final long serialVersionUID = 1L;
    private double convert;
    private double converted;
    private boolean initial;
    private String unit;

    /**
     * @return The value of the temperature that will be converted.
     */
    public double getConvert()
    {
        return convert;
    }

    /**
     * @param convert: Sets the parameter as the new convert value.
     */
    public void setConvert(double convert) {
        this.convert = convert;
    }

    /**
     * @return The value of the converted temperature.
     */
    public double getConverted()
    {
        return converted;
    }

    /**
     * @return The unit String
     */
    public String getUnit()
    {
        return unit;
    }

    /**
     * @return Returns the initial value.
     */
    public boolean getInitial()
    {
        return initial;
    }

    /**
     * Initializes the model
     */
    public void init()
    {
        initial = true;
        converted = 0;
        convert = 0;
        unit="";
    }

    /**
     * Resets the model by calling the method init().
     * Returns reset after this.
     *
     * @return String with value "reset".
     */
    public String reset()
    {
        init();
        return "reset";
    }

    /**
     * Converts the attribute convert from Celsius to Fahrenheit.
     * It also sets the attributes unit and converted to their new values.
     */
    public void celsiusToFahrenheit()
    {
        this.initial = false;
        this.unit="Fahrenheit";
        this.converted = (convert * 1.8) + 32;
    }

    /**
     * Converts the attribute convert from Fahrenheit to Celsius.
     * It also sets the attributes unit and converted to their new values.
     */
    public void fahrenheitToCelsius()
    {
        this.initial = false;
        this.unit = "Celsius";
        this.converted = (convert - 32)/ 1.8;
    }

    /**
     * Converts the attribute convert from Kelvin to Celsius.
     * It also sets the attributes unit and converted to their new values.
     */
    public void kelvinToCelsius()
    {
        this.initial = false;
        this.unit = "Celsius";
        this.converted = convert + 273.15;
    }

    /**
     * Converts the attribute convert from Celsius to Kelvin.
     * It also sets the attributes unit and converted to their new values.
     */
    public void celsiusToKelvin()
    {
        this.initial = false;
        this.unit = "Kelvin";
        this.converted = convert - 273.15;
    }

    /**
     * Converts the attribute convert from Kelvin to Fahrenheit.
     * It also sets the attributes unit and converted to their new values.
     */
    public void kelvinToFahrenheit()
    {
        this.initial = false;
        this.unit = "Fahrenheit";
        this.converted = convert + 459.67;
    }

    /**
     * Converts the attribute convert from Fahrenheit to Kelvin.
     * It also sets the attributes unit and converted to their new values.
     */
    public void fahrenheitToKelvin()
    {
        this.initial = false;
        this.unit = "Kelvin";
        this.converted = convert - 459.67;
    }
}
