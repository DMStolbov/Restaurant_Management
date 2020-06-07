from PIL import Image, ImageDraw, ImageFont

def print_check(num_pep, open_h, close_h, disc, dishes, total):
    img = Image.new('RGBA', (400, 600), 'tan')
    str1 = "Check"
    str2 = "---------------------"
    str3 = f"Number of people: {num_pep} "
    str4 = f"Opened at {open_h}"
    str5 = f"Closed at {close_h}"
    str6 = f"Discount: {disc} %"
    str7 = f"Overall: {total} "
    str8 = "Dishes: "
    font = ImageFont.truetype("arial.ttf", 50)
    font2 = ImageFont.truetype("arial.ttf", 18)
    font3 = ImageFont.truetype("arial.ttf", 18)
    draw = ImageDraw.Draw(img)
    # draw.text(((900-w)/2, (900-h)/2), str1, font=font, fill="white")
    # draw.text(((10,10), str1, font=font, fill="white")
    draw.text((100, 10), str1, font=font, fill="black")
    draw.text((10, 60), str2, font=font, fill="black")
    draw.text((10, 108), str3, font=font2, fill="black")
    draw.text((10, 140), str4, font=font3, fill="black")
    draw.text((200, 140), str5, font=font3, fill="black")
    draw.text((10, 174), str6, font=font3, fill="black")
    draw.text((10, 180), str2, font=font, fill="black")
    draw.text((10, 500), str2, font=font, fill="black")
    draw.text((10, 550), str7, font=font3, fill="black")
    draw.text((10, 230), str8, font=font3, fill="black")
    i = 260
    for dish in dishes:
        draw.text((10, i), dish, font=font3, fill="black")
        i += 20
    img.show()