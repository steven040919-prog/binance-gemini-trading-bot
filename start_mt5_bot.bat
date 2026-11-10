@echo off
cd /d "c:\Users\CINDEA\Documents\Crypto"
echo Iniciando Bot Autonomo Exness MetaTrader 5 (1H EMA 200 + Estocastico + Pilares ATR)...
python src/mt5_bot.py --loop --interval 300
pause
