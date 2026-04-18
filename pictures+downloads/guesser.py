import random
import pygame

songs = [
    {"name": "Mount Wario MKW REMIX", "stable_tense": 70, "acoustic_electric": 75, "sparse_massive": 85, "intimate_epic": 85, "usual_unpredictable": 60, "smooth_punchy": 50, "dark_bright": 60, "loopy_journey": 25, "calming_driving": 100, "grounded_floating": 15},
    {"name": "Koopa Beach (Night) MKW REMIX", "stable_tense": 25, "acoustic_electric": 0, "sparse_massive": 15, "intimate_epic": 0, "usual_unpredictable": 20, "smooth_punchy": 10, "dark_bright": 90, "loopy_journey": 10, "calming_driving": 0, "grounded_floating": 10},
    {"name": "Tick Tock Clock MKW REMIX", "stable_tense": 20, "acoustic_electric": 10, "sparse_massive": 30, "intimate_epic": 30, "usual_unpredictable": 80, "smooth_punchy": 80, "dark_bright": 40, "loopy_journey": 20, "calming_driving": 40, "grounded_floating": 60},
    {"name": "Maple Treeway MKW REMIX", "stable_tense": 25, "acoustic_electric": 0, "sparse_massive": 15, "intimate_epic": 20, "usual_unpredictable": 75, "smooth_punchy": 15, "dark_bright": 75, "loopy_journey": 5, "calming_driving": 5, "grounded_floating": 10},
    {"name": "Bowser's Courtyard MKW REMIX", "stable_tense": 80, "acoustic_electric": 10, "sparse_massive": 80, "intimate_epic": 90, "usual_unpredictable": 90, "smooth_punchy": 45, "dark_bright": 35, "loopy_journey": 40, "calming_driving": 90, "grounded_floating": 40},
    {"name": "Koopa Cape", "stable_tense": 55, "acoustic_electric": 65, "sparse_massive": 30, "intimate_epic": 25, "usual_unpredictable": 80, "smooth_punchy": 95, "dark_bright": 90, "loopy_journey": 60, "calming_driving": 60, "grounded_floating": 40},
    {"name": "Toad's Factory", "stable_tense": 70, "acoustic_electric": 25, "sparse_massive": 70, "intimate_epic": 70, "usual_unpredictable": 65, "smooth_punchy": 95, "dark_bright": 30, "loopy_journey": 20, "calming_driving": 80, "grounded_floating": 30},
    {"name": "Moo Moo Meadows", "stable_tense": 25, "acoustic_electric": 10, "sparse_massive": 35, "intimate_epic": 35, "usual_unpredictable": 20, "smooth_punchy": 45, "dark_bright": 90, "loopy_journey": 10, "calming_driving": 20, "grounded_floating": 5},
    {"name": "Coconut Mall MKW REMIX", "stable_tense": 15, "acoustic_electric": 0, "sparse_massive": 30, "intimate_epic": 25, "usual_unpredictable": 50, "smooth_punchy": 35, "dark_bright": 100, "loopy_journey": 20, "calming_driving": 55, "grounded_floating": 25},
    {"name": "Cloudy Court Galaxy MKW REMIX", "stable_tense": 75, "acoustic_electric": 90, "sparse_massive": 90, "intimate_epic": 50, "usual_unpredictable": 50, "smooth_punchy": 40, "dark_bright": 80, "loopy_journey": 45, "calming_driving": 100, "grounded_floating": 20},
    {"name": "Gusty Garden Galaxy MKW REMIX", "stable_tense": 40, "acoustic_electric": 40, "sparse_massive": 60, "intimate_epic": 70, "usual_unpredictable": 35, "smooth_punchy": 70, "dark_bright": 100, "loopy_journey": 70, "calming_driving": 40, "grounded_floating": 15},
    {"name": "MK8 Rainbow Road", "stable_tense": 90, "acoustic_electric": 100, "sparse_massive": 25, "intimate_epic": 80, "usual_unpredictable": 80, "smooth_punchy": 40, "dark_bright": 95, "loopy_journey": 85, "calming_driving": 55, "grounded_floating": 75},
    {"name": "Deal 'Em Out", "stable_tense": 90, "acoustic_electric": 25, "sparse_massive": 55, "intimate_epic": 45, "usual_unpredictable": 20, "smooth_punchy": 80, "dark_bright": 25, "loopy_journey": 5, "calming_driving": 65, "grounded_floating": 5},
    {"name": "Shovel Knight Main Theme", "stable_tense": 35, "acoustic_electric": 100, "sparse_massive": 55, "intimate_epic": 90, "usual_unpredictable": 60, "smooth_punchy": 60, "dark_bright": 85, "loopy_journey": 15, "calming_driving": 85, "grounded_floating": 20},
    {"name": "Resurrections", "stable_tense": 35, "acoustic_electric": 70, "sparse_massive": 20, "intimate_epic": 30, "usual_unpredictable": 35, "smooth_punchy": 70, "dark_bright": 35, "loopy_journey": 0, "calming_driving": 70, "grounded_floating": 0},
    {"name": "Fallen Down (Reprise)", "stable_tense": 80, "acoustic_electric": 80, "sparse_massive": 50, "intimate_epic": 25, "usual_unpredictable": 45, "smooth_punchy": 15, "dark_bright": 60, "loopy_journey": 20, "calming_driving": 0, "grounded_floating": 25},
    {"name": "Soldier", "stable_tense": 10, "acoustic_electric": 0, "sparse_massive": 50, "intimate_epic": 40, "usual_unpredictable": 0, "smooth_punchy": 45, "dark_bright": 15, "loopy_journey": 0, "calming_driving": 60, "grounded_floating": 0},
    {"name": "Your Best Friend", "stable_tense": 70, "acoustic_electric": 100, "sparse_massive": 0, "intimate_epic": 15, "usual_unpredictable": 0, "smooth_punchy": 70, "dark_bright": 80, "loopy_journey": 0, "calming_driving": 10, "grounded_floating": 0},
    {"name": "Everything", "stable_tense": 25, "acoustic_electric": 55, "sparse_massive": 40, "intimate_epic": 50, "usual_unpredictable": 30, "smooth_punchy": 65, "dark_bright": 75, "loopy_journey": 10, "calming_driving": 60, "grounded_floating": 5},
    {"name": "Bone Dry Dunes MKW REMIX", "stable_tense": 55, "acoustic_electric": 70, "sparse_massive": 65, "intimate_epic": 75, "usual_unpredictable": 25, "smooth_punchy": 75, "dark_bright": 20, "loopy_journey": 80, "calming_driving": 95, "grounded_floating": 50},
    {"name": "Ruins", "stable_tense": 70, "acoustic_electric": 45, "sparse_massive": 25, "intimate_epic": 80, "usual_unpredictable": 65, "smooth_punchy": 40, "dark_bright": 40, "loopy_journey": 55, "calming_driving": 15, "grounded_floating": 75},
    {"name": "Dark Horse", "stable_tense": 65, "acoustic_electric": 100, "sparse_massive": 25, "intimate_epic": 75, "usual_unpredictable": 10, "smooth_punchy": 25, "dark_bright": 25, "loopy_journey": 10, "calming_driving": 25, "grounded_floating": 5},
    {"name": "Squeaky Clean Sprint MKW REMIX", "stable_tense": 95, "acoustic_electric": 0, "sparse_massive": 70, "intimate_epic": 85, "usual_unpredictable": 25, "smooth_punchy": 55, "dark_bright": 80, "loopy_journey": 70, "calming_driving": 40, "grounded_floating": 85},
    {"name": "Home", "stable_tense": 65, "acoustic_electric": 0, "sparse_massive": 0, "intimate_epic": 85, "usual_unpredictable": 25, "smooth_punchy": 25, "dark_bright": 65, "loopy_journey": 30, "calming_driving": 0, "grounded_floating": 10},
    {"name": "Anxious Heart", "stable_tense": 20, "acoustic_electric": 20, "sparse_massive": 20, "intimate_epic": 15, "usual_unpredictable": 0, "smooth_punchy": 30, "dark_bright": 75, "loopy_journey": 5, "calming_driving": 50, "grounded_floating": 0},
    {"name": "Dark Hallway MKW REMIX", "stable_tense": 15, "acoustic_electric": 0, "sparse_massive": 55, "intimate_epic": 20, "usual_unpredictable": 20, "smooth_punchy": 5, "dark_bright": 35, "loopy_journey": 10, "calming_driving": 10, "grounded_floating": 15},
    {"name": "Heartache", "stable_tense": 10, "acoustic_electric": 100, "sparse_massive": 40, "intimate_epic": 90, "usual_unpredictable": 20, "smooth_punchy": 60, "dark_bright": 40, "loopy_journey": 10, "calming_driving": 85, "grounded_floating": 20},
    {"name": "Heart Attack", "stable_tense": 20, "acoustic_electric": 0, "sparse_massive": 50, "intimate_epic": 80, "usual_unpredictable": 0, "smooth_punchy": 60, "dark_bright": 65, "loopy_journey": 5, "calming_driving": 45, "grounded_floating": 0},
    {"name": "Pihranha Plant's Lullaby MKW REMIX", "stable_tense": 30, "acoustic_electric": 0, "sparse_massive": 25, "intimate_epic": 65, "usual_unpredictable": 50, "smooth_punchy": 0, "dark_bright": 70, "loopy_journey": 10, "calming_driving": 0, "grounded_floating": 0},
    {"name": "sans.", "stable_tense": 25, "acoustic_electric": 80, "sparse_massive": 20, "intimate_epic": 70, "usual_unpredictable": 10, "smooth_punchy": 55, "dark_bright": 45, "loopy_journey": 5, "calming_driving": 10, "grounded_floating": 0},
    {"name": "CONFIDENT", "stable_tense": 0, "acoustic_electric": 0, "sparse_massive": 45, "intimate_epic": 30, "usual_unpredictable": 0, "smooth_punchy": 65, "dark_bright": 30, "loopy_journey": 5, "calming_driving": 50, "grounded_floating": 0},
    {"name": "Ninja Hideaway MKW REMIX", "stable_tense": 15, "acoustic_electric": 100, "sparse_massive": 60, "intimate_epic": 35, "usual_unpredictable": 20, "smooth_punchy": 90, "dark_bright": 45, "loopy_journey": 5, "calming_driving": 95, "grounded_floating": 5},
    {"name": "Snowy", "stable_tense": 20, "acoustic_electric": 0, "sparse_massive": 5, "intimate_epic": 65, "usual_unpredictable": 65, "smooth_punchy": 10, "dark_bright": 30, "loopy_journey": 0, "calming_driving": 0, "grounded_floating": 40},
    {"name": "Come Alive", "stable_tense": 60, "acoustic_electric": 20, "sparse_massive": 40, "intimate_epic": 15, "usual_unpredictable": 10, "smooth_punchy": 55, "dark_bright": 55, "loopy_journey": 5, "calming_driving": 50, "grounded_floating": 0},
    {"name": "Rosalina in the Observatory MKW REMIX", "stable_tense": 85, "acoustic_electric": 0, "sparse_massive": 70, "intimate_epic": 100, "usual_unpredictable": 25, "smooth_punchy": 75, "dark_bright": 80, "loopy_journey": 30, "calming_driving": 25, "grounded_floating": 15},
    {"name": "Bonetrousle", "stable_tense": 70, "acoustic_electric": 100, "sparse_massive": 55, "intimate_epic": 80, "usual_unpredictable": 10, "smooth_punchy": 95, "dark_bright": 35, "loopy_journey": 0, "calming_driving": 60, "grounded_floating": 10},
]

