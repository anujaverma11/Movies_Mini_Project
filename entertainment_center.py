# Calling Class

# Importing python files to acess class Movie

import media
import fresh_tomatoes

# Using Class Movie to initiate objects: toy_story, minions, tangled, frozen, theJungleBook and findingNemo

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        ("https://lumiere-a.akamaihd.net/v1/images/"
                         "open-uri20150422-20810-m8zzyx_5670999f.jpeg"),
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

minions = media.Movie("Minions",
                      "The stroy of Minions, single-celled organisms",
                      ("https://upload.wikimedia.org/wikipedia/en/3/"
                       "3d/Minions_poster.jpg"),
                      "https://www.youtube.com/watch?v=eisKxhjBnZ0")

tangled = media.Movie("Tangled",
                      ("The story of a lost, young princess with long "
                       "magical hair."),
                      ("https://upload.wikimedia.org/wikipedia/en/a/a8/"
                       "Tangled_poster.jpg"),
                      "https://www.youtube.com/watch?v=JYKpIr1lSG0")

frozen = media.Movie("Frozen",
                     ("The story of a fearless princess"
                      "who sets off on a journey alongside a rugged iceman"),
                     ("https://upload.wikimedia.org/wikipedia/en/0/05/"
                      "Frozen_%282013_film%29_poster.jpg"),
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")

theJungleBook = media.Movie("The Jungle Book",
                            ("The story of Mowgli, an orphaned human boy who, "
                             "sets out on a journey of self-discovery while"
                             " evading the threatening Shere Khan."),
                            ("https://upload.wikimedia.org/wikipedia/en/a/a4/"
                             "The_Jungle_Book_%282016%29.jpg"),
                            "https://www.youtube.com/watch?v=5mkm22yO-bs")

findingNemo = media.Movie("Finding Nemo",
                          ("The story of the overprotective Ocellaris"
                           " clownfish named Marlin"),
                          ("https://upload.wikimedia.org/wikipedia/"
                           "en/2/29/Finding_Nemo.jpg"),
                          "https://www.youtube.com/watch?v=2zLkasScy7A")

# tangled.show_trailer()
moview = [toy_story, minions, tangled, frozen, theJungleBook, findingNemo]
fresh_tomatoes.open_movies_page(moview)

# this is to print the Docstrings from class Media
print(media.Movie.__doc__)