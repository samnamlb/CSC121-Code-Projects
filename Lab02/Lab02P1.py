#
# Aleem Azimov
# August 27, 2022
# Wavelength Classifier
#

# Get the wavelength.
wavelength = int(input('Enter the wavelength (in nm): '))

# Determine the classification of the wavelength
# and display the result.
if wavelength < 10:
    print('Below range')
elif wavelength >= 10 and wavelength < 401:
    print('Infrared')
elif wavelength >= 401 and wavelength < 701:
    print('Visible light')
elif wavelength >= 701 and wavelength < 1001:
    print('Ultraviolet')
else:
    print('Above range')
