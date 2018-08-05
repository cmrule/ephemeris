import os
import pandas as pd

def load_data(filename='Earth_2017_2020.txt', force_download=False):
    """
    Load ephemeris data, which is currently store in local text files.  Ideally,
    we'd have code here to fetch data directly from JPL

    Parameters:
    -----------
    filename : string (optional)
    force_download : bool (optional)
        If True, force re-download of data

    Returns:
    --------
    df: pandas DataFrame
    """
    print('Loading {}'.format(filename),end='')
    with open(filename, 'r') as myfile:
        qs=myfile.read().split('\n') # .replace('\n', ' ').replace('\t','')    return data

    ii=0
    # Strip the header
    while(qs[ii] != '$$SOE'):
        # print(qs[ii])
        ii=ii+1
    print('\t[{}] {}'.format(ii,qs[ii]),end='')
    ii = ii+1

    df = pd.DataFrame(columns=['jd', 'date', 'x', 'y', 'z', 'u', 'v', 'w', 'lt', 'rg', 'rr'])

    while(qs[ii] != '$$EOE'):
        tmp0 = qs[ii  ].replace('=-',' -').replace('= ',' ').strip().split(' ')
        tmp1 = qs[ii+1].replace('=-',' -').replace('= ',' ').strip().split(' ')
        tmp2 = qs[ii+2].replace('=-',' -').replace('= ',' ').strip().split(' ')
        tmp3 = qs[ii+3].replace('=-',' -').replace('= ',' ').strip().split(' ')
        thisRow = {
            "jd": float(tmp0[0]),
            "date": tmp0[3],
            "x": float(tmp1[2]),
            "y": float(tmp1[5]),
            "z": float(tmp1[8]),
            "u": float(tmp2[1]),
            "v": float(tmp2[3]),
            "w": float(tmp2[5]),
            "lt": float(tmp3[1]),
            "rg": float(tmp3[3]),
            "rr": float(tmp3[5])
        }
        df = df.append(thisRow, ignore_index=True)
        ii=ii+4
    df['date'] = pd.to_datetime(df['date'])
    print('\t[{}] {}.  Done.'.format(ii,qs[ii]))

    return df