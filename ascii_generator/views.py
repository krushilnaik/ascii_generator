from ascii_generator.models import Letter
from .forms import ArtForm
from django.shortcuts import render
from util.custom_logging import debug, critical


def index(request):
    art = [
        "..................",
        "#...#..###...###..",
        "#...#.#...#.#.....",
        "#...#.####...###..",
        ".####.#.........#.",
        "....#..####.####..",
        ".###.............."
    ]

    if request.method == 'POST':
        # if this is a POST request, pre-populate the form
        form = ArtForm(request.POST)

        if form.is_valid():
            letters = []

            for letter in form.cleaned_data["text"]:
                try:
                    char = Letter.objects.get(letter=letter)
                    debug(f"Successfully retrieved ASCII art for '{letter}'")
                except:
                    critical(f"Unsupported character '{letter}'")

                    return render(request, "generator/home.html", {
                        "art": [f"Unsupported character '{letter}'"],
                        "form": form,
                        "error": True
                    })

                letters.append(char.representation.split("|"))

            art = ["".join(line) for line in zip(*letters)]
        else:
            critical("Invalid form data")
    else:
        # if this is not a POST request, initialize a blank form
        form = ArtForm()

    return render(request, "generator/home.html", {
        "art": art,
        "form": form
    })
