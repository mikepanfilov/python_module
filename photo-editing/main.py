from PIL import Image

image = Image.open('monro.jpg')

red, green, blue = image.split()

red1_coordinates = (50, 0, red.width - 50, red.height)
red2_coordinates = (100, 0, red.width, red.height)
croped_red1 = red.crop(red1_coordinates)
croped_red2 = red.crop(red2_coordinates)
blended_red = Image.blend(croped_red1, croped_red2, 0.7)

blue1_coordinates = (50, 0, blue.width - 50, blue.height)
blue2_coordinates = (0, 0, blue.width - 100, blue.height)
croped_blue1 = blue.crop(blue1_coordinates)
croped_blue2 = blue.crop(blue2_coordinates)
blended_blue = Image.blend(croped_blue1, croped_blue2, 0.7)

green_coordinates = (50,0,green.width-50,green.height)
croped_green = green.crop(green_coordinates)

monroe_avtr = Image.merge('RGB', (blended_red, croped_green, blended_blue))
monroe_avtr.thumbnail((80, 70))

monroe_avtr.save('monroe_avtr.jpg')