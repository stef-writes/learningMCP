from mcp_instance import mcp
import pandas as pd

@mcp.tool()
def goals_by_minute_range() -> dict:
    """
    Count Messi's goals in different minute ranges (0-15, 16-30, ..., 76-90+).
    """
    df = pd.read_csv("liomessidata.csv")
    # Clean up 'Minute' column: handle '90+1', '45+2', etc.
    def parse_minute(minute):
        try:
            # Handle empty/missing values
            if pd.isna(minute):
                return None
            
            # Handle stoppage time notation (e.g., "90+1")
            if '+' in str(minute):
                parts = str(minute).split('+')
                if len(parts) == 2:
                    try:
                        base = int(parts[0])
                        extra = int(parts[1])
                        return base + extra
                    except (ValueError, TypeError):
                        return None
            
            # Try simple integer conversion
            return int(minute)
        except (ValueError, TypeError):
            # Return None for any unparseable values
            return None

    # Apply the safer parsing function
    df['Minute_clean'] = df['Minute'].apply(parse_minute)
    
    # Remove rows with unparseable minutes
    df = df.dropna(subset=['Minute_clean'])
    
    # Define bins and labels
    bins = [0, 15, 30, 45, 60, 75, 120]
    labels = ['0-15', '16-30', '31-45', '46-60', '61-75', '76+']
    
    # Apply the binning
    df['Minute_range'] = pd.cut(df['Minute_clean'], bins=bins, labels=labels, right=True, include_lowest=True)
    
    # Count goals in each range
    result = df['Minute_range'].value_counts().sort_index().to_dict()
    return result 