from PIL import Image, ImageDraw, ImageFont
import shutil

headline = 'The Pop Shop'
bottomline = '3pm Tuesdays'
social = 'ury.org.uk | @ury1350'
brand = '#002d5a'
topText = 350
bottomText = 800
btmPadding = 70

W, H = (1000, 1000)
img = Image.new('RGB', (W, H), color=brand)
fontsize = 60

roboto = ImageFont.truetype('../settings/fonts/Roboto-Regular.ttf', 60)
raleway = ImageFont.truetype('../settings/fonts/Raleway-Regular.ttf', 50)
d = ImageDraw.Draw(img)

w, h = d.textsize(headline, roboto)
while w > 900:
    fontsize -= 5
    w, h = d.textsize(headline, ImageFont.truetype(
        '../settings/fonts/Roboto-Regular.ttf', fontsize))
roboto = ImageFont.truetype(
    '../settings/fonts/Roboto-Regular.ttf', fontsize)
pos = (((W-w)/2, topText))
d.text(pos, headline, fill=(255, 255, 255), font=roboto)

w, h = d.textsize(bottomline, raleway)
pos = (((W-w)/2, bottomText))
d.text(pos, bottomline, fill=(255, 255, 255), font=raleway)

w, h = d.textsize(social, raleway)
pos = (((W-w)/2, bottomText + btmPadding))
d.text(pos, social, fill=(255, 255, 255), font=raleway)


foreground = Image.open("logo.png")
basewidth = 600
wpercent = (basewidth/float(foreground.size[0]))
hsize = int((float(foreground.size[1])*float(wpercent)))
foreground = foreground.resize((basewidth, hsize), Image.ANTIALIAS)
img.paste(foreground, (200, 30), foreground)


img.save('showimage.png')

original = r'showimage.png'
target = r'../settings/backgrounds/ury.png'

shutil.copyfile(original, target)
