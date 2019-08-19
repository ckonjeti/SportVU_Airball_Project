import get_coordinates
import get_shot_list
from collections import defaultdict
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.interpolate import *
from scipy.stats import *
from get_ball_coordinates_for_shot_events import get_ball_coordinates_for_shot_events

player_coordinates = defaultdict(dict)  # (playerID: game event id: [coordinates, time])

get_coordinates.main('game.json', player_coordinates)

shot_list = get_shot_list.get_shot_list('shots.csv')

airball_arr = []


def detect_airballs(coord_arr, shot_arr, airball_arr, gameID):
    game_event_list = []

    ball_coord_list = get_ball_coordinates_for_shot_events('game.json')
    #print(ball_coord_list)
    xs, ys, zs, times = [], [], [], []

    for key in ball_coord_list:
        for coords in ball_coord_list.get(key):
            for outer_arr in coords:
                print(outer_arr)
            '''
            if (coords[2] > 9):
                times.append(time)
                xs.append(coords[0])
                ys.append(coords[1])
                zs.append(coords[2])
            else:
                try:
                    xy = polyfit(xs, ys, 1)
                    xz = polyfit(xs, zs, 2)
                    yz = polyfit(ys, zs, 2)

                    if (xy > .99 and xz > .99 and yz > .99):
                        airball_arr.append(times[0])

                    xs.clear()
                    ys.clear()
                    zs.clear()
                    times.clear()
                except:
                    pass
            '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xs, ys, zs)
    plt.ylim(0, 13)

    plt.show()
    #print(airball_arr)


def polyfit(x, y, degree):
    try:
        results = {}

        coeffs = np.polyfit(x, y, degree)

        # Polynomial Coefficients
        results['polynomial'] = coeffs.tolist()

        # r-squared
        p = np.poly1d(coeffs)
        # fit values, and mean
        yhat = p(x)  # or [p(z) for z in x]
        ybar = np.sum(y) / len(y)  # or sum(y)/len(y)
        ssreg = np.sum((yhat - ybar) ** 2)  # or sum([ (yihat - ybar)**2 for yihat in yhat])
        sstot = np.sum((y - ybar) ** 2)  # or sum([ (yi - ybar)**2 for yi in y])
        results['determination'] = ssreg / sstot

        return results['determination']
    except:
        pass


detect_airballs(player_coordinates, shot_list, airball_arr, '21500493')