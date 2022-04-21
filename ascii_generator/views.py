from django.shortcuts import render


def index(request):
    response = [
        "..................",
        "#...#..###...###..",
        "#...#.#...#.#.....",
        "#...#.####...###..",
        ".####.#.........#.",
        "....#..####.####..",
        ".###.............."
    ]

    return render(request, "generator/home.html", {
        "art": response
    })
