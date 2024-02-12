def mass(userPPM):
    ppm = float(userPPM)
    vol = float(input('Volume (ml): '))
    mass = (ppm*vol)/1000
    return mass


def calculatePPM():
    theRatio = float(
        input('Enter the ratio of the metal ions in the powder: '))
    theConcentration = float(input('Enter the desired PPM: '))
    m = mass(theConcentration)
    calculatedPPM = m * (1/theRatio)
    return calculatedPPM


if __name__ == "__main__":
    ppmcalc = calculatePPM()
    print(str(ppmcalc) + ' gm' )
