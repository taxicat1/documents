import numpy.polynomial

class G2Polynomial:
    """
    This class represents a polynomial in GF(2). It wraps and extends numpy's
    Polynomial class.

    The constructor for this class takes a string of binary digits, rather than
    the list of coefficients used by Polynomial. To create a G2Polynomial for
    x^5 + x^3 + 1, do:

        myPolynomial = G2Polynomial("101001")

    """

    def __init__(self, initValue):
        if isinstance(initValue, str):
            coefficients = list()
            for digit in initValue:
                coefficients.insert(0, int(digit))
            self.polynomial = numpy.polynomial.Polynomial(coefficients)

        elif isinstance(initValue, numpy.polynomial.Polynomial):
            self.polynomial = initValue

        else:
            self.polynomial = None

        self.reduce()

    def reduce(self):
        if self.polynomial:
            coefficients = list()
            for coefficient in self.polynomial:
                coefficients.append(coefficient % 2)
            self.polynomial = numpy.polynomial.Polynomial(coefficients)

    def __str__(self):
        power = self.polynomial.degree()
        first = True
        polynomialString = ""
        for coefficient in reversed(list(self.polynomial)):
            if coefficient != 0 or (power == 0 and first):
                if first:
                    first = False
                else:
                    polynomialString += " + "

                if power == 0 or coefficient > 1:
                    polynomialString += str(int(coefficient))
                if power >= 1:
                    polynomialString += "x"
                if power >= 2:
                    polynomialString += "^" + str(power)

            power -= 1

        return polynomialString

    def toBinaryString(self, minDigits = 0):
        binaryString = ""

        for coefficient in reversed(list(self.polynomial)):
            binaryString += str(int(coefficient))

        while len(binaryString) < minDigits:
            binaryString = "0" + binaryString;

        return binaryString

    def degree(self):
        return self.polynomial.degree()

    def __add__(self, other):
        return G2Polynomial(self.polynomial.__add__(other.polynomial))

    def __mul__(self, other):
        return G2Polynomial(self.polynomial.__mul__(other.polynomial))

    def __mod__(self, other):
        return G2Polynomial(self.polynomial.__mod__(other.polynomial))

    def __pow__(self, other):
        return G2Polynomial(self.polynomial.__pow__(other))

