@echo off
cd /d "c:\Users\CINDEA\Documents\Crypto"
set MT5_STRATEGY_MODE=SUPERVISED_M15_SCALPER
set MT5_TRADING_WINDOW_START=8
set MT5_TRADING_WINDOW_END=23
set MT5_LOCAL_TZ_OFFSET=-6
set MT5_SUPERVISED_MAX_POSITIONS=6
echo Iniciando Bot Exness MT5 - Modo 3: SUPERVISED_M15_SCALPER (Ventana 08:00-23:00 UTC-6)...
python src/mt5_bot.py --loop --supervised-scalper --interval 60
pause
