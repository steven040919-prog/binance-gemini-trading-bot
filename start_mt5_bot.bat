@echo off
cd /d "c:\Users\CINDEA\Documents\Crypto"
echo Iniciando Bot Autonomo Exness MetaTrader 5 (Modo Adaptativo IA)...
python src/mt5_bot.py --loop --adaptive-ai --seed-history
pause
