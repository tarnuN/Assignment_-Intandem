import folium
import pandas as pd
def create_map(df, stoppages):
    df['timestamp'] = pd.to_datetime(df['eventGeneratedTime'], unit='ms')
    fmap = folium.Map(location=[df['latitude'][0], df['longitude'][0]], zoom_start=14)

    # Draw path line
    folium.PolyLine(df[['latitude', 'longitude']].values, color='blue').add_to(fmap)

    # Add stoppage markers
    for s in stoppages:
        popup = f"""
        <b>Reach:</b> {s['reach_time']}<br>
        <b>End:</b> {s['end_time']}<br>
        <b>Duration:</b> {s['duration_min']} min
        """
        folium.Marker(
            location=[s['lat'], s['lon']],
            popup=popup,
            icon=folium.Icon(color='red', icon='pause')
        ).add_to(fmap)

    fmap.save('templates/map.html')
