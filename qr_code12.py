"""Simple Qrcode Generator"""

import qrcode as qr
img = qr.make("https://github.com/arshi1606")
img.save("arshi_Github_Link.png")

img = qr.make("https://github.com/harshpatel080503")
img.save("Surprise.png")