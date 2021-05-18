import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler

from utils.angles import ANGLE_KEYS


def augment_data(path, iterations=5):
    """
    Function that loads a csv file, augments and scales it. Finally saves it again.
    """
    df = pd.read_csv(path)
    positions = df.iloc[:, :-len(ANGLE_KEYS)]
    positions = add_standard_deviation_to_df(positions, scale = 0.005, iterations=iterations, ignore_first=True)
    angles = df.iloc[:, -len(ANGLE_KEYS):]
    angles = add_standard_deviation_to_df(angles, scale=5, iterations=iterations, angle_rescale=360)
    df = positions.reset_index(drop=True).join(angles.reset_index(drop=True))
    df = scaling(df)
    df.to_csv(f'{path}_augmented_scaled')
    return df


def add_standard_deviation_to_df(df: pd.DataFrame, scale: int, iterations: int, angle_rescale = 0, ignore_first=False):
    shape = df.shape
    keeper = pd.DataFrame(df)
    for i in range(iterations):
        if ignore_first:
            first = pd.DataFrame(df.iloc[:, 0])
            rest = df.iloc[:, 1:]
            rest = rest + np.random.normal(0, scale, rest.shape)
            keeper = keeper.append(first.join(rest))
        else:
            keeper = keeper.append(df + np.random.normal(0, scale, df.shape))
    if angle_rescale != 0:
        keeper.applymap(lambda x: angle_formatting(x, angle_rescale))
    return keeper


def angle_formatting(angle, max_degrees):
    if angle < 0:
        angle += max_degrees
    elif angle > max_degrees:
        angle -= angle
        if angle > max_degrees:
            angle -= angle
    return angle

def scaling(df):
    scaler = StandardScaler()
    scaler.fit(df.iloc[:, 1:])
    scaled = scaler.transform(df.iloc[:, 1:])
    df.iloc[:, 1:] = scaled
    return df
