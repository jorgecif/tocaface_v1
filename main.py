def on_forever():
    if input.acceleration(Dimension.X) > 550:
        basic.show_icon(IconNames.GHOST)
        soundExpression.mysterious.play()
        basic.pause(1000)
    elif input.acceleration(Dimension.Y) > 550:
        basic.show_icon(IconNames.GHOST)
        soundExpression.mysterious.play()
        basic.pause(1000)
    else:
        basic.clear_screen()
basic.forever(on_forever)
