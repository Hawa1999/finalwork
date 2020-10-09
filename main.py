# This is a sample Python script.


import arcade
import random


def main():
    file_name = input("Enter a file name: ")
    data = list()
    lines = open(file_name, 'r')
    for line in lines.readlines():
        split_line = line.split(":")
        split_line[0] = split_line[0].strip()
        split_line[1] = int(split_line[1].strip())
        data.append(split_line)
    lines.close()
    arcade.open_window(800, 800, "project3")
    arcade.set_background_color(arcade.color.FAWN)
    yaxis = arcade.create_line(30, 100, 30, 800, arcade.color.KOBE)
    xaxis = arcade.create_line(30, 100, 800, 100, arcade.color.AVOCADO)
    bar_width = 50
    y_scale = 30
    y_offset = 100
    x_offset = 100
    colors = [arcade.color.AVOCADO, arcade.color.BALL_BLUE, arcade.color.BANANA_MANIA, arcade.color.ARSENIC,
              arcade.color.ANTIQUE_WHITE, arcade.color.BITTERSWEET]
    bars = []
    for i in range(len(data)):
        height = data[i][1]
        bars.append(arcade.create_rectangle_filled(x_offset + i * bar_width * 2, y_offset + int(height) / 4 * y_scale,
                                                   bar_width, height / 2 *
                                                   y_scale, colors[random.randint(0, len(colors) - 1)]))
    text_width = 15
    # paul = arcade.create_rectangle_filled(100, 100, 70, 100, arcade.color.AMARANTH_PURPLE)
    # haleh = arcade.create_rectangle_filled(200, 110, 70, 120, arcade.color.ANTIQUE_WHITE)
    # enping = arcade.create_rectangle_filled(300, 120, 70, 140, arcade.color.AVOCADO)
    # michael = arcade.create_rectangle_filled(400, 130, 70, 160, arcade.color.BALL_BLUE)
    # seikyung = arcade.create_rectangle_filled(500, 140, 70, 180, arcade.color.ARSENIC)
    # john = arcade.create_rectangle_filled(600, 150, 70, 200, arcade.color.BANANA_MANIA)
    # abdul = arcade.create_rectangle_filled(700, 160, 70, 220, arcade.color.BITTERSWEET)
    # text1 = arcade.draw_text("paul", 75, 30, arcade.color.AMARANTH_PURPLE)
    # text2 = arcade.draw_text("haleh", 175, 30, arcade.color.ANTIQUE_WHITE)
    # text3 = arcade.draw_text("enping", 270, 30, arcade.color.AVOCADO)
    # text4 = arcade.draw_text("michael", 370, 30, arcade.color.BALL_BLUE)
    # text5 = arcade.draw_text("seikyung", 470, 30, arcade.color.ARSENIC)
    # text6 = arcade.draw_text("john", 570, 30, arcade.color.BANANA_MANIA)
    # text7 = arcade.draw_text("abdul", 670, 30, arcade.color.BITTERSWEET)
    arcade.start_render()
    for bar in bars:
        bar.draw()
    for i in range(len(data)):
        arcade.draw_text(data[i][0], i * bar_width +
                         x_offset, 80, arcade.color.BARN_RED)
    yaxis.draw()
    xaxis.draw()
    arcade.finish_render()
    arcade.run()


main()

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
