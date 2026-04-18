from ortools.constraint_solver import pywrapcp, routing_enums_pb2

songs = [[], [], []]
#     ["Example_song_name",  {"key": "C", "bpm": 108, "time_sig": [4, 4], "instruments": {"percussion": 0, "strings": 0, "keyboard": 4, "woodwind": 5, "bass": 3, "electric": 0, "synth": 0, "picked": 0, "brass": 0}}, 
        #     {"key": "C", "bpm": 108, "time_sig": [4, 4], "instruments": {"percussion": 4, "strings": 0, "keyboard": 3, "woodwind": 5, "bass": 1, "electric": 0, "synth": 0, "picked": 0, "brass": 0}}]

major = ["C", "G", "D", "A", "E", "B", "F#", "C#", "G#", "D#", "A#", "F"]
minor = ["a", "e", "b", "f#", "c#", "g#", "d#", "a#", "f", "c", "g", "d"]

def get_diff(start_index, end_index, printing):
    # KEY v
    # making major-minor not matter
    if songs[start_index][2]["key"] in major:
        happy_1 = True
        key_num_1 = major.index(songs[start_index][2]["key"])
    else:
        happy_1 = False
        key_num_1 = minor.index(songs[start_index][2]["key"])
    if songs[end_index][1]["key"] in major:
        happy_2 = True
        key_num_2 = major.index(songs[end_index][1]["key"])
    else:
        happy_2 = False
        key_num_2 = minor.index(songs[end_index][1]["key"])
    # difference around the circle of fifths
    key_diff = (key_num_2 - key_num_1) % 12
    key_diff = min(key_diff, 12 - key_diff)
    # if one is major and the other is minor
    if happy_1 != happy_2:
        key_diff += 1
        # if one is just the opposite of the other :)
        if (happy_1 and major[key_num_1] == minor[key_num_2].upper()) or (happy_2 and minor[key_num_1] == major[key_num_2].lower()):
            key_diff = 1
    # KEY ^

    # BPM v
    # number difference
    bpm_diff = min(max(songs[end_index][1]["bpm"]/songs[start_index][2]["bpm"], songs[start_index][2]["bpm"]/songs[end_index][1]["bpm"]), max(songs[end_index][1]["bpm"]*2/songs[start_index][2]["bpm"], songs[start_index][2]["bpm"]/(songs[end_index][1]["bpm"]*2)), max(songs[end_index][1]["bpm"]/(songs[start_index][2]["bpm"]*2), songs[start_index][2]["bpm"]*2/songs[end_index][1]["bpm"]))
    # different time signature shinanigens
    # if not the exact same
    if songs[start_index][2]["time_sig"] != songs[end_index][1]["time_sig"]:
        # if mathematically the same
        if songs[start_index][2]["time_sig"][0]/songs[start_index][2]["time_sig"][1] == songs[end_index][1]["time_sig"][0]/songs[end_index][1]["time_sig"][1]:
            bpm_diff += bpm_diff*.2
        # if 2-3 ratio
        elif bool(songs[start_index][2]["time_sig"][0]%3) != bool(songs[end_index][1]["time_sig"][0]%3):
            bpm_diff += bpm_diff
        # must be 1/2 ratios or something
        else:
            bpm_diff += bpm_diff*.4

    # BPM ^

    # INSTRUMENTS v
    instrument_diff = 0
    for i in songs[start_index][2]["instruments"]:
        # if the instrument is used in both
        if songs[start_index][2]["instruments"][i] and songs[end_index][1]["instruments"][i]:
            instrument_diff += abs(songs[end_index][1]["instruments"][i] - songs[start_index][2]["instruments"][i])/3
        elif ((not songs[start_index][2]["instruments"][i]) and songs[end_index][1]["instruments"][i] or songs[start_index][2]["instruments"][i] and (not songs[end_index][1]["instruments"][i])):
            instrument_diff += abs(songs[end_index][1]["instruments"][i] - songs[start_index][2]["instruments"][i])
    # INSTRUMENTS ^
    
        key_multiplier = 10
        bpm_exponent = 22
        instrument_exponent = 2

        if bpm_diff**bpm_exponent > 500:
            final_bpm_diff = 500
        else:
            final_bpm_diff = bpm_diff**bpm_exponent
    if printing:
        print("Key: "+str(int(key_diff*key_multiplier))+", BPM/Time: "+str(int(final_bpm_diff))+", Instruments: "+str(int(instrument_diff**instrument_exponent)))
    total_diff = int(key_diff*key_multiplier) + int(final_bpm_diff) + int(instrument_diff**instrument_exponent)
    return(total_diff)

n = len(songs)

distance_matrix = [
    [get_diff(i, j, False) for j in range(n)]
    for i in range(n)
]


# The other stuff idk
def solve_playlist(distance_matrix):
    n = len(distance_matrix)

    manager = pywrapcp.RoutingIndexManager(n, 1, 0)  
    routing = pywrapcp.RoutingModel(manager)

    # Distance callback
    def distance_callback(from_index, to_index):
        i = manager.IndexToNode(from_index)
        j = manager.IndexToNode(to_index)
        return int(distance_matrix[i][j] * 100)  # scale to int

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Search settings
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
    )
#     CHANGE THE TIME Taken to find the path
    search_parameters.time_limit.seconds = 60

    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        index = routing.Start(0)
        route = []

        while not routing.IsEnd(index):
            node = manager.IndexToNode(index)
            route.append(node)
            index = solution.Value(routing.NextVar(index))

        return route
    else:
        return None
    
route = solve_playlist(distance_matrix)

total = 0
for i in range(len(route)):
    print(songs[route[i]][0])
    try: 
        diff = get_diff(route[i], route[i+1], True)
        print(diff)
        total += diff
    except IndexError:
        diff = get_diff(route[i], route[0], True)
        print(diff)
        print("Total is: "+str(total+diff))