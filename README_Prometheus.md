# Prometheus: Add README for Popularity-in-Socials-

## Project Overview

An AI-powered content generation tool designed specifically for creating engaging short-form video scripts about cryptocurrency tokens. The tool leverages advanced AI technologies to produce compelling 15-60 second video content optimized for social media platforms like TikTok, Instagram, and YouTube.

### Core Purpose
The project addresses the growing demand for concise, informative, and engaging crypto-related content by automating script generation for social media short-form videos. It helps content creators and crypto enthusiasts produce high-quality, trending content about cryptocurrency tokens with minimal manual effort.

### Key Features
- Automated script generation for short-form video content
- AI-powered content creation using GPT-4 technology
- Generation of engaging hook titles and compelling scripts
- Automatic hashtag and call-to-action (CTA) suggestions
- Focus on trending cryptocurrency token topics
- Optimization for social media engagement

### Benefits
- Saves time in content creation process
- Provides professional-quality scripts consistently
- Keeps content aligned with current crypto trends
- Enhances social media content strategy for crypto creators

## Getting Started, Installation, and Setup

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR-USERNAME/ai-crypto-reels.git
cd ai-crypto-reels
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Configuration

1. Create a `.env` file in the project root directory
2. Add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

### Running the Application

To generate crypto content reels, simply run:
```bash
python main.py
```

### Development Mode

For development purposes, ensure you have the following additional dependencies installed:
- pandas
- schedule
- python-dotenv
- openai

### Troubleshooting

- Verify Python version: `python --version`
- Ensure all dependencies are correctly installed
- Check your OpenAI API key permissions and billing status