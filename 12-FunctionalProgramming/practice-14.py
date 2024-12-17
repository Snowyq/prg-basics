bottles = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]

tolerance = 0.02

correctly_filled = round(
    len(
        list(
            filter(
                lambda el: 500 * (1 - tolerance) < el and 500 * (1 + tolerance) > el,
                bottles,
            )
        )
    )
    / len(bottles)
    * 100
)

print(100 - correctly_filled)
