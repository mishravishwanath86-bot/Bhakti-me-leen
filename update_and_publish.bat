@echo off
chcp 65001 > nul
echo ========================================================
echo   🚀 BHAKTI APP - AUTO UPDATE & RELEASE PUBLISHER 🚀
echo ========================================================
echo.
echo नया अपडेट तैयार किया जा रहा है और सभी फोनों के लिए पब्लिश किया जा रहा है...
echo.

cd /d "C:\Users\vishw\.gemini\antigravity-ide\scratch\bhakti-app"
python publish_update.py %*

echo.
echo ========================================================
echo   काम पूरा हुआ! प्रेस कोई भी बटन बंद करने के लिए...
echo ========================================================
pause