possible = {"stable_tense": [0, 100], "acoustic_electric": [0, 100], "sparse_massive": [0, 100], "intimate_epic": [0, 100], "usual_unpredictable": [0, 100], "smooth_punchy": [0, 100], "dark_bright": [0, 100], "loopy_journey": [0, 100], "calming_driving": [0, 100], "grounded_floating": [0, 100]}
guessed = []

pygame.mixer.init()  # moved here so it only initializes once

def guess_a_song(all_ranges):
    possible_songs = []
    for i in songs:
        possible_flag = True
        for n in all_ranges:
            if not all_ranges[n][0] <= i[n] <= all_ranges[n][1]:
                possible_flag = False
        if possible_flag and i not in guessed:
            possible_songs.append(i)

    if possible_songs:
        random_song = random.choice(possible_songs)
        guessed.append(random_song)
        return random_song
    return None

def adjust_stats(guess_stats, options):
    same_stats = {k: [] for k in [
        "same_stable_tense","same_acoustic_electric","same_sparse_massive",
        "same_intimate_epic","same_usual_unpredictable","same_smooth_punchy",
        "same_dark_bright","same_loopy_journey","same_calming_driving","same_grounded_floating"
    ]}

    if options:
        print(":)")
        for i in songs:
            for n in possible:
                if possible[n][0] <= i[n] <= possible[n][1]:
                    same_stats["same_"+n].append(i)

        stats_to_change = max(same_stats, key=lambda k: len(same_stats[k]))
        tied = [k for k in same_stats if len(same_stats[k]) == len(same_stats[stats_to_change])]
        stat_to_change = random.choice(tied).replace("same_", "")

        while True:
            more_or_less = input(f"Is it more {stat_to_change.split('_')[0]}[1] or more {stat_to_change.split('_')[1]}[2]? ([3] If similar or idk) ")
            if more_or_less == "1":
                possible[stat_to_change][1] = guess_stats[stat_to_change]
                break
            elif more_or_less == "2":
                possible[stat_to_change][0] = guess_stats[stat_to_change]
                break
            elif more_or_less == "3":
                possible[stat_to_change][0] = max(0, guess_stats[stat_to_change] - 30)
                possible[stat_to_change][1] = min(100, guess_stats[stat_to_change] + 30)
                break
            else:
                print("Invalid answer")
    else:
        print(">:|")
        if len(guessed) == len(songs):
            print("Well, Those are all the songs I know, bro!")
            print("Ask Josiah if he could add the song you were thinking of to my memory! Bye bye!!")
            input("Press Enter to exit...")
            return ("done", None)
        stat = min(possible, key=lambda k: possible[k][1] - possible[k][0])
        possible[stat][0] = max(0, possible[stat][0] - 10)
        possible[stat][1] = min(100, possible[stat][1] + 10)

def check_one():
    guess = guess_a_song(possible)
    if not guess:
        return ("no_options", None)
    print(":o")
    pygame.mixer.music.load("./songs/" + guess["name"] + ".mp3")
    pygame.mixer.music.play()

    while True:
        ans = input("Is your song " + guess["name"] + "? ")
        if ans == "y":
            print("XD")
            print("YAY I got it!")
            print("And it only took me "+str(len(guessed)-1)+" wrong guesses! Hehe")
            print("^w^")
            for k in guess:
                print(k + ": " + str(guess[k]))
            input("Press Enter to exit...")
            return ("done", None)
        elif ans == "n":
            return ("wrong", guess)
        else:
            print("Invalid answer")

# ---------- MAIN LOOP (this fixes recursion) ----------
while True:
    result, guess = check_one()

    if result == "done":
        break
    elif result == "no_options":
        adjust_stats(None, False)
    elif result == "wrong":
        adjust_stats(guess, True)