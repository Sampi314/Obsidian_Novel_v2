#!/bin/bash

# Configuration
PROJECT_DIR="/Users/sampi_wu/Documents/GitHub/Obsidian_Novel_v2"
PROMPT_FILE="$PROJECT_DIR/PROMPT.md"
LOG_DIR="$PROJECT_DIR/logs"
LOG_FILE="$LOG_DIR/scheduled_task.log"
GEMINI_BIN="/usr/local/bin/gemini"

# Environment
export HOME="/Users/sampi_wu"
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

# Ensure log directory exists
mkdir -p "$LOG_DIR"

# Log start time
echo "--- Task started at $(date) ---" >> "$LOG_FILE"

# Run Gemini with the prompt content
# Using -p to pass the content of PROMPT.md
if [ -f "$PROMPT_FILE" ]; then
    cd "$PROJECT_DIR"
    "$GEMINI_BIN" -p "$(cat "$PROMPT_FILE")" >> "$LOG_FILE" 2>&1
    RESULT=$?
    echo "--- Task finished at $(date) with exit code $RESULT ---" >> "$LOG_FILE"
else
    echo "Error: Prompt file not found at $PROMPT_FILE" >> "$LOG_FILE"
    exit 1
fi
