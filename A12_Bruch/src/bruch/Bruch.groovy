package bruch

/**
 * @author Filip Scopulovic
 * @use Is a class that represents a fraction
 * @date 05-03-2017
 */
class Bruch implements Comparable {
    /**
     * Bruch class shows a fraction
     * It implements also the Comparable class for the equals and compareTo method (Martin Wölfer showed me this)
     * It has two attributes, both of them are BigIntegers
     * z: Is the numerator of the fraction
     * n: Is the denominator of the fraction, from the beginning it's set with a 1
     */
    BigInteger z
    BigInteger n = 1

    /**
     * One constructor of the Bruch class
     * This constructor has one parameter
     * This takes the numerator and denominator of the Bruch b
     * and it sets the numerator and denominator of this class the same as the one of the b object
     *
     * @param Bruch: b
     */
    Bruch (Bruch b) {
        this.z = b.z
        this.n = b.n
    }

    /**
     * One constructor of the Bruch class
     * This constructor has one parameter
     * This takes only the numerator and sets it to z
     * Made with auto-generator
     *
     * @param BigInteger: z
     */
    Bruch (BigInteger z) {
        this.z = z
    }

    /**
     * One constructor of the Bruch class
     * This constructor has two parameters
     * z is the numerator and n is the denominator
     * Made with auto-generator
     *
     * @param BigInteger: z
     * @param BigInteger: n
     */
    Bruch (BigInteger z, BigInteger n) {
        if(n == (0 as BigInteger))
            throw new IllegalArgumentException("Denominator can't be 0")
        this.z = z
        this.n = n
    }

    /**
     * This method returns the fraction as a String
     *
     * @return String: "Bruch(this.z, this.n)"
     */
    String toString(){
        "Bruch(${this.z}, ${this.n})"
    }

    /**
     * Returns the value of the fraction as a double
     *
     * @return double: (this.z / this.n)
     */
    double doubleValue() {
        (this.z / this.n) as double
    }

    /**
     * Method for adding two fractions together
     * This is used for the "+"-operator
     *
     * @param a: The main parameter that can be a number or a Bruch
     * @param b: Is optional if the method is called like this Bruch.plus(1, 2)
     * @return new Bruch that is the result
     */
    Bruch plus(a, b=null) {
        Bruch hb;
        if(b == null) {
            hb = new Bruch(a)
        } else {
            hb = new Bruch(a, b)
        }
        def lcm = lcm(this.n, hb.n) as BigInteger
        this.z = ((this.z * lcm) / this.n) + ((hb.z * lcm) / hb.n) as BigInteger
        this.n = lcm
        new Bruch(this.z, this.n)
    }

    /**
     * Method for subtracting two fractions
     * This is used for the "-"-operator
     *
     * @param a: The main parameter that can be a number or a Bruch
     * @param b: Is optional if the method is called like this Bruch.minus(1, 2)
     * @return new Bruch that is the result
     */
    Bruch minus(a, b=null) {
        Bruch hb;
        if(b == null) {
            hb = new Bruch(a)
        } else {
            hb = new Bruch(a, b)
        }
        def lcm = lcm(this.n, hb.n) as BigInteger
        this.z = ((this.z * lcm) / this.n) - ((hb.z * lcm) / hb.n) as BigInteger
        this.n = lcm
        new Bruch(this.z, this.n)
    }

    /**
     * Method for multiplying two fractions
     * This is used for the "*"-operator
     *
     * @param a: The main parameter that can be a number or a Bruch
     * @param b: Is optional if the method is called like this Bruch.multiply(1, 2)
     * @return new Bruch that is the result
     */
    Bruch multiply(a, b=null) {
        Bruch hb;
        if(b == null) {
            hb = new Bruch(a)
        } else {
            hb = new Bruch(a, b)
        }
        new Bruch((this.z * hb.z), (this.n * hb.n))
    }

    /**
     * Method for dividing two fractions
     * This is used for the "/"-operator
     *
     * @param a: The main parameter that can be a number or a Bruch
     * @param b: Is optional if the method is called like this Bruch.div(1, 2)
     * @return new Bruch that is the result
     */
    Bruch div(a, b=null) {
        Bruch hb;
        if(b == null) {
            hb = new Bruch(a)
        } else {
            hb = new Bruch(a, b)
        }
        new Bruch((this.z * hb.n), (this.n * hb.z))
    }

    /**
     * Method that turns the fraction into negative
     * This is used for the "-"-operator (negative operator)
     *
     * @return Bruch: that has a negative numerate
     */
    Bruch negative() {
        new Bruch(-this.z, this.n)
    }

    /**
     * If the denominator is negative, it switches the numerator to being negative and puts the denominator positive
     */
    void correct() {
        if (this.n < 0) {
            this.z = -this.z
            this.n = -this.n
        }
    }

    /**
     * Method that reduces the fraction using the greatest common divisor
     */
    void shorten() {
        def gdc = gcd(this.z, this.n)
        this.z /= gdc
        this.n /= gdc
    }

    /**
     * This method is used for the comparing a object with the Bruch via the spaceship-operator
     *
     * @param a: Object that is used for the compare
     * @return int: It returns the results of the spaceship-operator (-1, 0, 1)
     */
    @Override
    int compareTo(Object a) {
        this.doubleValue().compareTo(a.doubleValue())
    }

    /**
     * This method is used for comparing a object with the Bruch with the equals-operator
     *
     * @param other Object that is used for the compare
     * @return boolean: The result of the compare
     */
    @Override
    boolean equals(Object other) {
        this.doubleValue() == other.doubleValue()
    }

    /**
     * Martin Wölfer helped me with this class
     *
     * @param a: Class that the fraction is going to be casted at
     * @return The fraction casted to the class given as the parameter
     */
    def asType(Class a) {
        a == String ? toString() : doubleValue().asType(a)
    }
    /**
     * Greatest Common Divisor method
     * Source: https://gist.github.com/jmendeth/1753043
     *
     * @param a: Is the first denominator
     * @param b: Is the second denominator
     * @return int: a
     */
    static gcd(a, b) {
        if (!b) a
        else gcd(b, a%b)
    }

    /**
     * Method for the Lowest Common Multiple
     * Source: https://github.com/adamldavis/z/blob/master/resources/lcm.groovy
     *
     * @param a: Is the first denominator
     * @param b: Is the second denominator
     * @return BigInteger: a
     */
    static lcm(a, b) {
        return (a * b).intdiv(gcd(a, b))
    }

    /**
     * Returns the numerator of the fraction
     * Made with auto-generate
     *
     * @return The z attribute of the Bruch class
     */
    BigInteger getZ() {
        return z
    }

    /**
     * Sets the numerator of the fraction
     * Made with auto-generate
     *
     * @param BigInteger: z
     */
    void setZ(BigInteger z) {
        this.z = z
    }

    /**
     * Returns the denominator of the fraction
     * Made with auto-generate
     *
     * @return The n attribute of the Bruch class
     */
    BigInteger getN() {
        return n
    }

    /**
     * Sets the denominator of the fraction
     * Made with auto-generate
     *
     * @param BigInteger: n
     */
    void setN(BigInteger n) {
        this.n = n
    }
}
