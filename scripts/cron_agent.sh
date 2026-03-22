#!/bin/bash
# Cron Agent — Chạy Claude Code mỗi giờ theo PROMPT.md
# Setup: crontab -e → thêm dòng:
# 5 * * * * /Users/sampi_wu/Documents/GitHub/Obsidian_Novel_v2/scripts/cron_agent.sh >> /tmp/cron_agent.log 2>&1

cd /Users/sampi_wu/Documents/GitHub/Obsidian_Novel_v2

echo "=== $(date) === Starting agent session ==="

/usr/local/bin/claude --dangerously-skip-permissions -p "Read and follow PROMPT.md. Do the work, push results." --max-turns 50

echo "=== $(date) === Session complete ==="
