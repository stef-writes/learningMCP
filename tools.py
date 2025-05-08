from mcp_instance import mcp
from kaggle.api.kaggle_api_extended import KaggleApi
import os
from dotenv import load_dotenv
import pandas as pd
import openai
import anthropic
import json
from typing import Optional

# Load environment variables
load_dotenv()

# Add this near the top with other imports
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
openai_client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@mcp.tool()
def summarize_liomessidata() -> str:
    """Summarize the liomessidata.csv dataset: number of rows, columns, column names, and first 5 rows."""
    df = pd.read_csv("liomessidata.csv")
    summary = {
        "num_rows": len(df),
        "num_columns": len(df.columns),
        "columns": list(df.columns),
        "head": df.head().to_dict(orient="records")
    }
    return str(summary)

@mcp.tool()
def goals_by_minute_range() -> dict:
    """
    Count Messi's goals in different minute ranges (0-15, 16-30, ..., 76-90+).
    """
    df = pd.read_csv("liomessidata.csv")
    # Clean up 'Minute' column: handle '90+1', '45+2', etc.
    def parse_minute(minute):
        if pd.isnull(minute):
            return None
        if '+' in str(minute):
            base, extra = str(minute).split('+')
            return int(base) + int(extra)
        try:
            return int(minute)
        except ValueError:
            return None

    df['Minute_clean'] = df['Minute'].apply(parse_minute)
    # Define bins and labels
    bins = [0, 15, 30, 45, 60, 75, 120]
    labels = ['0-15', '16-30', '31-45', '46-60', '61-75', '76+']
    df['Minute_range'] = pd.cut(df['Minute_clean'], bins=bins, labels=labels, right=True, include_lowest=True)
    # Count goals in each range
    result = df['Minute_range'].value_counts().sort_index().to_dict()
    return result

@mcp.tool()
def analyze_data_with_claude(query: str, category: Optional[str] = None) -> str:
    """
    Use Claude to analyze Messi's data based on a natural language query.
    Optional category parameter to filter data (e.g., 'LaLiga', 'Champions League').
    
    Example queries:
    - "Analyze Messi's goal distribution across different competitions"
    - "Which season was Messi's most productive and why?"
    - "How did Messi's scoring change throughout his career?"
    """
    # Load and filter the data
    df = pd.read_csv("liomessidata.csv")
    
    # Filter by category if provided
    if category:
        df = df[df['Competition'].str.contains(category, case=False)]
    
    # Prepare data for Claude
    data_sample = df.head(50).to_dict(orient="records")
    stats = {
        "total_goals": len(df),
        "competitions": df['Competition'].unique().tolist(),
        "seasons": df['Season'].unique().tolist(),
        "avg_minute": df['Minute'].mean(),
        "common_type": df['Type'].value_counts().to_dict()
    }
    
    # Create the prompt
    prompt = f"""
    You are a football analyst specializing in Lionel Messi's career statistics.
    
    Here is some summary information about the dataset:
    {json.dumps(stats, indent=2)}
    
    And here is a sample of the data (first 50 rows):
    {json.dumps(data_sample, indent=2)}
    
    User query: {query}
    
    Provide a concise, insightful analysis that answers the query specifically.
    Include relevant statistics and patterns you observe in the data.
    Format your response in markdown.
    """
    
    # Call Claude API
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.content[0].text

@mcp.tool()
def analyze_data_with_gpt(query: str, category: Optional[str] = None) -> str:
    """
    Use GPT to analyze Messi's data based on a natural language query.
    Optional category parameter to filter data (e.g., 'LaLiga', 'Champions League').
    
    Example queries:
    - "Compare Messi's performance in home vs away games"
    - "Analyze goal patterns by minute intervals"
    - "Which teams did Messi score against most frequently?"
    """
    # Load and filter the data
    df = pd.read_csv("liomessidata.csv")
    
    # Filter by category if provided
    if category:
        df = df[df['Competition'].str.contains(category, case=False)]
    
    # Prepare data for GPT
    data_sample = df.head(50).to_dict(orient="records")
    stats = {
        "total_goals": len(df),
        "competitions": df['Competition'].unique().tolist(),
        "seasons": df['Season'].unique().tolist(),
        "avg_minute": df['Minute'].mean(),
        "common_type": df['Type'].value_counts().to_dict()
    }
    
    # Create the prompt
    prompt = f"""
    You are a football analyst specializing in Lionel Messi's career statistics.
    
    Here is some summary information about the dataset:
    {json.dumps(stats, indent=2)}
    
    And here is a sample of the data (first 50 rows):
    {json.dumps(data_sample, indent=2)}
    
    User query: {query}
    
    Provide a concise, insightful analysis that answers the query specifically.
    Include relevant statistics and patterns you observe in the data.
    Format your response in markdown.
    """
    
    # Call OpenAI API
    response = openai_client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a football analytics expert."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )
    
    return response.choices[0].message.content

# Add more tools as needed 