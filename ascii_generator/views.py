from ascii_generator.models import Letter
from .forms import ArtForm
from django.shortcuts import render
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


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
        # if this is a POST request
        # create a pre-populated form:
        form = ArtForm(request.POST)

        # check whether it's valid
        if form.is_valid():
            letters = []

            for letter in form.cleaned_data["text"]:
                try:
                    char = Letter.objects.get(letter=letter)
                    logging.debug(
                        f"Successfully retrieved ASCII art for '{letter}'"
                    )
                except:
                    logging.critical(f"Unsupported character '{letter}'")

                    return render(request, "generator/home.html", {
                        "art": [f"Unsupported character '{letter}'"],
                        "form": form,
                        "error": True
                    })
                letters.append(char.representation.split("|"))

            art = ["".join(line) for line in zip(*letters)]
        else:
            logging.critical("Invalid form data")
    else:
        # if a GET (or any other method) we'll create a blank form
        form = ArtForm()

    return render(request, "generator/home.html", {
        "art": art,
        "form": form
    })
