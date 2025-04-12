# Secrets Configuration

To run this application, you need to configure the following secrets:

- `GEMINI_API_KEY`: Your Gemini API key.
- `WEATHER_API_KEY`: Your Weather API key.
- `GEO_API_KEY`: Your Geo API key.

You can configure these secrets by creating a `.streamlit/secrets.toml` file in the root directory of your project. The file should have the following format:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
WEATHER_API_KEY = "YOUR_WEATHER_API_KEY"
GEO_API_KEY = "YOUR_GEO_API_KEY"
```

Replace `YOUR_GEMINI_API_KEY`, `YOUR_WEATHER_API_KEY`, and `YOUR_GEO_API_KEY` with your actual API keys.

Alternatively, you can set these secrets as environment variables.

**Note:** Make sure to restart the Streamlit app after configuring the secrets.