from ascii_generator.models import Letter
from .forms import ArtForm
from django.shortcuts import render
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


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
                except:
                    logging.error(f"Unsupported character '{letter}'")
                letters.append(char.representation.split("|"))

            art = ["".join(line) for line in zip(*letters)]

            return render(request, 'generator/home.html', {"art": art, "form": form})
        else:
            logging.error("Invalid form data")
    else:
        # if a GET (or any other method) we'll create a blank form
        form = ArtForm()

    return render(request, "generator/home.html", {
        "art": response,
        "form": form
    })
