import pandas as pd

def detect_stoppages(df, threshold_minutes):
    df['timestamp'] = pd.to_datetime(df['eventGeneratedTime'], unit='ms')

    stoppages = []
    i = 0
    while i < len(df) - 1:
        start = i
        while (i < len(df) - 1 and
               df.loc[i, 'latitude'] == df.loc[i+1, 'latitude'] and
               df.loc[i, 'longitude'] == df.loc[i+1, 'longitude']):
            i += 1
        end = i
        duration = (df.loc[end, 'timestamp'] - df.loc[start, 'timestamp']).total_seconds() / 60
        if duration >= threshold_minutes:
            stoppages.append({
                'lat': df.loc[start, 'latitude'],
                'lon': df.loc[start, 'longitude'],
                'reach_time': df.loc[start, 'timestamp'],
                'end_time': df.loc[end, 'timestamp'],
                'duration_min': round(duration, 2)
            })
        i += 1
    return stoppages
